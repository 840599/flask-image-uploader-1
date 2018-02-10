# Flask Image Uploader
A Flask website where you can upload pictures and see them.
  - One page to show a different random image (previously uploaded) each 7 seconds
  - Another page to update JPG and PNG file up to 3MB
  - 404 & 413 error are caught


A [demo](https://shielded-basin-20047.herokuapp.com/) is available on Heroku.

# Install
```bash
# Only if you want a virtual environment
virtualenv env-img-uploader
source env-img-uploader/bin/activate

# Install the package
pip install -e . # From the repository root folder

# Run the app 
export FLASK_APP=image-uploader 
export FLASK_DEBUG=1 # for enabling debug mode
export SECRET_KEY=my-custom-key
flask run
```

# Notes
 - Secret key: if no custom key is provided, a default one (in the package) is used
 - Uploaded images are never part of the package
 - Uploaded images are saved in `instance/uploads/` where the app has been launched
 - gunicorn is used only to launched the app on Heroku

# Dependencies
Python:
 - Flask == 0.12.2
 - gunicorn==19.7.1
 
Web: (included in the package)
 - jquery == 3.3.1

