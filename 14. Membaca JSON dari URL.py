import json
import requests

# Mengambil data JSON dari URL
response = requests.get('https://api.example.com/data')
data = response.json()  # Dengan requests, Anda dapat langsung memuat JSON

print("Data yang diambil dari API:", data)
# Fungsi: Mengambil dan memuat data JSON dari API eksternal.
# Kondisi: Ketika Anda ingin mendapatkan data dinamis dari web service.
