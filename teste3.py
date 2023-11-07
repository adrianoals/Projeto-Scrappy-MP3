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

# Navegando até a página do genero Rock
driver.get('https://player.kovver.app/genres/3/artists')

sleep(1)


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
    
    # Adicionando Pausa
    sleep(1)
    
    # Retornando a página de artistas
    # Localizando o botão pelo seletor de classe e clicando nele
    botao_voltar = driver.find_element(By.CSS_SELECTOR, "button.navbar-brand")
    botao_voltar.click()

    # Adicionando Pausa
    sleep(1)
    
    input('deseja continuar? ')
