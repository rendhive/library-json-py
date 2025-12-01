import json

data = {'key': 'value', 'number': 42}
json_bytes = json.dumps(data).encode('utf-8')  # Mengonversi ke bytes

print("JSON as bytes:", json_bytes)
# Fungsi: Mengonversi string JSON ke format biner (bytes).
# Kondisi: Ketika Anda perlu mentransmisikan data JSON dalam format biner.
