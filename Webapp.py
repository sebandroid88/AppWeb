import streamlit as st
from PIL import Image


st.title("DETODOTECNO - Agenda de Citas")
st.subheader("Tecnología - Servicios - Automatismo")
st.write("[Haz clic aquí para visitar Google](https://www.google.com)")
img = Image.open("imagen1.jpg")
st.image(img, use_column_width=True)

def main():
    st.title("Visor de Detección de Rostros en Tiempo Real")
    st.write("Usa la cámara para detectar rostros en tiempo real.")

    

    

if __name__ == "__main__":
    main()
