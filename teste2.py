import json
from pprint import pprint

json_teste = "\n        openPlayer('{\\\"id\\\":1054,\\\"name\\\":\\\"Here Without You\\\",\\\"artist\\\":{\\\"id\\\":286,\\\"name\\\":\\\"3 Doors Down\\\"},\\\"duration\\\":\\\"04:03\\\",\\\"tracks\\\":[{\\\"id\\\":10315,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/abca4e6dffa793513415465c8b0d2e43.mp3\\\",\\\"name\\\":\\\"Backing Vocal\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1},{\\\"id\\\":10327,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/30b2acf3e12f1d2f364d56e44a21f744.mp3\\\",\\\"name\\\":\\\"Bateria\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1},{\\\"id\\\":10306,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/1c1cef10582dd8e51a93115e1270cef7.mp3\\\",\\\"name\\\":\\\"Contrabaixo\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1},{\\\"id\\\":10312,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/d7ce49aa5d5f2836a14c36ce433e88b6.mp3\\\",\\\"name\\\":\\\"Cordas\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1},{\\\"id\\\":10318,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/08fd541aef3380bdb0f7736371681eea.mp3\\\",\\\"name\\\":\\\"Guitarra Base\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1},{\\\"id\\\":10309,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/5b081534b2ba07cb00b9d06962381969.mp3\\\",\\\"name\\\":\\\"Guitarra Solo\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1},{\\\"id\\\":10324,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/90b21c88a2f45300c8a09584e951ed47.mp3\\\",\\\"name\\\":\\\"Viol\\\\u00e3o\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1},{\\\"id\\\":10321,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/88144013f0fb1c614d93d3b7e91e3159.mp3\\\",\\\"name\\\":\\\"Vocal\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1}],\\\"metronome\\\":{\\\"id\\\":10330,\\\"path\\\":\\\"https:\\\\/\\\\/storage.googleapis.com\\\\/songs.kovverapp.com\\\\/3-doors-down_here-without-you_5740-multi\\\\/26b9a7fb000e57e751ece72901ae9c62.mp3\\\",\\\"name\\\":\\\"Metr\\\\u00f4nomo\\\",\\\"left\\\":false,\\\"right\\\":false,\\\"muted\\\":false,\\\"volume\\\":1},\\\"favorite\\\":false,\\\"pitch\\\":0,\\\"tone\\\":\\\"C#\\\",\\\"rate\\\":1,\\\"info\\\":\\\"Fonte: Tency Music\\\\r\\\\nInt\\\\u00e9rprete: Tency Music\\\\r\\\\nCompositor: Brad Arnold \\\\/ Robert Harrell \\\\/ Matt Roberts \\\\/ Chris Henderson\\\\r\\\\n\\\\u00c1lbum: The Better Life\\\\r\\\\nData de lan\\\\u00e7amento: 2002\\\",\\\"lyric\\\":true,\\\"bought\\\":false}');\n    "

# Remova os espaços em branco e "\n        openPlayer('" do início e ");\n    " do final
json_teste = json_teste.strip().lstrip("\n        openPlayer('").rstrip("');\n    ")

print()
print(json_teste)
print(type(json_teste))

# print()
# json_teste2 = json_teste.replace('\\\\/' , '')
# print(json_teste)

# Agora você pode carregar o conteúdo como JSON
dados = json.dumps(json_teste)
print()
print(dados)
print()
print(type(dados))

print()
json_teste2 = dados.replace('\\' , '')
print(json_teste2)
print(type(json_teste2))
print()
json_teste2 = json_teste2[1:-1]
print(json_teste2)
print(type(json_teste2))
print()

dados2 =json.loads(json_teste2)
print(dados2)
print()
print(type(dados2))


print(dados2['artist']['name'])
print(dados2['name'])
print(dados2['tracks'])
print(dados2['tracks'][0]['path'])
print(dados2['tracks'][0]['name'])




