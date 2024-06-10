from flask import Flask, request, jsonify
from models import db, StoryKancil, StoryMalinKudang
from config import Config
from utils import kancil_keywords_from_image, malin_keywords_from_image, store_data_in_firestore
import os
import uuid
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)
address = ('127.0.0.1', 8080)

@app.route('/stories/kancil', methods=['GET'])
def get_kancil_story():
    kancil_story = StoryKancil.query.first()
    if not kancil_story:
        return jsonify({"error": "Cerita Kancil tidak ditemukan"}), 404
    return jsonify(kancil_story.to_dict())

@app.route('/stories/malin_kudang', methods=['GET'])
def get_malin_kudang_story():
    malin_kudang_story = StoryMalinKudang.query.first()
    if not malin_kudang_story:
        return jsonify({"error": "Cerita Malin Kudang tidak ditemukan"}), 404
    return jsonify(malin_kudang_story.to_dict())

@app.route('/kancil_keywords', methods=['POST'])
def extract_kancil_keywords():
    if 'image' not in request.files:
        return jsonify({"error": "No image file uploaded"}), 400

    image = request.files['image']
    image_path = os.path.join("templates", image.filename)
    image.save(image_path)

    keywords = kancil_keywords_from_image(image_path)
    os.remove(image_path)  # Cleanup uploaded image

    # Store keywords in Firestore
    data = {'keywords': keywords}
    doc_id = str(uuid.uuid4())
    try:
        store_data_in_firestore(doc_id, data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"keywords": keywords, "doc_id": doc_id})

@app.route('/malin_keywords', methods=['POST'])
def extract_malin_keywords():
    if 'image' not in request.files:
        return jsonify({"error": "No image file uploaded"}), 400

    image = request.files['image']
    image_path = os.path.join("templates", image.filename)
    image.save(image_path)

    keywords = malin_keywords_from_image(image_path)
    os.remove(image_path)  # Cleanup uploaded image

    # Store keywords in Firestore
    data = {'keywords': keywords}
    doc_id = str(uuid.uuid4())
    try:
        store_data_in_firestore(doc_id, data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"keywords": keywords, "doc_id": doc_id})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')