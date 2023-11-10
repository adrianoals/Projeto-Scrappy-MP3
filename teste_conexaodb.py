from database_config import *
import requests
import os
from funnction import *

connection_string = 'mongodb://localhost:27017/'
db_name = 'VS_Musics'

db_connection = connect_to_db(connection_string=connection_string, db_name=db_name)

collections = db_connection.list_collection_names()
print(f'Lista de collections: {collections}')

documents = find_documents(db_connection=db_connection, collection_name='Musicas', query=None)
for document in documents:
    print(document)
    print()
    nome_artista = document['artist']['name']
    nome_musica = document['name']
    # Criando diretorio
    caminho = criar_diretorio(nome_artista, nome_musica)

    # Salvando arquivos
    for name in document['tracks']:
        nome = name['name']
        nome_arquivo = nome + '.mp3'
        link_download = name['path']
        # Fazendo uma requisição GET para a URL
        resposta = requests.get(link_download)
        with open(os.path.join(caminho, nome_arquivo), 'wb') as arquivo:
            arquivo.write(resposta.content)
            print('Arquivo baixado com sucesso')
    
    # Salvando arquivo de metronomo

    # print(document['metronome']['name'])



