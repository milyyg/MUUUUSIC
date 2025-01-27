import streamlit as st
import random

# Lista de canciones (puedes agregar más)
canciones = [
    {"titulo": "Bohemian Rhapsody", "artista": "Queen", "genero": "Rock"},
    {"titulo": "Shape of You", "artista": "Ed Sheeran", "genero": "Pop"},
    {"titulo": "Billie Jean", "artista": "Michael Jackson", "genero": "Pop"},
    {"titulo": "Stairway to Heaven", "artista": "Led Zeppelin", "genero": "Rock"},
    {"titulo": "Blinding Lights", "artista": "The Weeknd", "genero": "Pop"},
    {"titulo": "Imagine", "artista": "John Lennon", "genero": "Rock"},
    {"titulo": "Rolling in the Deep", "artista": "Adele", "genero": "Soul"},
    {"titulo": "Uptown Funk", "artista": "Mark Ronson ft. Bruno Mars", "genero": "Funk"}
]

# Título de la aplicación
st.title("Generador de Música Aleatoria")

# Instrucciones
st.write("""
Haz clic en el botón para descubrir una canción aleatoria. 
Cada vez que presiones el botón, verás el título, el artista y el género de la canción aleatoria que te sugiero.
""")

# Botón para generar una canción aleatoria
if st.button('Generar Canción'):
    cancion = random.choice(canciones)
    st.write(f"🎶 **Título:** {cancion['titulo']}")
    st.write(f"🎤 **Artista:** {cancion['artista']}")
    st.write(f"🎼 **Género:** {cancion['genero']}")
