
import os
import streamlit as st
from manager import add_translation_to_json_file

json_file_name = 'sentences.JSON'
json_file_path = os.path.abspath(json_file_name)

st.write("Aplicación de Streamlit para almacenar texto")
text_input_ing = st.text_area("Escribe tu párrafo aquí en ingles:")
text_input_spa = st.text_area("Escribe tu párrafo aquí en español:")

if st.button("Guardar"):
    add_translation_to_json_file(text_input_ing, text_input_spa, json_file_path)

