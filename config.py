import os

class Config:
    # Informasi koneksi database Google Cloud SQL
    DB_USER = 'Bintang'
    DB_PASSWORD = '12345678'
    DB_HOST = '34.101.192.86'  # Ganti dengan alamat IP Cloud SQL Anda
    DB_PORT = '3306'  # Ganti dengan port Cloud SQL Anda
    DB_NAME = 'cerita'

    # URL koneksi database
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FIRESTORE_PROJECT_ID = os.getenv('FIRESTORE_PROJECT_ID', 'capstone-bangkit-424311')
