from mongodb import *

connection_string = 'mongodb://localhost:27017/'
db_name = 'VS_Musics'

db_connection = connect_to_db(connection_string=connection_string, db_name=db_name)


collections = db_connection.list_collection_names()
print(f'Lista de collections: {collections}')


json = {'id': 1054, 'name': 'Here Without You', 'artist': {'id': 286, 'name': '3 Doors Down'}, 'duration': '04:03', 'tracks': [{'id': 10315, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/abca4e6dffa793513415465c8b0d2e43.mp3', 'name': 'Backing Vocal', 'left': False, 'right': False, 'muted': False, 'volume': 1}, {'id': 10327, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/30b2acf3e12f1d2f364d56e44a21f744.mp3', 'name': 'Bateria', 'left': False, 'right': False, 'muted': False, 'volume': 1}, {'id': 10306, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/1c1cef10582dd8e51a93115e1270cef7.mp3', 'name': 'Contrabaixo', 'left': False, 'right': False, 'muted': False, 'volume': 1}, {'id': 10312, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/d7ce49aa5d5f2836a14c36ce433e88b6.mp3', 'name': 'Cordas', 'left': False, 'right': False, 'muted': False, 'volume': 1}, {'id': 10318, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/08fd541aef3380bdb0f7736371681eea.mp3', 'name': 'Guitarra Base', 'left': False, 'right': False, 'muted': False, 'volume': 1}, {'id': 10309, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/5b081534b2ba07cb00b9d06962381969.mp3', 'name': 'Guitarra Solo', 'left': False, 'right': False, 'muted': False, 'volume': 1}, {'id': 10324, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/90b21c88a2f45300c8a09584e951ed47.mp3', 'name': 'Violu00e3o', 'left': False, 'right': False, 'muted': False, 'volume': 1}, {'id': 10321, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/88144013f0fb1c614d93d3b7e91e3159.mp3', 'name': 'Vocal', 'left': False, 'right': False, 'muted': False, 'volume': 1}], 'metronome': {'id': 10330, 'path': 'https://storage.googleapis.com/songs.kovverapp.com/3-doors-down_here-without-you_5740-multi/26b9a7fb000e57e751ece72901ae9c62.mp3', 'name': 'Metru00f4nomo', 'left': False, 'right': False, 'muted': False, 'volume': 1}, 'favorite': False, 'pitch': 0, 'tone': 'C#', 'rate': 1, 'info': 'Fonte: Tency MusicrnIntu00e9rprete: Tency MusicrnCompositor: Brad Arnold / Robert Harrell / Matt Roberts / Chris Hendersonrnu00c1lbum: The Better LifernData de lanu00e7amento: 2002', 'lyric': True, 'bought': False}

# insert_one_document(db_connection=db_connection, collection_name='Musicas', data=json)

documents = find_documents(db_connection=db_connection, collection_name='Musicas', query=None)
for document in documents:
    print(document)
    print()
    print(document['artist']['name'])
    print()
    print(document['name'])
    print()
    
    for name in document['tracks']:
        print(name['name'])
    
    print(document['metronome']['name'])

