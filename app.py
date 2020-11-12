from flask import Flask, render_template, request, redirect
import os.path
#from werkzeug import secure_filename

UPLOAD_FOLDER = 'nedlastninger'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload')
def upload_file():
   return render_template("upload.html")
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
     # f.save(f.filename) # denne fungerer men lagrer i feil mappe
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename)) #fjern denne om nedlasting ikke fungerer
      return 'file uploaded successfully'
		
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
   app.run(debug = True)