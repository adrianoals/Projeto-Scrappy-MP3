import os

# Strings raw: Adicione um r antes da string para torná-la uma string raw, que ignora caracteres de escape:

# # Defina o caminho completo do diretório onde você quer criar a pasta
# caminho_do_diretorio = r"C:\Users\drili\OneDrive\Área de Trabalho\Projeto Scrappy MP3\MP3"

artista = 'Acdc'
musica = 'Highway to Hell'
# # Defina o nome da pasta que você quer criar
# nome_da_pasta = f"{artista} - {musica}"

# # Combine o caminho do diretório com o nome da pasta
# caminho_completo = os.path.join(caminho_do_diretorio, nome_da_pasta)

# # Use o método makedirs() para criar a pasta
# os.makedirs(caminho_completo, exist_ok=True)


caminho_do_diretorio = r"C:\Users\drili\OneDrive\Área de Trabalho\Projeto Scrappy MP3\MP3"
caminho = caminho_do_diretorio + '\\' + artista + ' - ' + musica
print(caminho)



