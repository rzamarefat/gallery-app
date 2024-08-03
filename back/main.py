from flask import Flask, jsonify, send_file
import os
import base64
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

IMAGE_DIR = r"C:\Users\ASUS\Desktop\github_projects\gallery\gallery-app\test_images"

def get_images():
    images = []
    for filename in os.listdir(IMAGE_DIR):
        if filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
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

if __name__ == '__main__':
    app.run(debug=True)
