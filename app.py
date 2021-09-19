import os

from pixel_calc import Pixel_calc
from flask import Flask, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

pixelS=''
hex_color =''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file_upload')
def file_upload():
    return render_template('index.html')

@app.route('/file_uploading', methods=['GET', 'POST'])
def file_uploading():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return redirect(url_for('index'))
            file = request.files['file']
            if file.filename == '' or file.filename is None:
                return redirect(url_for('index'))
            if file:
                fpath = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], fpath))
                global patch
                patch = 'C:/tmp/' + str(file.filename)
                return redirect(url_for('px_calc'))
    except:
        return render_template('index.html')

@app.route('/pixel_calc')
def px_calc():

#    hex_color = request.form['hex_color']
    pixelS = Pixel_calc.pixel(patch)
    return render_template('pixel_calc.html', value=pixelS)

if __name__ == '__main__':
    app.run()
