import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

print("Data dibaca dari 'data.json':", data)
# Fungsi: Membaca dan memuat isi file JSON ke dalam objek Python.
# Kondisi: Ketika Anda perlu memuat data dari file JSON yang sudah ada.
