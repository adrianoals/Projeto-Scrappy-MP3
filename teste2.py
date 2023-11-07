import requests

# URL do arquivo
url = 'https://storage.googleapis.com/songs.kovverapp.com/aerosmith_crazy_14215-multi/984658dd14df20ccc8a7d78a55a1cc46.mp3'

# Faça uma requisição GET para a URL
resposta = requests.get(url)

# Abra o arquivo em modo de escrita binária e escreva o conteúdo da resposta
with open('bateria.mp3', 'wb') as arquivo:
    arquivo.write(resposta.content)

print('Arquivo baixado com sucesso')
