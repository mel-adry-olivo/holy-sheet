from flask import Flask, render_template, request, jsonify
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def uploadFile(): 
    file = request.files['file']
    # test-data.xlsx

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    # uploads/test-data.xlsx

    fileName, fileExtension = os.path.splitext(file.filename)

    # if os.path.exists(file_path):
    #     return jsonify({'message': 'File already exists'}), 400
    
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({'message': f'File upload failed: {str(e)}'}), 500
    
    if(fileExtension == '.csv'):
        df = pd.read_csv(file_path)
    elif(fileExtension == '.xlsx'):
        df = pd.read_excel(file_path)
    else:
        return jsonify({'message': 'Invalid file format'}), 400
    
    
    return df.to_json(orient='records'), 200

if __name__ == "__main__":
    app.run(debug=True)
