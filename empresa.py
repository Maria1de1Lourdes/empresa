import streamlit as st
st.image(
    "gucci.png",
    caption="Acesse a Página da GUCCI por aqui",
    width=750
)
st.write("Maria de Lourdes de Freitas Almeida")
st.image(
        "Foto.jpg",
         width=320
        )
st.write("Tenho mestrado em Design e em administração, fui contratada pela Gucci após uma entrevista acirrada. Atualmente faço parte na modelagem dos sites.")

st.image(
    "whatsapp.png",
    caption="Acesse o whattsapp oficial da GUCCI por aqui",
    width=400
)
st.image(
    "QRcode.png",
    width=400
)
st.button("acesse aqui")
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
