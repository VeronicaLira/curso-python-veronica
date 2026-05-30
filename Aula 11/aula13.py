import os
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

supabase_url= os.getenv('SUPABASE_URL')
supabase_key= os.getenv('SUPABASE_KEY')

supabase=create_client(supabase_url,supabase_key)

# resposta = (supabase.table('itens_pedidos')
#             .select('nome, pedidos(id, valor, usuarios(nome))')
#             .execute())

# print(resposta.data)

resposta=supabase.table('matricula').select('alunos(nome),curso(nome)').eq('id_aluno',4).execute()
# print(resposta.data)

for resp in resposta.data:
    print(f'{resp['alunos']['nome']} : {resp['curso']['nome']}')