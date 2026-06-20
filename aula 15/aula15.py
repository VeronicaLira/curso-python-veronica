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
    #return{'mensagem':f'Id escolhido: {id}'}
    resposta = supabase.table('biblioteca_livro').select("*").eq('id',id).execute()
    

#     livros = resposta.data

#     if len(livros) == 0:
#         return {'Mensagem: Livro não encontrado'}

#     return livros

# @app.get('livros/{id}/{ano}')
#     def get_livros_id_ano(id: int, ano: int):
#     return {
#         "id":id,
#         "ano":ano
#     }

@app.get('/busca')
def busca(titulo:str=None, quantidade: int=None, genero:str=None, ano: int=None):
    resposta = supabase.table('biblioteca_livro').select('*')

    if titulo:
        resposta = resposta.ilike('titulo', f'%{titulo}%')

    if quantidade:
        resposta = resposta.eq('quantidade', quantidade)

    if genero:
        resposta = resposta.ilike('genero', f'%{genero}%')

    if ano:
        resposta = resposta.eq('ano', ano)

    resposta = resposta.execute()

    livros = resposta.data
    if len(livros) == 0:
        return{'Mensagem: Livro não enocntrado'}
    
    return livros

#http://127.0.0.1:8000/busca?

from fastapi import Body

@app.post('/livros')
def cadastrar_livro(dados: dict = Body()):
    resposta=supabase.table('biblioteca_livro').insert(dados).execute()

    resposta=resposta.data
    return resposta

###
@app.get('/autores')
def get_autores():
    resposta = supabase.table('biblioteca_autor').select("*").execute()
    livros = resposta.data
    return livros

@app.post('/autores')
def cadastrar_autor(dados: dict=Body()):
    resposta=supabase.table('biblioteca_autor').insert(dados).execute()
    resposta=resposta.data
    return resposta

#cadastrar usuário, perfil, empréstimo

#delete

@app.delete('/deletarlivro/{id}')
def deletarLivro(id: int=None):
    resposta=supabase.table('biblioteca_livro').delete().eq('id',id).execute()

    return {
        "msg":"Livro deletado com sucesso",
        "reposta":resposta.data
    }

#atualizar
@app.put("/atualizarlivro/{id}")
def atualizarlivro(id:int,dados:dict = Body()):
    resposta=supabase.table('biblioteca_livro').update(dados).eq('id',id).execute()

    return{
        "msg":"Livro atualizado com sucesso",
        "dados":resposta.data
    }

