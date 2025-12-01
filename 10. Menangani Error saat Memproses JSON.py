import json

# JSON yang tidak valid
invalid_json = '{"name": "Tom", "age": 30'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
# Fungsi: Menangani kesalahan saat mencoba mendekode JSON yang tidak valid.
# Kondisi: Ketika Anda ingin memastikan aplikasi Anda bisa menangani input JSON yang tidak benar.
