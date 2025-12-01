import json

# JSON yang valid
json_data = '{"key": "value", "number": 42}'

# Mengonversi string JSON kembali ke objek Python
try:
    data = json.loads(json_data)
    print("Decoded data:", data)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
# Fungsi: Mendekode string JSON yang valid.
# Kondisi: Saat Anda harus memastikan bahwa data JSON yang diterima aman untuk dikelola.
