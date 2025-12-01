import json

json_data = '{"key": "value", "number": 42}'
data = json.loads(json_data)

print("Decoded data:", data)
# Fungsi: Mengonversi data JSON (dalam bentuk string) kembali ke objek Python.
# Kondisi: Ketika Anda menerima data JSON yang perlu diproses dalam program.
