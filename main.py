import json

# Objek JSON
element = {
    'human': {
        'nama': 'your name',
        'usia':17
    }
}

# Hapus properti 'usia'
if 'massa' in element['human']:
    del element['human']['usia']

# Mengubah objek menjadi string JSON
json_string = json.dumps(element, indent=4)

# Tampilkan hasil
print(json_string)
