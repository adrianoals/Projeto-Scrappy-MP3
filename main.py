from funnction import *
from database_config import *
import json
from time import sleep
from random import uniform

# Conectando ao banco de dados
db_connection = connect_to_db('mongodb://localhost:27017/', 'VS_Musics')

# Iniciando o driver
driver = iniciar_driver()

# Navegando Site
navegar_site(driver)

# Pausa
pausa_aleatoria = uniform(2, 4)
sleep(pausa_aleatoria)

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
    sleep(pausa_aleatoria)

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
    print()
            
    # Percorrendo a lista de músicas e entrando nelas
    for musica in titulos_das_musicas:
        sleep(pausa_aleatoria)

        clicando_no_texto2(driver, musica)
        
        sleep(5)
        # Obetendo o script da musica
        try: 
            elemento_script = driver.find_element(By.XPATH, '//script[contains(text(), "openPlayer")]')
            # Obtenha o conteúdo interno do elemento <script>
            conteudo_script = elemento_script.get_attribute('innerHTML')
    
            # Adicionando pausa
            sleep(pausa_aleatoria)

            script = json.dumps(conteudo_script)

            # Formatando Json
            script = script[1:-1]
            script = script.replace('\\' , '')
            script = script.strip().lstrip("\n        openPlayer('").rstrip("');\nn    ")

            # # Converta a string JSON em um objeto JSON
            obj_json = json.loads(script)
            print(obj_json)
            
            insert_one_document(db_connection=db_connection, collection_name='Musicas', data=obj_json)
            print()

        except:
            print()
            print(f'Nao foi possível pegar o script da música {musica} do {artista}')
            print()
        
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
    sleep(pausa_aleatoria)


# antes de fehar a automacao
input('digite algo para fechar... ')