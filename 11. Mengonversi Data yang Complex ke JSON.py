import json

data = {
    'name': 'Alice',
    'hobbies': ['reading', 'hiking', 'coding'],
    'education': {
        'degree': 'BSc Computer Science',
        'university': 'XYZ University'
    }
}

json_data = json.dumps(data)
print("Encoded complex data to JSON:", json_data)
# Fungsi: Mengonversi objek kompleks ke format JSON.
# Kondisi: Saat Anda memiliki struktur data yang besar dan ingin memformatnya dalam JSON.
