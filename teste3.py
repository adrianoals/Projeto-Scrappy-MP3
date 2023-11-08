from funnction import *
import json

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

# Navegando até a página do genero Rock
driver.get('https://player.kovver.app/genres/3/artists')

sleep(1)

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

# Converta a string JSON em um objeto JSON
obj_json = json.loads(script)
print(obj_json)
print()
print(type(script))

# antes de fehar a automacao
input('digite algo para fechar... ')
