from flask import Flask, jsonify, send_file, request
from werkzeug.utils import secure_filename
import os
import base64
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

IMAGE_DIR = r"C:\Users\ASUS\Desktop\github_projects\gallery\gallery-app\test_images"

def get_images():
    images = []
    for filename in os.listdir(IMAGE_DIR):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(IMAGE_DIR, filename)
            with open(file_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                images.append({
                    "filename": filename,
                    "data": encoded_string
                })
    return images

@app.route('/images', methods=['GET'])
def images():
    images = get_images()
    return jsonify(images)

@app.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    file_path = os.path.join(IMAGE_DIR, filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "File not found", 404


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files or 'description' not in request.form:
        return jsonify({'error': 'No file or text provided'}), 400

    file = request.files['image']
    text = request.form['description']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    return jsonify({'filename': filename})



if __name__ == '__main__':
    app.run(debug=True)
