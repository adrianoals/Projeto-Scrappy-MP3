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
        sleep(1)
        # Obetendo o script da musica
        elemento_script = driver.find_element(By.XPATH, '//script[contains(text(), "openPlayer")]')
        # Obtenha o conteúdo interno do elemento <script>
        conteudo_script = elemento_script.get_attribute('innerHTML')
        # Imprima o conteúdo do script
        print(conteudo_script)

        # Adicionando pausa
        sleep(1.2)

        # Retornando a página de músicas do artista
        # Localizando o botão pelo seletor de classe e clicando nele
        botao_voltar = driver.find_element(By.CSS_SELECTOR, "button.navbar-brand")
        botao_voltar.click()

    # Retornando a página do artistas
    # Localizando o botão pelo seletor de classe e clicando nele
    botao_voltar = driver.find_element(By.CSS_SELECTOR, "button.navbar-brand")
    botao_voltar.click()
    sleep(0.3)


# antes de fehar a automacao
input('digite algo para fechar... ')