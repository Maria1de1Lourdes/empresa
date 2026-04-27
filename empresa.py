import streamlit as st
st.image(
    "gucci.png",
    caption="Clique para esplorar a página da GUCCI.",
    link="https://www.gucci.com/int/en/st/brazil-landing",
    width=750
)
st.write("Maria de Lourdes de Freitas Almeida")
st.image("Foto.jpg")
st.write("Tenho mestrado em Design e em administração, fui contratada pela Gucci após uma entrevista acirrada.")

st.image(
    "whatsapp.png",
    caption="Clique para nos contatar via Whatsapp.",
    link="https://w.app/gucci",
    width=680
)
st.image("QRcode.png")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2E3135;
    }
    </style>
    """,
    unsafe_allow_html=True
)
