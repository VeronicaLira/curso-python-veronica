import streamlit as st
import pyqrcode as qr
import pyttsx3

st.title('Gerador de qrcode')

#1. entrada de dados
nome = st.text_input('Qual o seu nome?')
telefone = st.text_input('Digite o seu telefone')
mensagem = st.text_area('Digite a mensagem')

if st.button ('Enviar'):
    link = f'https://api.whatsapp.com/send/?phone=55{telefone}&text={mensagem}&type=phone_number&app_absent=0'

    qrcode = qr.create(link)
    qrcode.png('qrcode_aula.png',scale=3)

    st.image('qrcode_aula.png')
    st.write('QRCode gerado com sucesso')
    

    st.write(link)

