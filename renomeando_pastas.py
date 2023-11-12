import os
# import shutil


lista_artista_rock_nacional = ['Barão Vermelho', 'Canto dos Malditos na Terra do Nunca', 'Capital Inicial', 'Cássia Eller', 'Cazuza', 'Charlie Brown Jr.', 'Engenheiros do Hawaii', 'Frejat', 'Jota Quest', 'Kid Abelha', 'Legião Urbana', 'Lobão', 'Los Hermanos', 'Lulu Santos', 'Mundo Livre S/A', 'Nando Reis', 'O Rappa', 'Paralamas do Sucesso', 'Raul Seixas', 'Roupa Nova', 'Skank', 'Titãs']

caminho_diretorio = r"C:\Users\drili\Downloads\Rock Nacional"  # substitua por seu caminho de diretório

for artista in lista_artista_rock_nacional:
    os.makedirs(os.path.join(caminho_diretorio, artista), exist_ok=True)





# # Caminho para a pasta 'músicas'
# music_folder_path = r'C:\Users\drili\OneDrive\Área de Trabalho\Scrapy Tab\MP3'

# # Lista todas as pastas na pasta 'músicas'
# folders = os.listdir(music_folder_path)

# for folder in folders:
#     # Divide o nome da pasta em 'artista' e 'música'
#     artist, song = folder.split(' - ')

#     # Caminho para a nova pasta do artista
#     artist_folder_path = os.path.join(music_folder_path, artist)

#     # Cria uma nova pasta para o artista, se ainda não existir
#     os.makedirs(artist_folder_path, exist_ok=True)

#     # Caminho para a pasta da música atual
#     song_folder_path = os.path.join(music_folder_path, folder)

#     # Caminho para a nova localização da pasta da música
#     new_song_folder_path = os.path.join(artist_folder_path, folder)

#     # Move a pasta da música para a pasta do artista
#     shutil.move(song_folder_path, new_song_folder_path)