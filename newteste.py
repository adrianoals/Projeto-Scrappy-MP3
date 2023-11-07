from funnction import *

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

sleep(1.4)

'''
for artista in lista_artista:
    clicando_no_texto(driver, artista)
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
    # Obtém a URL atual
    url_atual = driver.current_url
    print("URL atual:", url_atual)

    for musica in titulos:

'''












# Clicando no rock
clicando_no_texto(driver, "Guns N")





# antes de fehar a automacao
input('digite algo para fechar... ')