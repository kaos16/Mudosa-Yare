
import streamlit as st
import time
import webbrowser

# Configuración de la página
st.set_page_config(page_title="Para mi Mudosa 💖", page_icon="💘", layout="centered")

# Estilos personalizados
st.markdown("""
    <style>
    .titulo {
        font-size: 36px;
        text-align: center;
        color: #ff3366;
        font-weight: bold;
    }
    .corazon {
        text-align: center;
        font-size: 40px;
        animation: latido 1s infinite;
    }
    @keyframes latido {
        0% {transform: scale(1);}
        50% {transform: scale(1.2);}
        100% {transform: scale(1);}
    }
    .mensaje {
        background-color: #fff0f5;
        border-radius: 10px;
        padding: 20px;
        font-size: 18px;
        color: #333;
        margin-top: 20px;
    }
    .firma {
        margin-top: 40px;
        text-align: center;
        color: gray;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<div class='titulo'>💘 Para mi Mudosa 💘</div>", unsafe_allow_html=True)

# Corazón animado
st.markdown("<div class='corazon'>❤️ 💖 ❤️</div>", unsafe_allow_html=True)

# Botón para mostrar mensaje
if st.button("💌 Ver mensaje 💌"):
    with st.expander("💬 Mensaje de amor"):
        st.markdown("""
            <div class='mensaje'>
            Para ti, mi mudosa hermosa 💖<br><br>
            Desde el 5 de junio del 2023, cada día a tu lado es un regalo.<br>
            Tu risa, tus abrazos, tu forma de ver el mundo... todo me hace amarte más.<br>
            Gracias por existir y por elegirme. Nunca olvides lo mucho que te amo.
            </div>
        """, unsafe_allow_html=True)

# Botón para reproducir canción
if st.button("🎶 Escuchar 'Solo tú' de Luis Miguel 🎶"):
    st.markdown("[Haz clic aquí para escuchar la canción](https://www.youtube.com/watch?v=EZl6BRY9IYQ)")

# Firma final
st.markdown("<div class='firma'>Con todo mi amor, tu Emmanuel 🌹</div>", unsafe_allow_html=True)
