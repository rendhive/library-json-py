import json

data = {'key': 'value', 'number': 42}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

print("Data berhasil disimpan ke 'data.json'.")
# Fungsi: Menyimpan objek Python sebagai file JSON.
# Kondisi: Ketika Anda ingin menyimpan data ke disk dalam format JSON.
