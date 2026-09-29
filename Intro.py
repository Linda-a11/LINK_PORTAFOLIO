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

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Frutas")
    image = Image.open('frutas.png')
    st.image(image, width=190)
    st.write("Explora una experiencia interactiva donde la Inteligencia Artificial se encuentra con el mundo de las frutas.")
    url = "https://frutas-nokzmkbrymex7jhrfgw77f.streamlit.app/"
    st.write(f"🍎 Explorar: [Enlace]({url})")

    st.subheader("Descenso de Gradiente Interactivo")
    image = Image.open('graint.jpg')
    st.image(image, width=200)
    st.write("Descubre cómo un algoritmo encuentra el camino hacia la mejor solución, paso a paso.")
    url = "https://appgradier-i2fhmkpa8y3j99syx5wfyq.streamlit.app/"
    st.write(f"📉 Experimentar: [Enlace]({url})")

    st.subheader("Datos: preparación y estructura")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("Antes de que los datos hablen, hay que ponerlos en orden. Aquí comienza el proceso.")
    url = "https://trabajo1-r8qbrczcyr83agvurfalyx.streamlit.app/"
    st.write(f"🧩 Explorar: [Enlace]({url})")


with col2:
    st.subheader("Serie de tiempo")
    image = Image.open('Time.jpg')
    st.image(image, width=200)
    st.write("Viaja a través de los datos y descubre patrones que cambian con el tiempo.")
    url = "https://serietiempo-dc6vybtpsopreu4qcjxrxx.streamlit.app/"
    st.write(f"⏳ Explorar: [Enlace]({url})")

    st.subheader("Regresión")
    image = Image.open('regre.jpg')
    st.image(image, width=190)
    st.write("Convierte datos en relaciones y deja que los modelos encuentren la tendencia.")
    url = "https://regresion1-xcpdmqqzdwd9fy5tchiidx.streamlit.app/"
    st.write(f"📊 Experimentar: [Enlace]({url})")

    st.subheader("Regresión Logística interactiva")
    image = Image.open('logist.jpg')
    st.image(image, width=200)
    st.write("Una mirada interactiva a cómo los datos pueden ayudarnos a tomar decisiones de clasificación.")
    url = "https://nwcf9mkmqmmj4pmvuythtv.streamlit.app/"
    st.write(f"🎯 Explorar: [Enlace]({url})")


with col3:
    st.subheader("Predictor de Sensación Térmica")
    image = Image.open('termi2.jpg')
    st.image(image, width=190)
    st.write("¿Qué tan caliente o frío se sentirá? Deja que los datos hagan la predicción.")
    url = "https://prediccionsensacion-gslxba8faz7jkqhq6tb3aa.streamlit.app/"
    st.write(f"🌡️ Probar: [Enlace]({url})")

    st.subheader("Limpieza de datos")
    image = Image.open('clean.jpg')
    st.image(image, width=200)
    st.write("Datos más limpios, modelos más confiables. Dale a tus datos una buena puesta a punto.")
    url = "https://limpiezadatos-2jnxnjxdullblqwnjgxsy5.streamlit.app/"
    st.write(f"🧹 Explorar: [Enlace]({url})")

    st.subheader("Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Cuando los datos salen de la pantalla y comienzan a interactuar con el mundo real.")
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"🤖 Descubrir: [Enlace]({url})")

    st.subheader("Explora KNN con datos de suelos de AGROSAVIA")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Explora cómo los vecinos más cercanos pueden revelar patrones en los datos de fertilidad del suelo.")
    url = "https://clasificaci-n-de-fertilidad-de-suelos-dzagvqtnqdel93wobengpl.streamlit.app/"
    st.write(f"🌱 Explorar: [Enlace]({url})")

    st.subheader("Detector de Anomalías: Lógica + Big-O + NumPy")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Encuentra lo que se sale de lo normal y descubre cómo la lógica y el código trabajan juntos.")
    url = "https://juegoprogramacionavanzada-ebpvypkht2pa4vmbsqlurv.streamlit.app/"
    st.write(f"🔎 Detectar: [Enlace]({url})")
