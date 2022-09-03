import os
from flask import Flask,request, render_template
UPLOAD_FOLDER = 'C:\Users\ADMIN\Desktop\6206021612105\upload\ ' #จะเป็นโฟล์เดอร์ที่เก็บไฟล์ที่เรา upload
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/upload', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f= request.files['filename']
        f.save(os.path.join (app.config['UPLOAD_FOLDER'],f.filename))
        return 'upload file success'
if __name__=='__main__':
    app.run(debug=True)


