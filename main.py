import streamlit as st
from PIL import Image

# <a href="https://br.freepik.com/vetores-gratis/texto-neon-de-clinica-e-dente-brilhante-com-coroa_4550664.htm#query
# =dentist%20logo&position=12&from_view=search&track=robertav1_2_sidr">Imagem de katemangostar</a> no Freepik

st.image(Image.open('imagens/logo.jpg'))
st.title('Agenda Consultório 📆')

st.subheader('📍 Selecionar data')

st.date_input('data', label_visibility="hidden")

st.subheader('Agenda do dia 📑')
st.text_area('Agenda', label_visibility="hidden", height=350)

st.button('Salvar')

