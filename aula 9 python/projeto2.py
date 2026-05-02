import streamlit as st

st.title('Cadastro de Usuário')

nome = st.text_input('Nome')

idade= st.text_input('Idade')

cidade= st.text_input('Cidade')

email= st.text_input('Digite seu email')

senha= st.text_input('Digite uma senha')

# if st.button ('Cadastrar'):
#     append