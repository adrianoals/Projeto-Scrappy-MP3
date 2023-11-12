from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import requests

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


# Navegando até o site
def navegar_site(driver):
    driver.get('https://player.kovver.app/account/login/email')


# Localize os campos de entrada e insira o texto
def login(driver):
    campo_email = driver.find_element(By.ID, 'email')
    campo_senha = driver.find_element(By.ID, 'password')
    campo_email.send_keys('adrianotesteapp@gmail.com')
    campo_senha.send_keys('Testeapp@') 
    # Localize o botão de login e clique nele
    botao_login = driver.find_element(By.ID, 'email-do')
    botao_login.click()
    return print('Login efetuado')


# Localizando o web player e clicando nele
def clicando_webplayer(driver):
    link_player_web = driver.find_element(By.XPATH, '//a[contains(text(), "Player Web")]')
    link_player_web.click()
    print('Link clicado')


def clicando_no_texto(driver, texto):
    try: 
        elemento_texto = driver.find_element(By.XPATH, f'//div[contains(text(), "{texto}")]')
        elemento_texto.click()
        print(f'Click no elemento que contém {texto}')
    except:
        print()
        print(f'Elemento com texto "{texto}" não encontrado.')
        print()


def clicando_no_texto2(driver, texto):
    try:
        elemento_texto = driver.find_element(By.XPATH, f'//div[@class="item-title" and text()="{texto}"]')
        elemento_texto.click()
        print(f'Click no elemento que contém {texto}')
    except:
        print()
        print(f'Elemento com texto "{texto}" não encontrado.')
        print()


lista_artista = ['Rock Noisy', 'Rod Stewart', 'Roxette', 'Roy Orbison', 'Rush', 'Santana', 'School of Rock', 'Scorpions', 'Shadowplay', 'Shawn Mendes', 'Simple Minds', 'Skillet', 'Slipknot', 'Spacecruiser', 'Steppenwolf', 'Steve Vai', 'Stone Sour', 'Supertramp', 'Survivor', 'System Of A Down', 'Tearful Regret', 'Tenacious D', 'The Animals', 'The Beatles', 'The Cosmic Surfer', 'The Cure', 'The Doors', 'The Freejacks', 'The Killers', 'The Nucleus Winter', 'The Offspring', 'The Police', 'The Rolling Stones', 'The White Stripes', 'The Who', 'Tina Turner', 'Toto', 'Treadplate', 'U2', 'Ultraje a Rigor', 'Uns e Outros', 'Van Halen', 'Velvet Revolver', 'Vivendo do Ócio', 'Whitesnake', 'Wry', 'Yacht Sunset', 'YMA', 'Zero Time Ghosts']


def criar_diretorio(artista, musica):
    try:
        # Definindo caminho
        caminho_do_diretorio = r"C:\Users\drili\OneDrive\Área de Trabalho\Projeto Scrappy MP3\MP3"
        # Definindo o nome da pasta 
        nome_da_pasta = f"{artista} - {musica}"
        # Combinando o caminho do diretório com o nome da pasta
        caminho_completo = os.path.join(caminho_do_diretorio, nome_da_pasta)
         # Método makedirs() para criar a pasta
        os.makedirs(caminho_completo, exist_ok=True)
        print(f"Pasta '{nome_da_pasta}' criada com sucesso em '{caminho_do_diretorio}'")
        return caminho_completo
    except Exception as e:
        print(f"Não foi possível criar a pasta. Erro: {str(e)}")


def download_arquivos(link_download, caminho, nome_arquivo):
    try:
        # Fazendo uma requisição GET para a URL
        resposta = requests.get(link_download)
        # Verificando se a requisição foi bem sucedida
        resposta.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Erro de Conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print ("Erro:", err)
    else:
        try:
            with open(os.path.join(caminho, nome_arquivo), 'wb') as arquivo:
                arquivo.write(resposta.content)
                print('Arquivo baixado com sucesso')
        except Exception as e:
            print("Não foi possível salvar o arquivo:", e)


# # Fazendo uma requisição GET para a URL
# resposta = requests.get(link_download)
# with open(os.path.join(caminho, nome_arquivo), 'wb') as arquivo:
#     arquivo.write(resposta.content)
#     print('Arquivo baixado com sucesso')



# # Localizando todos os elementos com a classe "artist-thumb"
# elementos_artist_thumb = driver.find_elements(By.CSS_SELECTOR, '.artist-thumb')
# # Crie uma lista para armazenar os conteúdos do 'event_label'
# event_labels = []
# # Percorra cada elemento e obtenha o atributo 'onclick'
# for elemento in elementos_artist_thumb:
#     onclick = elemento.get_attribute('onclick')
#     # Use a função split para extrair o conteúdo do 'event_label'
#     inicio = onclick.find("'event_label' : '") + len("'event_label' : '")
#     fim = onclick.find("'", inicio)
#     event_label = onclick[inicio:fim]
#     # Adicione o conteúdo do 'event_label' à lista
#     event_labels.append(event_label)

