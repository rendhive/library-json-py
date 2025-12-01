import json

json_data = '{"name": "CompanyX", "employees": [{"name": "John"}, {"name": "Sarah"}]}'
data = json.loads(json_data)

print("Nama Perusahaan:", data['name'])
print("Daftar Karyawan:")
for emp in data['employees']:
    print("- ", emp['name'])
# Fungsi: Mengobati dan menggunakan data JSON untuk aplikasi dunia nyata.
# Kondisi: Ketika Anda bekerja dengan data yang lebih berstruktur terkait bisnis atau organisasi.
