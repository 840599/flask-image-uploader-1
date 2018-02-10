import os, random
from flask import Flask, url_for, render_template, redirect, \
                request, send_from_directory, flash, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)
app.config.from_object('image-uploader.default_settings')
app.config.from_envvar('SETTINGS', silent=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024


@app.route("/")
def images():
    return render_template('images.html', random_image=getRandomImage())

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    error = None
    msg = None
    if request.method == 'POST':
        if 'file' not in request.files:
            error = 'No file part'
        else:
            file = request.files['file']
            if file.filename == '':
                error = 'No selected file', 'error'
            else:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    save_file(file, filename)
                    msg = 'File uploaded!'
                else:
                    error = 'The file is not accepted, only .png and .jpg'

    return render_template('upload.html', error=error, msg=msg)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(
            os.path.join(app.instance_path,
                            app.config['UPLOAD_FOLDER']), filename)

@app.route('/uploads/get/random')
def getJSONRandomImage():
    filename = getRandomImage()
    return jsonify( filename )

def getRandomImage():
    upload_path = os.path.join(app.instance_path,
                    app.config['UPLOAD_FOLDER'])
    filename = ""

    if os.path.exists(upload_path):
        files = os.listdir(upload_path)
        if len(files):
            filename = files[random.randint(0,len(files)-1)]

    return url_for('uploaded_file', filename=filename )

def save_file(file, filename):
    upload_path = os.path.join(app.instance_path,
                    app.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    file.save(os.path.join(upload_path, filename))

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.context_processor
def inject_debug():
    return dict(debug=app.debug)

@app.errorhandler(404)
def page_not_found(error):
    error = str(error).split(':')
    error_title = error[0]
    error_message = error[1]
    return render_template('error.html', error_title=error_title, error_message=error_message), 404


if __name__ == "__main__":
    app.run()
