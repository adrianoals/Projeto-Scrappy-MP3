from funnction import *
from mongodb import *
import json


# Conectando ao banco de dados
db_connection = connect_to_db('mongodb://localhost:27017/', 'VS_Musics')

# Iniciando o driver
driver = iniciar_driver()

# Navegando Site
navegar_site(driver)

# Pausa
sleep(5)

# Fazendo Login
login(driver)

# Pausa
sleep(2)

# Entrando no webPlayer
clicando_webplayer(driver)

# Pausa
sleep(3)

# Clicando no rock
clicando_no_texto(driver, "Rock")

# Adicionando Pausa
sleep(1.4)


for artista in lista_artista:
    # Entrando no artista
    clicando_no_texto(driver, artista)

    # Adicionando Pausa
    sleep(1)

    # Verificaando a quantidade de músicas do artista
    # Localizando todos os elementos com a classe "item-title"
    elementos_item_title = driver.find_elements(By.CSS_SELECTOR, '.item-title')
    # Criando uma lista para armazenar os títulos das músicas
    titulos_das_musicas = []

    # Percorrendo cada elemento e adicionando o título da música
    for elemento in elementos_item_title:
        titulos_das_musicas.append(elemento.text)    
        
    # Imprimindo as músicas
    print(titulos_das_musicas)
            
    # Percorrendo a lista de músicas e entrando nelas
    for musica in titulos_das_musicas:
        clicando_no_texto(driver, musica)
        sleep(2)
        # Obetendo o script da musica
        elemento_script = driver.find_element(By.XPATH, '//script[contains(text(), "openPlayer")]')
        # Obtenha o conteúdo interno do elemento <script>
        conteudo_script = elemento_script.get_attribute('innerHTML')
        # Imprima o conteúdo do script
        print(conteudo_script)

        # Adicionando pausa
        sleep(2.2)

        # Converte a string JSON em um objeto Python
        data = json.loads(conteudo_script)

        # Insere o objeto Python no MongoDB
        insert_one_document(db_connection,'VS_Musics', data)
        # result = collection.insert_one(data)

        # Retornando a página de músicas do artista
        # Localizando o botão pelo seletor de classe e clicando nele
        botao_voltar = driver.find_element(By.CSS_SELECTOR, "button.navbar-brand")
        botao_voltar.click()
        
        # Adicionando pausa
        sleep(2.1)

    # Retornando a página do artistas
    # Localizando o botão pelo seletor de classe e clicando nele
    botao_voltar = driver.find_element(By.CSS_SELECTOR, "button.navbar-brand")
    botao_voltar.click()
    sleep(1.5)


# antes de fehar a automacao
input('digite algo para fechar... ')