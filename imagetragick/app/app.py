import os
from flask import Flask, request, redirect, url_for
from wand.image import Image
import time

UPLOAD_FOLDER = './uploads/'
CONVERTED_FOLDER = './converted/'
ALLOWED_EXTENSIONS = set(['mvg', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = f"{time.ctime()}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with Image(filename=os.path.join(app.config['UPLOAD_FOLDER'], filename)) as img:
                img.format = 'png'
                img.save(filename=os.path.join(app.config['CONVERTED_FOLDER'], filename + '.png'))
            return redirect(url_for('upload_file'))

    return '''
    <!doctype html>
    <title>Secure Image Uploader</title>
    <h1>Secure Image Uploader</h1>
    <img src="static/imagemagick.png" />
    <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=file>
        <input type=submit value=Upload></p>
    </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
