import json

json_data = '{"name": "Jane", "info": {"age": 25, "city": "London"}}'
data = json.loads(json_data)

# Mengakses data dalam dictionary
print("Name:", data['name'])
print("City:", data['info']['city'])
# Fungsi: Mengakses data terstruktur dalam format JSON.
# Kondisi: Ketika Anda perlu bekerja dengan data bersarang dalam objek JSON.
