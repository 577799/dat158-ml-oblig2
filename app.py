from flask import Flask, render_template, request, redirect
#from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/upload")

@app.route('/upload')
def upload_file():
   return render_template("upload.html")
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)