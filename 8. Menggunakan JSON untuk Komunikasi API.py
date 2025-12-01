import json

# Contoh struktur data yang akan dikirim ke API
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

json_payload = json.dumps(data)
print("Payload JSON untuk API:", json_payload)
# Fungsi: Mempersiapkan data dalam format JSON untuk dikirim ke API.
# Kondisi: Saat Anda ingin berinteraksi dengan web service atau API JSON.
