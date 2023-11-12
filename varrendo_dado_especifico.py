from database import *
from selenium_functions import *
from funnctions import *
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
clicando_no_texto(driver, "POP")

# Adicionando Pausa
sleep(1.4)

# Localizando todos os elementos com a classe "artist-thumb"
elementos_artist_thumb = driver.find_elements(By.CSS_SELECTOR, '.artist-thumb')
# Crie uma lista para armazenar os conteúdos do 'event_label'
event_labels = []
# Percorra cada elemento e obtenha o atributo 'onclick'
for elemento in elementos_artist_thumb:
    onclick = elemento.get_attribute('onclick')
    # Use a função split para extrair o conteúdo do 'event_label'
    inicio = onclick.find("'event_label' : '") + len("'event_label' : '")
    fim = onclick.find("'", inicio)
    event_label = onclick[inicio:fim]
    # Adicione o conteúdo do 'event_label' à lista
    event_labels.append(event_label)

# Imprima os conteúdos do 'event_label'
print(event_labels)

# for event_label in event_labels:
#     print(event_label)







# # Entrando no artista
# clicando_no_texto(driver, "Bon Jovi")

# sleep(1)

# # Clicando na música
# clicando_no_texto(driver, "You Give Love a Bad Name")

# # Localize o elemento <script>
# elemento_script = driver.find_element(By.XPATH, '//script[contains(text(), "openPlayer")]')

# # Obtenha o conteúdo interno do elemento <script>
# conteudo_script = elemento_script.get_attribute('innerHTML')
# print(conteudo_script)
# print()
# print(type(conteudo_script))
# print()

# script = json.dumps(conteudo_script)
# print(script)
# print()
# print(type(script))
# print()

# # Formatando Json
# # Remova os espaços em branco e "\n        openPlayer('" do início e ");\n    " do final
# script = script[1:-1]
# script = script.replace('\\' , '')
# script = script.strip().lstrip("\n        openPlayer('").rstrip("');\nn    ")
# print(script)
# print(type(script))

# # # Converta a string JSON em um objeto JSON
# print()
# obj_json = json.loads(script)
# print(obj_json)
# print()
# print(type(obj_json))

# # Inserindo no BD
# insert_one_document(db_connection=db_connection, collection_name='Musicas', data=obj_json)


# antes de fehar a automacao
input('digite algo para fechar... ')
