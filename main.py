from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import json

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1024,730', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

# Iniciando o driver
driver = iniciar_driver()
# Navegando até o site
driver.get('https://player.kovver.app/account/login/email')

# Adicione uma espera para garantir que a página tenha tempo para carregar
sleep(3)

# Localize os campos de entrada e insira o texto
campo_email = driver.find_element(By.ID, 'email')
campo_senha = driver.find_element(By.ID, 'password')
campo_email.send_keys('adrianotesteapp@gmail.com')
campo_senha.send_keys('Testeapp@') 
# Localize o botão de login e clique nele
botao_login = driver.find_element(By.ID, 'email-do')
botao_login.click()
print('Login efetuado')

# inserindo pausa
sleep(3)

# Localizando o web player e clicando nele
link_player_web = driver.find_element(By.XPATH, '//a[contains(text(), "Player Web")]')
link_player_web.click()
print('Link clicado')

# Pausa
sleep(2)

# Localizando o elemento com o texto "Rock" e clicando nele
elemento_rock = driver.find_element(By.XPATH, '//div[contains(text(), "Rock")]')
# Clique no elemento
elemento_rock.click()
print('Botão "Rock" clicado')

# Pausa
sleep(2)


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

# Pausa
sleep(1)

# Entrando no artista e baixando a música
# Localize o elemento com o texto "Aerosmith"
elemento_aerosmith = driver.find_element(By.XPATH, '//div[contains(text(), "Aerosmith")]')

# Clique no elemento
elemento_aerosmith.click()
print('Botão "Aerosmith" clicado')

sleep(0.9)

# Verificaando a quantidade de músicas do artista
# Localize todos os elementos com a classe "item-title"
elementos_item_title = driver.find_elements(By.CSS_SELECTOR, '.item-title')

# Crie uma lista para armazenar os textos
titulos = []
# Percorra cada elemento e adicione o texto à lista
for elemento in elementos_item_title:
    titulos.append(elemento.text)
# Imprima os textos
print(titulos)


# for titulo in titulos:
#     print(titulo)


sleep(1)

# Entrando dentro da música Crazy
elemento_musica = driver.find_element(By.XPATH, '//div[contains(text(), "Crazy")]')

# Clique no elemento
elemento_musica.click()
print('Botão "Crazy" clicado')

print('')

sleep(5)

# # Obtenha o código-fonte da página
# codigo_fonte = driver.page_source
# # Imprima o código-fonte
# print(codigo_fonte)

print('')

# Localize o elemento <script>
elemento_script = driver.find_element(By.XPATH, '//script[contains(text(), "openPlayer")]')

# Obtenha o conteúdo interno do elemento <script>
conteudo_script = elemento_script.get_attribute('innerHTML')

# Imprima o conteúdo do script
print(conteudo_script)
print(type(conteudo_script))

data = json.loads(conteudo_script)
print()
print(type(data))
print(data)


# antes de fehar a automacao
input('digite algo para fechar... ')
