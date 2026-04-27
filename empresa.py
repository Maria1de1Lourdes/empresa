import streamlit as st
st.image(
    "gucci.png",
    caption="Clique para esplorar a página da GUCCI.",
    link="https://www.gucci.com/int/en/st/brazil-landing",
    width=750
)
<br>
st.write("Maria de Lourdes de Freitas Almeida")
<br>
st.image(
        "Foto.jpg",
         width=320
        )
<br>
st.write("Tenho mestrado em Design e em administração, fui contratada pela Gucci após uma entrevista acirrada.")
<br>

st.image(
    "whatsapp.png",
    caption="Clique para nos contatar via Whatsapp.",
    link="https://w.app/gucci",
    width=400
)
st.image(
    "QRcode.png",
    width=400
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2E3135;
        text-color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)