# # Imprima os conteúdos do 'event_label'
# print(event_labels)

# # for event_label in event_labels:
# #     print(event_label)


# lista_artista = ['3 Doors Down', '4 Non Blondes', 'AC/DC', 'Aerosmith', 'Al Jarreau', 'Alanis Morissette', 'Alice in Chains', 'Andy Dreamy Day', 'Andy Williams', 'Angra', 'Arctic Monkeys', 'Audioslave', 'Avenged Sevenfold', 'Beyond Cyberia', 'Billy Joel', 'Biquíni Cavadão', 'Black Sabbath', 'Blink-182', 'Bon Jovi', 'Brainless Wonders', 'Brittney', 'Bruce Springsteen', 'Bryan Adams', 'Buckcherry', 'Bud Elkin & Company', 'Canto das Gerais', 'Chaos Disorder', 'Charcot Marie', 'Chuck & Patty', 'Chuck Berry', 'Corey Landis', 'Cream', 'Creed', 'Creedence Clearwater Revival', 'Dark Jester', 'David Bowie', 'Dé Repetto & William Possato', 'Deep Purple', 'Dire Straits', 'Dream Theater', 'Dust To Dust', 'Eagles', 'Elbert Torphy', 'Elton John', 'Elvis Presley', 'Eric Clapton', 'Europe', 'Eviltwins', 'Extreme', 'Fabiano Manhas', 'Faith No More', 'Fall Out Boy', 'Fireflight', 'Fleetwood Mac', 'Flywire', 'Foo Fighters', 'Foreigner', 'Genesis', 'Goo Goo Dolls', 'Gorillaz', 'Green Day', 'Greta Van Fleet', 'Guns N', 'Guy Campo', 'Heart', 'High Wire Dive', 'Huey Lewis & The News', 'Imagine Dragons', 'Improved', 'Inn Sample', 'IRA', 'Iron Maiden', 'Isabella', 'James Blunt', 'Janis Joplin', 'Jason Aaron Wood', 'Jezebel', 'Jim Willoughby', 'Jimi Hendrix', 'Joan Jett', 'Joan Osborne', 'Joe Cocker', 'John Daly', 'John Lennon', 'John Mayer', 'John Mellencamp', 'Josey Wells', 'Journey', 'Kansas', 'Kiss', 'Konfront the Khaos', 'Korn', 'Krisiun', 'Led Zeppelin', 'Limp Bizkit', 'Linkin Park', 'Little Drop Joe', 'Low Embryonic Cells', 'Lynyrd Skynyrd', 'Marilyn Manson', 'Maurício Alabama', 'Megadeth', 'Men at Work', 'Metallica', 'Metallstein Rock', 'Motley Crue', 'Motörhead', 'Muse', 'My Chemical Romance', 'Nann Farias', 'Napalmbats', 'Nirvana', 'Oasis', 'Ol Sonuf', 'Ozzy Osbourne', 'Pantera', 'Paramore', 'Patsy Cline', 'Paul McCartney', 'Pearl Jam', 'Pedram Mojtabavi', 'Peep Show Junkies', 'Peter Frampton', 'Peter Gabriel', 'Phil Collins', 'Pink Floyd', 'Poison', 'Poperia', 'Prince', 'Queen', 'Queens of the Stone Age', 'R.E.M.', 'Radiohead', 'Rage Against the Machine', 'Rai Starr', 'Raimundos', 'Ramones', 'Red Hot Chili Peppers', 'Ritchie Valens', 'Rock Feelings Podcast', 'Rock Noisy', 'Rod Stewart', 'Roxette', 'Roy Orbison', 'Rush', 'Santana', 'School of Rock', 'Scorpions', 'Shadowplay', 'Shawn Mendes', 'Simple Minds', 'Skillet', 'Slipknot', 'Spacecruiser', 'Steppenwolf', 'Steve Vai', 'Stone Sour', 'Supertramp', 'Survivor', 'System Of A Down', 'Tearful Regret', 'Tenacious D', 'The Animals', 'The Beatles', 'The Cosmic Surfer', 'The Cure', 'The Doors', 'The Freejacks', 'The Killers', 'The Nucleus Winter', 'The Offspring', 'The Police', 'The Rolling Stones', 'The White Stripes', 'The Who', 'Tina Turner', 'Toto', 'Treadplate', 'U2', 'Ultraje a Rigor', 'Uns e Outros', 'Van Halen', 'Velvet Revolver', 'Vivendo do Ócio', 'Whitesnake', 'Wry', 'Yacht Sunset', 'YMA', 'Zero Time Ghosts']