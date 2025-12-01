import json

data = {
    'b': 2,
    'a': 1,
    'c': 3
}

# Urutkan kunci saat menyimpan
json_data = json.dumps(data, sort_keys=True)
print("JSON with sorted keys:", json_data)
# Fungsi: Menyimpan data JSON dengan mengurutkan kunci.
# Kondisi: Ketika Anda ingin menyajikan data dengan cara yang teratur untuk keperluan estetika atau logika.
