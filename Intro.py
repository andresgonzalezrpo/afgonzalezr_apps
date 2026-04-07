import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# --- Fila 1 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Detección de Objetos en Imágenes")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("En el siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial.")
    url = "https://chatpdf-vn2w6tkq8dcozfbyzriogf.streamlit.app/"
    st.write(f"Texto a voz: [Enlace]({url})")

with col2:
    st.subheader("Análisis de frecuencia léxica y visualización de nubes de palabras")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos como se detectan objetos en Imágenes.")
    url = "https://convoluciones-cdin7ufd3ncc9dxzmlbtma.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url})")

with col3:
    st.subheader("Análisis de Imagen")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos como puedes usar tu modelo entrenado.")
    url = "https://r8m7h4jobeam9eyurvitrc.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url})")

# --- Fila 2 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("TRADUCTOR")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("En el siguiente veremos una aplicación que usa la conversión de voz a texto.")
    url = "https://traductorstt.streamlit.app/"
    st.write(f"Voz a texto: [Enlace]({url})")

with col2:
    st.subheader("Reconocimiento de Imágenes")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos como se pueden analizar datos usando agentes.")
    url = "https://convoluciones-jpb7tkyxjhzz6hhqrbw75l.streamlit.app/"
    st.write(f"Datos: [Enlace]({url})")

with col3:
    st.subheader("Clasificador de Flores")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos como realizamos transcripciones de audio/video.")
    url = "https://convoluciones-caj3bvakhkg9jzx9k49trr.streamlit.app/"
    st.write(f"Transcriptor: [Enlace]({url})")

# --- Fila 3 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Análisis de Sentimientos")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En el siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).")
    url = "https://convoluciones-5qcgmqmtqtbtmzan9d89ol.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

with col2:
    st.subheader("Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de análisis en Imágenes.")
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

with col3:
    st.subheader("Predicción de Secuencias Temporales")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de interacción con el mundo físico.")
    url = "https://convoluciones-2tofnpnjnkjbtwfctr3h74.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

# --- Fila 4 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Predicción de Secuencias Temporales")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En el siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).")
    url = "https://convoluciones-6dquggq2faoaxquhnpapne.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

with col2:
    st.subheader("Predicción de Consumo Eléctrico con LSTM")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de análisis en Imágenes.")
    url = "https://pred55554332.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

with col3:
    st.subheader("Reconocimiento Óptico de Caracteres")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de interacción con el mundo físico.")
    url = "https://chatpdf-4clusqdmn7wcnthmyyzmmr.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

# --- Fila 5 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("OCR Avanzado")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En el siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).")
    url = "https://lttfezxibcvfavukrdbdut.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

with col2:
    st.subheader("Detección de Dígitos Escritos a Mano")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de análisis en Imágenes.")
    url = "https://andresgonzalezrpoappio-b7zpcy7jvdt2vqoekyhi5r.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

with col3:
    st.subheader("Generador de Texto LSTMs")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de interacción con el mundo físico.")
    url = "https://convoluciones-j4zjyapt5spkfbnbqqu93g.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

# --- Fila 6 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Conversión de Texto a Audio")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En el siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).")
    url = "https://convoluciones-cqqgbnixf3zmwapihnxyxi.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

with col2:
    st.subheader("Convoluciones Visualizadas")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de análisis en Imágenes.")
    url = "https://convoluciones-v8gfjsu5cwptaepcldc5hu.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

with col3:
    st.subheader("Chat GPT propio")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de interacción con el mundo físico.")
    url = "https://kxrdms7saguynjxs9g5ast.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

# --- Fila 7 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Análisis sobre PDF")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En el siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).")
    url = "https://chatpdf-hyuzukqskqkhoh8ngztked.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

with col2:
    st.subheader("Explorar y generar dígitos")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos la capacidad de análisis en Imágenes.")
    url = "https://a4d2leeinvy5bbitllkmb9.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")
