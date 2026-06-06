import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase_url= os.getenv('SUPABASE_URL')
supabase_key= os.getenv('SUPABASE_KEY')

supabase=create_client(supabase_url,supabase_key)

#tabela autor: id, criado em, nome (text), gênero textual(text), nacionalidade | 1 pra muitos
#tabela livro: id, criado em, título, quant. de livros (int), gênero, ano(int), id do autor (int)
#tabela usuarios: id, criado em, nome, cpf, telefone(text), endereço, ativo (bolean) (true/false)
#tabela perfil: id, criado em, foto(text), bio, preferencias, id_usuario(int) | 1 pra 1
#tabela emprestimos: id, criado em, data de devolução, data de entrega, id_livro, id_usuario 

def inserirUsuario():
    nome = input('Digite o nome')
    cpf = input('Digite o cpf')
    telefone = input('Digite o telefone')
    endereco = input('Digite o endereço')

    novoUsuario = {
        'nome':nome,
        'cpf':cpf,
        'telefone':telefone,
        'endereco':endereco
    }
    resposta = supabase.table('biblioteca_usuario').insert(novoUsuario).execute()

    print(resposta)

#inserirUsuario()

def inserirPerfil():
    foto= input('Coloque o link da foto:')
    bio = input('Coloque uma bio:')
    preferencia = input('Coloque suas preferencias:')
    id_usuario = input('Inserir id de usuario')

    novoPerfil = {
        'foto':foto,
        'bio':bio,
        'preferencia':preferencia,
        'id_usuario':id_usuario
    }
    resposta = supabase.table('biblioteca_perfil').insert(novoPerfil).execute()

    print(resposta)

#inserirPerfil() 

def inserirDadosTabelas(tabela,dados):
    try:
        resposta = supabase.table(tabela).insert(dados).execute()
        print('Dados inseridos com sucesso')
    except Exception as erro:
        print(f'Erro ao inserir os dados: {erro}')

def atualizarDados(tabela,id,dados):
    try:
        resposta = supabase.table(tabela).update(dados).eq('id',id).execute()
        print('Dados atualizados com sucesso')
    except Exception as erro:
        print(f'Erro ao atualizar os dados: {erro}')

tabela='biblioteca_autor'
atualizacaoAutor = {
    'nome':'Clarice Lispector',
    'genero_literario':'Romance',
    'id':'1'
}


def coletarDadosInserir():
    opcao = input('Selecione uma opção:\n1-Inserir Usuario\n2-Inserir Perfil\n3-Inserir Autor\n4-Inserir livro\n5-Inserir Empréstimo\n')
    if opcao == '1':
        tabela = 'biblioteca usuarios'
        nome = input('Digite o nome')
        cpf = input('Digite o cpf')
        telefone = input('Digite o telefone')
        endereco = input('Digite o endereço')
        novoUsuario = {
            'nome':nome,
            'cpf':cpf,
            'telefone':telefone,
            'endereco':endereco
        }
        inserirDadosTabelas(tabela,novoUsuario)
    if opcao =='2':
        foto= input('Coloque o link da foto:')
        bio = input('Coloque uma bio:')
        preferencia = input('Coloque suas preferencias:')
        id_usuario = input('Inserir id de usuario')
        novoPerfil = {
            'foto':foto,
            'bio':bio,
            'preferencia':preferencia,
            'id_usuario':id_usuario
        }
        inserirDadosTabelas(tabela,novoPerfil)
    if opcao =='3':
        nome_autor= input('Coloque o nome do autor:')
        genero_literario= input('Coloque o genero literario:')
        nacionalidade = input('Coloque a nacionalidade do autor:')
        novoAutor = {
            'nome_autor':nome_autor,
            'genero_literario':genero_literario,
            'nacionalidade':nacionalidade
        }
        inserirDadosTabelas(tabela,novoAutor)
    if opcao =='4':
        titulo= input('Coloque o titulo do livro:')
        quantidade= input('Coloque a quantidade de livros:')
        genero = input('Coloque o genero:')
        id_autor = input('Coloque o id do autor:')
        novoLivro = {
            'titulo':titulo,
            'quantidade':quantidade,
            'genero':genero,
            'id_autor':id_autor
        }
        inserirDadosTabelas(tabela,novoLivro)
    if opcao =='5':
        data_devolucao= input('Coloque a data de devolução:')
        data_entrega= input('Coloque a data de entrega:')
        id_livro = input('Coloque o id do livro:')
        id_usuario = input('Coloque o id de usuario')
        novoEmprestimo = {
            'data_devolucao':data_devolucao,
            'data_entrega':data_entrega,
            'id_livro':id_livro,
            'id_usuario':id_usuario
        }
        inserirDadosTabelas(tabela,novoEmprestimo)
        
def coletarDadosAtuais():
    print('Qual tabela você quer atualizar?')
    tabelas={
        '1':'biblioteca_usuarios',
        '2':'biblioteca_perfil',
        '3':'biblioteca_autor',
        '4':'biblioteca_livro',
        '5':'biblioteca_emprestimo'
    }

    camposTabela={
        'biblioteca_usuarios':['nome','cpf','endereco','ativo'],
        'biblioteca_perfil':['foto','bio','preferencias'],
        'biblioteca_autor':['nome','genero','nacionalidade'],
        'biblioteca_livro':["titulo","quantidade","genero","ano"],
        "emprestimo":["data_devolucao"]
    }

    for chave, valor in tabelas.items():
        print(f'{chave}-`{valor}')
    opcao = input('Digite a opção desejada:')
    tabelaSelecionada = tabelas[opcao]
    resposta = supabase.table(tabelaSelecionada).select('*').execute()
    print('Selecione o ID que você quer atualizar')
    for resposta in resposta.data:
        print('///////////////////////////////')
    for chave, valor in resposta.items():
        print(f'{chave} - {valor}')
    id = input('Digite o ID que você quer atualizar:')

resposta = supabase.table(tabelaSelecionada).select('*').eq('id',id).execute()

atualizarDados()

#coletarDadosInserir()

#código tá bem incompleto, algum dia eu ajeito