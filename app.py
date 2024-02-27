from flask import Flask

app = Flask(__name__)

def process_image():
    pass

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def hello_world():
    return render_template("about.html")

@app.route("/edit",methods = ["GET","POST"])
def edit():
    if request.method == "POST":
         # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))

    return render_template("edit.html")
if __name__ == "main":


  app.run(debug=True)   