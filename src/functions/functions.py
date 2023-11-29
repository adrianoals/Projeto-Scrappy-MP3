import os
import requests

def criar_diretorio(artista, musica):
    try:
        # Definindo caminho
        caminho_do_diretorio = r"C:\Users\drili\OneDrive\Área de Trabalho\Projeto Scrappy MP3\MP3"
        # caminho_do_diretorio = r"/Users/adriano/Desktop/Projeto-Scrappy-MP3/Projeto-Scrappy-MP3/MP3"
        # Definindo o nome da pasta 
        nome_da_pasta = f"{artista} - {musica}"
        # Combinando o caminho do diretório com o nome da pasta
        caminho_completo = os.path.join(caminho_do_diretorio, nome_da_pasta)
         # Método makedirs() para criar a pasta
        os.makedirs(caminho_completo, exist_ok=True)
        print(f"Pasta '{nome_da_pasta}' criada com sucesso em '{caminho_do_diretorio}'")
        return caminho_completo
    except Exception as e:
        print(f"Não foi possível criar a pasta. Erro: {str(e)}")


def download_arquivos(link_download, caminho, nome_arquivo):
    try:
        # Fazendo uma requisição GET para a URL
        resposta = requests.get(link_download)
        # Verificando se a requisição foi bem sucedida
        resposta.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Erro de Conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print ("Erro:", err)
    else:
        try:
            with open(os.path.join(caminho, nome_arquivo), 'wb') as arquivo:
                arquivo.write(resposta.content)
                print('Arquivo baixado com sucesso')
        except Exception as e:
            print("Não foi possível salvar o arquivo:", e)
