import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

print("Data yang diambil dari file:", data)
# Fungsi: Memuat data dari file JSON dan menggunakannya dalam program.
# Kondisi: Ketika Anda ingin memanfaatkan data yang sudah ada dan tersimpan.
