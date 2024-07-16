import json

# Objek JSON
element = {
    'human': {
        'nama': 'your namd',
        'usia':17
    }
}

# Hapus properti 'usia'
if 'massa' in element['H']:
    del element['human']['usia']

# Mengubah objek menjadi string JSON
json_string = json.dumps(element, indent=4)

# Tampilkan hasil
print(json_string)
