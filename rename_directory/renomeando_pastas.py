import os
from lista_de_musicas import *

# import shutil

caminho_diretorio = r"C:\Users\drili\Downloads\Pop"  # substitua por seu caminho de diretório

for artista in lista_artista_pop:
    os.makedirs(os.path.join(caminho_diretorio, artista), exist_ok=True)
