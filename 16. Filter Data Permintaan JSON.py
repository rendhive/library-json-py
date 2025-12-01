import json

json_data = '''
[
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Doe", "age": 22}
]
'''

people = json.loads(json_data)
young_people = [person for person in people if person['age'] < 30]

print("People aged under 30:", young_people)
# Fungsi: Menerapkan filter pada data yang diterima dalam format JSON.
# Kondisi: Ketika Anda hanya tertarik pada subset dari data yang lebih besar.
