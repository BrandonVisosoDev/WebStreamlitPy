
#Librerias Necesarias

import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd
import plotly.express as px


# Funcion De Animacion con metodo get

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Cargamos la variable animacion de LottieFiles

lottie_coding = load_lottieurl("https://lottie.host/4889d067-05fc-4d8b-af3c-efd2b7e6f091/EyPLz3IrMR.json")

# Cargamos unas variables de imagenes

image_pink1 = Image.open("img/IMG1.jpg")
image_pink2 = Image.open("img/IMG2.jpg")
image_pink3 = Image.open("img/IMG3.jpg")
image_pink4 = Image.open("img/IMG4.jpg")

# variable de video


video_path = "vd/vd.mp4"

# Primer contenedor encabezado

with st.container():
    st.subheader("La Revolución del K-Pop  ") #Subtitulo
    #Ponemos un video
    
    st.video(video_path, format="video/mp4", start_time=0)
    
    st.title("BlackPink En Tu Area :purple_heart: ") # Titulo
    st.write("Bienvenidos a la experiencia definitiva de BLACKPINK, el fenómeno global que ha revolucionado el mundo del K-Pop. Con su estilo único y su música contagiosa, Jisoo, Jennie, Rosé y Lisa han conquistado los corazones de millones y han roto barreras en la industria musical. En esta página, celebramos su talento, su moda icónica y su impacto cultural. Únete a nosotros en este viaje vibrante y descubre por qué BLACKPINK no es solo un grupo musical, sino un movimiento que inspira a una generación.")
    st.write("[A VR Encore - Official Trailer>](https://www.youtube.com/watch?v=qfTIbCXH68A)") # Sirve como texto y hipervinculo
    
# Segundo contenedor pero con dos secciones

with st.container():
    st.write("---")
    
    left_column , right_colum = st.columns(2) 
    
    with left_column:
        st.header("Acerca de  BlackPink")
        st.write("""Blackpink, también conocido como BLΛƆKPIИK o BLACKPINK, es un grupo femenino surcoreano formado por la empresa YG Entertainment en Seúl, Corea del Sur, el 8 de agosto de 2016. 
                 El grupo está compuesto por Jisoo, Jennie, Rosé y Lisa. Desde su debut, Blackpink ha dejado una huella significativa en la escena musical.""")
        st.write("[Su primer video - Debut Blackpink>](https://www.youtube.com/watch?v=bwmSjveL3Lc)")
    
    with right_colum:
        st_lottie(lottie_coding, height= 300, key="coding") # Mostramos la animacion

# integrantes    
with st.container():
    st.write("---")
    st.header("Acerca de sus integrantes")
    imagen_column, text_column = st.columns((1,2))
    with imagen_column:
        st.image(image_pink1)
    with text_column:
        st.write(
            """
            Jennie (Kim Jennie):
                Nombre en coreano (hangul): 김제니
                Edad: 27 años
                Cumpleaños: 16 de enero
                Aportación:
                Cantante, rapera, modelo y bailarina.
                Debutó con BLACKPINK en 2016 bajo la discográfica YG Entertainment.
                Fue la primera integrante en lanzar un sencillo en solitario, titulado “SOLO”.
                En 2023, lanzó su segundo sencillo, “You & Me”.
                Participó en la serie de HBO “The Idol” junto a The Weeknd y Lily Rose Depp.
                Tiene créditos de letrista en el tema “Lovesick Girls” del último disco “The Album”.
                Habla fluido coreano, japonés e inglés.
                Adora la comida coreana y tiene dos perritos llamados Kai y Kuma1
            
            """
        )
        
with st.container():
    st.write("---")
    imagen_column, text_column = st.columns((1,2))
    with imagen_column:
        st.image(image_pink2)
    with text_column:
        st.write(
            """
            Jisoo (Kim Ji-soo):
                Nombre en coreano (hangul): 김지수
                Edad: 27 años
                Cumpleaños: 3 de enero
                Aportación:
                Vocalista principal y visual del grupo.
                Actriz y modelo.
                Participó en la serie de televisión “Arthdal Chronicles”.
                Habla coreano e inglés.
                Amante de la moda y la fotografía
            
            """
        )
        
with st.container():
    st.write("---")
    imagen_column, text_column = st.columns((1,2))
    with imagen_column:
        st.image(image_pink3)
    with text_column:
        st.write(
            """
            Rosé (Park Chae-young):
                Nombre en coreano (hangul): 박채영
                Edad: 25 años
                Cumpleaños: 11 de febrero
                Aportación:
                Vocalista principal y guitarrista.
                Lanzó su sencillo en solitario “On The Ground” en 2021.
                abla coreano, inglés y japonés.
                Su voz distintiva y estilo único la han convertido en una favorita de los fans
            
            """
        )

with st.container():
    st.write("---")
    imagen_column, text_column = st.columns((1,2))
    with imagen_column:
        st.image(image_pink4)
    with text_column:
        st.write(
            """
            Lisa (Lalisa Manoban):
                Nombre en coreano (hangul): 리사
                Edad: 25 años
                Cumpleaños: 27 de marzo
                Aportación:
                Rapera principal y bailarina.
                De origen tailandés y habla tailandés, coreano, inglés y japonés.
                Es conocida por su habilidad en el baile y su carisma en el escenario.
                Participó en el programa de competencia de baile “Youth With You” en China.
                Su estilo de moda y su presencia en redes sociales la han convertido en una influencia global
            
            """
        )
        
with st.container():
    st.write("---")
    st.header("Canciones mas Escuchadas")
    
# Cargamos Datos

archivo_csv = "DATA.csv" 
df = pd.read_csv(archivo_csv)

# Mostramos datos en tabla

st.dataframe(df)

# Crear un gráfico de barras con Plotly Express

fig = px.bar(df, x="Canción", y="Reproducciones (millones)", title="Reproducciones de Canciones de BLACKPINK", color_discrete_sequence=['pink'])
st.plotly_chart(fig)