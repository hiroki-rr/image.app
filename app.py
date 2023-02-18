import os
import uuid
from flask import Flask, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import flash
from models import dbConnect

from datetime import timedelta
import hashlib
import re

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





'''@app.route('/')
def test():
    return render_template('test.html')'''

@app.route('/', methods=['POST'])
def uploads_file():
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        # データの取り出し
        file = request.files['file']
        # ファイル名がなかった時の処理
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        
        extension = os.path.splitext(file.filename)[1]
        iid = uuid.uuid4()
        filename = str(iid) + extension

        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(img_path)

        dbConnect.addImage(filename)
        
        img_path = dbConnect.getImage()

        return render_template('my-profile.html', img_path=img_path)

@app.route('/', methods=['GET'])
def show_img():

    return render_template('test.html')


@app.route('/user-profile', methods=['GET'])
def zikoshoukai():

    return render_template('user-profile.html')












if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
