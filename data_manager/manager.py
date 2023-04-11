import json

def add_translation_to_json_file(english_phrase, spanish_translation, json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    data[english_phrase] = spanish_translation

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)