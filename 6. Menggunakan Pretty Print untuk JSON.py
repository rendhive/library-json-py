import json

data = {'key': 'value', 'number': 42}

# Mengonversi objek Python menjadi JSON dengan format yang lebih terbaca
json_data = json.dumps(data, indent=4)
print("Pretty JSON:\n", json_data)
# Fungsi: Menghasilkan output JSON yang lebih mudah dibaca dengan indentasi.
# Kondisi: Ketika Anda ingin menampilkan data JSON secara lebih jelas, seperti untuk debugging.
