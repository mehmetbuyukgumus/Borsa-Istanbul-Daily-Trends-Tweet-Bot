from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv(dotenv_path= "passwords.env")

# Çevresel değişkenlere eriş
password = os.getenv("myPassword")

# Değerleri yazdır
print(password)
