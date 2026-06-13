# python -m venv venv - cria o ambiente virtual
# venv/scripts/activate - ativa o ambiente virtual
# pip install supabase
# pip install python-dotenv
# criar o arquivo requirements.txt
# pip freeze > requirements.txt - salva as dependências do projeto no arquivo requirements.txt
# criar o arquivo .env
# criar o arquivo .gitignore -> venv e .env
# executar o fastapi com uvicorn
  #uvicorn aula14:app --reload

import os
from dotenv import load_dotenv
from supabase import create_client #
from fastapi import FastAPI
import requests


load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url,supabase_key) 

app= FastAPI()

# selecao=input('Digite o produto que deseja buscar')
# produtos=requests.get(f'https://fakestoreapi.com/products/{selecao}').json()
# print(produtos)
# print(produtos['image'])

#crie um programa em python que solicite o cep do usuário e utilize a API do viacep para buscara cidade, estado e nome da rua

# cep=input('Digite seu cep:')
# endereco=requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()

# print(f'Endereço: {endereco['logradouro']}\nCidade: {endereco['localidade']}\nEstado: {endereco['estado']}')

@app.get('/livros')
def get_livros():
    resposta = supabase.table('biblioteca_livro').select("*").execute()
    livros = resposta.data
    return livros

@app.get('/livros/{id}')
def get_livros_id(id:int):
    print(id)
    return{'mensagem':f'Id escolhido: {id}'}
    resposta = supabase.table('biblioteca_livro').select("*").eq('id',id).execute()

    livros = resposta.data

    if len(livros) == 0:
        return {'Mensagem: Livro não encontrado'}

    return livros

#1.pegar os dados de todos os usúario
@app.get('/usuarios')
def get_usuarios():
    resposta = supabase.table('biblioteca_usuario').select('*').execute()
    usuarios = resposta.data
    return usuarios

#2.pegar os dados de um usúario pelo seu cpf

#3.pegar todos os livros de um autor