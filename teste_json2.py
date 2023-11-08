json = "{\"id\":1027,\"name\":\"When I\'m Gone\",\"artist\":{\"id\":286,\"name\":\"3 Doors Down\"},\"duration\":\"04:19\",\"tracks\":[{\"id\":10072,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/e3be43f32cb6909cc35715eddf72b382.mp3\",\"name\":\"Backing Vocal\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":10084,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/e6ac2a1266a9ff3521dafe8724bc58be.mp3\",\"name\":\"Bateria\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":10063,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/a455c7e686fb59c8156ba70e4bba95c1.mp3\",\"name\":\"Contrabaixo\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":10075,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/7656f9b66f1c21175ae5f6a0b0d3a6f0.mp3\",\"name\":\"Guitarra Base\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":10066,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/0f561e79be156c41725ce8e25d085c8c.mp3\",\"name\":\"Guitarra Solo\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":10069,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/4c13030cb2bed97e3586c63ca3cbf3d7.mp3\",\"name\":\"Percuss\\u00e3o\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":10081,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/c21ca94baab44ab81433db91276b6511.mp3\",\"name\":\"Viol\\u00e3o\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":10078,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/d1332d80ee82a6d01dffdfa626bfc605.mp3\",\"name\":\"Vocal\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1}],\"metronome\":{\"id\":10087,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/3-doors-down_when-i-m-gone_7196-multi\\/d47ea235748a965c9c9ff61311508b0d.mp3\",\"name\":\"Metr\\u00f4nomo\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},\"favorite\":false,\"pitch\":0,\"tone\":\"Am\",\"rate\":1,\"info\":\"Fonte: Tency Music\\r\\nInt\\u00e9rprete: Tency Music\\r\\nCompositor: Chris Henderson \\/ Brad Arnold \\/ Matt Roberts \\/ Todd Harrell\\r\\n\\u00c1lbum: The Better Life\\r\\nData de lan\\u00e7amento: 2000\",\"lyric\":true,\"bought\":false}"

# # Sua string
# s = 'openPlayer(...)'  # substitua por sua string real


# Encontre o índice inicial do JSON
inicio_json = json.find('{')

# Encontre o índice final do JSON
fim_json = json.rfind('}') + 1

# Extraia a parte JSON da string
json_str = json[inicio_json:fim_json]

# Converta a string JSON em um objeto JSON
obj_json = json.loads(json_str)

print(obj_json)