import json

data = {
    'tests': [
        {'id': 1, 'result': 'pass'},
        {'id': 2, 'result': 'fail'}
    ]
}

json_fixture = json.dumps(data, indent=4)
print("Formatted JSON for testing:\n", json_fixture)
# Fungsi: Memformat JSON untuk kemudahan pembacaan dalam konteks testing.
# Kondisi: Ketika Anda ingin membagikan data untuk kebutuhan debugging atau pengujian.
