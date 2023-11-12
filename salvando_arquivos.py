from database import *
from funnctions import *

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

        download_arquivos(link_download=link_download, caminho=caminho, nome_arquivo=nome_arquivo)

    # Salvando arquivo de metronomo
    try:
        link_metronome = document['metronome']['path']
        download_arquivos(link_download=link_metronome, caminho=caminho, nome_arquivo='Metronomo.mp3')
    except KeyError as e:
        print("Chave não encontrada no documento:", e)
    except Exception as e:
        print("Erro ao baixar e salvar o arquivo:", e)
    





