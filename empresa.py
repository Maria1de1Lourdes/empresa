import streamlit as st

import base64
st.set_page_config(page_title="Perfil da Gucci", layout="wide")
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
img_base64 = get_base64_image("gucci.png")
zap_base64 = get_base64_image("whatsapp.png")
img2_base64=get_base64_image("QRcode.png")
 
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="https://starlink.com/" target="_blank">
                <img src="data:image/png;base64,{img_base64}"
                     width="320"
                     style="border-radius:12px;">
            </a>
        </div>
    """, unsafe_allow_html=True)
col_left, col_right = st.columns([3,1])
with col_left:
    st.markdown("""
    <div style='margin-bottom:30px; font-size:30px;'>
        <b>Nome: Maria de Lourdes de Freitas Almeida </b>
    </div>
    """, unsafe_allow_html=True)
    subcol1, subcol2 = st.columns([1,4])
    with subcol1:
        st.markdown("""
        <div style="
            display: flex;
            align-items: center;
            height: 100%;
        ">
        """, unsafe_allow_html=True)
        st.image("Foto.jpg", width=800)
        st.markdown("</div>", unsafe_allow_html=True)
    with subcol2:
        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 20px;
            line-height: 2.0;
            width: 100%;
            max-width: none;
        ">
            <b>Sobre Maria:<br>
           Maria de Lourdes de Freitas Almeida é uma  participante do curso profissionalizante de informática, sendo uma das pioneiras desse curso no instituto IFPB de Itabaiana.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<div style='margin-top:30px;'>", unsafe_allow_html=True)
    st.link_button("Acessar","https://www.gucci.com/int/en/st/brazil-landing")
    st.markdown("</div>", unsafe_allow_html=True)
with col_right:
    st.empty()
    st.markdown(f"""
    <div style="text-align: center; margin-top: 10px;">
        <a href="link="https://w.app/gucci" target="_blank">
            <img src="data:image/png;base64,{zap_base64}" width="100">
        </a>
    </div>
     """, unsafe_allow_html=True)
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
                <img src="data:image/png;base64,{img2_base64}"
                     width="320"
                     style="border-radius:12px;">
        </div>
     """, unsafe_allow_html=True)

    

