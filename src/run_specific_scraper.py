from database.database import *
from functions.selenium_functions import *
from functions.functions import *
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


artista = 'Bon Jovi'
musica = "Always"


# Entrando no artista
clicando_no_texto(driver, artista)

sleep(1)

# Clicando na música  
clicando_no_texto(driver, musica)

# Localize o elemento <script>
elemento_script = driver.find_element(By.XPATH, '//script[contains(text(), "openPlayer")]')

# Obtenha o conteúdo interno do elemento <script>
conteudo_script = elemento_script.get_attribute('innerHTML')
print(conteudo_script)
print()
print(type(conteudo_script))
print()

script = json.dumps(conteudo_script)
print(script)
print()
print(type(script))
print()

# Formatando Json
# Remova os espaços em branco e "\n        openPlayer('" do início e ");\n    " do final
script = script[1:-1]
script = script.replace('\\' , '')
script = script.strip().lstrip("\n        openPlayer('").rstrip("');\nn    ")
print(script)
print(type(script))

# # Converta a string JSON em um objeto JSON
print()
obj_json = json.loads(script)
print(obj_json)
print()
print(type(obj_json))

# Inserindo no BD
insert_one_document(db_connection=db_connection, collection_name='Musicas Testes', data=obj_json, musica=musica)

# antes de fehar a automacao
input('digite algo para fechar... ')
