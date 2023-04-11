import json

def add_translation_to_json_file(english_phrase: str, spanish_translation: str, json_file_path: str) -> None:
    """
    Agrega una nueva entrada al archivo JSON ubicado en json_file_path.

    Parámetros
    ----------
    english_phrase : str
        La frase en inglés que se quiere agregar al archivo JSON.
    spanish_translation : str
        La traducción de la frase en español que se quiere agregar al archivo JSON.
    json_file_path : str
        La ruta absoluta del archivo JSON donde se quiere agregar la nueva entrada.

    Retorno
    -------
    None
    """

    # Abrir el archivo JSON en modo lectura y cargar su contenido en la variable 'data'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Agregar la nueva entrada al diccionario 'data'
    data[english_phrase] = spanish_translation

    # Sobrescribir el archivo JSON con el nuevo contenido
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)
