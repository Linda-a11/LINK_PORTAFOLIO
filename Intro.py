import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portafolio Programación Avanzada",
    page_icon="🤖",
    layout="wide"
)

# Estilos visuales
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .main-description {
        text-align: center;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 8px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 12px;
        padding: 12px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">Aplicaciones de Inteligencia Artificial</div>',
    unsafe_allow_html=True
)

# Barra lateral
with st.sidebar:
    st.subheader("Portafolio Programación Avanzada")

    parrafo = (
        "Bienvenido a mi portafolio, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )

    st.write(parrafo)

    st.divider()

    st.write("Portafolio de aplicaciones y ejercicios prácticos.")

# Enlace principal
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown(
    '<div class="section-title">Páginas y ejercicios prácticos</div>',
    unsafe_allow_html=True
)

st.write(
    f"En el siguiente enlace puedes encontrar páginas y ejercicios prácticos: "
    f"[Abrir portafolio]({url_ia})"
)

st.divider()

# Información de las aplicaciones
aplicaciones = [
    {
        "titulo": "Frutas",
        "imagen": "frutas.png",
        "descripcion": "Explora una experiencia interactiva donde la Inteligencia Artificial se encuentra con el mundo de las frutas.",
        "url": "https://frutas-nokzmkbrymex7jhrfgw77f.streamlit.app/",
        "accion": "🍎 Explorar"
    },
    {
        "titulo": "Descenso de Gradiente Interactivo",
        "imagen": "graint.jpg",
        "descripcion": "Descubre cómo un algoritmo encuentra el camino hacia la mejor solución, paso a paso.",
        "url": "https://appgradier-i2fhmkpa8y3j99syx5wfyq.streamlit.app/",
        "accion": "📉 Experimentar"
    },
    {
        "titulo": "Datos: preparación y estructura",
        "imagen": "estruc.jpg",
        "descripcion": "Antes de que los datos hablen, hay que ponerlos en orden. Aquí comienza el proceso.",
        "url": "https://trabajo1-r8qbrczcyr83agvurfalyx.streamlit.app/",
        "accion": "🧩 Explorar"
    },
    {
        "titulo": "Serie de tiempo",
        "imagen": "Time.jpg",
        "descripcion": "Viaja a través de los datos y descubre patrones que cambian con el tiempo.",
        "url": "https://serietiempo-dc6vybtpsopreu4qcjxrxx.streamlit.app/",
        "accion": "⏳ Explorar"
    },
    {
        "titulo": "Regresión",
        "imagen": "regre.jpg",
        "descripcion": "Convierte datos en relaciones y deja que los modelos encuentren la tendencia.",
        "url": "https://regresion1-xcpdmqqzdwd9fy5tchiidx.streamlit.app/",
        "accion": "📊 Experimentar"
    },
    {
        "titulo": "Regresión Logística interactiva",
        "imagen": "logist.jpg",
        "descripcion": "Una mirada interactiva a cómo los datos pueden ayudarnos a tomar decisiones de clasificación.",
        "url": "https://nwcf9mkmqmmj4pmvuythtv.streamlit.app/",
        "accion": "🎯 Explorar"
    },
    {
        "titulo": "Predictor de Sensación Térmica",
        "imagen": "termi2.jpg",
        "descripcion": "¿Qué tan caliente o frío se sentirá? Deja que los datos hagan la predicción.",
        "url": "https://prediccionsensacion-gslxba8faz7jkqhq6tb3aa.streamlit.app/",
        "accion": "🌡️ Probar"
    },
    {
        "titulo": "Limpieza de datos",
        "imagen": "clean.jpg",
        "descripcion": "Datos más limpios, modelos más confiables. Dale a tus datos una buena puesta a punto.",
        "url": "https://limpiezadatos-2jnxnjxdullblqwnjgxsy5.streamlit.app/",
        "accion": "🧹 Explorar"
    },
    {
        "titulo": "Sistema Ciberfísico",
        "imagen": "OIG6.jpg",
        "descripcion": "Cuando los datos salen de la pantalla y comienzan a interactuar con el mundo real.",
        "url": "https://vision2-gpt4o.streamlit.app/",
        "accion": "🤖 Descubrir"
    },
    {
        "titulo": "Explora KNN con datos de suelos de AGROSAVIA",
        "imagen": "agrosa.jpg",
        "descripcion": "Explora cómo los vecinos más cercanos pueden revelar patrones en los datos de fertilidad del suelo.",
        "url": "https://clasificaci-n-de-fertilidad-de-suelos-dzagvqtnqdel93wobengpl.streamlit.app/",
        "accion": "🌱 Explorar"
    },
    {
        "titulo": "Detector de Anomalías: Lógica + Big-O + NumPy",
        "imagen": "big.jpg",
        "descripcion": "Encuentra lo que se sale de lo normal y descubre cómo la lógica y el código trabajan juntos.",
        "url": "https://juegoprogramacionavanzada-ebpvypkht2pa4vmbsqlurv.streamlit.app/",
        "accion": "🔎 Detectar"
    },
    {
        "titulo": "Fundamentos de computacion paralela",
        "imagen": "lelo.jpg",
        "descripcion": "uso simultáneo de varios procesadores para resolver problemas con mayor velocidad y eficiencia.",
        "url": "https://programacionorientadao-uugwot68kq3rdnjmb3xynw.streamlit.app/",
        "accion": "🔎 Detectar"
    }
]

# Presentación organizada en tres columnas
for inicio in range(0, len(aplicaciones), 3):
    columnas = st.columns(3, gap="medium")

    for posicion in range(3):
        indice = inicio + posicion

        if indice < len(aplicaciones):
            aplicacion = aplicaciones[indice]

            with columnas[posicion]:
                with st.container(border=True):
                    st.subheader(aplicacion["titulo"])

                    try:
                        imagen = Image.open(aplicacion["imagen"])
                        st.image(imagen, use_container_width=True)
                    except FileNotFoundError:
                        st.warning(
                            f"No se encontró la imagen: {aplicacion['imagen']}"
                        )

                    st.write(aplicacion["descripcion"])

                    st.link_button(
                        aplicacion["accion"],
                        aplicacion["url"],
                        use_container_width=True
                    )

st.divider()

st.caption("Portafolio de Programación Avanzada")
