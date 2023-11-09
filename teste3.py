from funnction import *
import json
from mongodb import *

connection_string = 'mongodb://admin:password@localhost:27017/?authSource=ad'
db_name = 'VS_Musics'

client = MongoClient(connection_string)
db_connection = client[db_name]
collection = db_connection['json_musicas']

# Iniciando o driver
driver = iniciar_driver()

# Navegando Site
navegar_site(driver)

# Pausa
sleep(3)

# Fazendo Login
login(driver)

# Pausa
sleep(1.5)

# Navegando até a página do genero Rock
driver.get('https://player.kovver.app/genres/3/artists')

sleep(1.2)

# Indo no artista
clicando_no_texto(driver, "3 Doors Down")

sleep(1)

# Clicando na música
clicando_no_texto(driver, 'Here Without You')

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

# Insere o dicionário na coleção
collection.insert_one(obj_json)

# antes de fehar a automacao
input('digite algo para fechar... ')
