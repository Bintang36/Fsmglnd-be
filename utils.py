import subprocess
import json

def kancil_keywords_from_image(image_path):
    # Dummy function for extracting keywords
    # Implement your actual image processing and ML model here
    return ["kancil", "hutan", "Kancil adalah anak nakal yang suka mencuri ketimun di kebun tetangganya. Setiap malam, dia menyelinap masuk ke kebun dan mencuri ketimun yang lezat. Namun, suatu hari, ketimun yang dicuri Kancil ternyata beracun! Kancil hampir saja menjadi korban dari keberaniannya yang terlalu berlebihan. Akhirnya, dia belajar dari kesalahannya dan berjanji untuk tidak mencuri lagi."]

def malin_keywords_from_image(image_path):
    # Dummy function for extracting keywords
    # Implement your actual image processing and ML model here
    return ["Malin durhaka"]


def store_data_in_firestore(id, data):
    # Convert data to JSON string
    data_str = json.dumps(data)
    
    # Run Node.js script using subprocess
    result = subprocess.run(
        ['node', 'node_scripts/storeData.js', id, data_str],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(f"Error storing data: {result.stderr}")
    
    return result.stdout
