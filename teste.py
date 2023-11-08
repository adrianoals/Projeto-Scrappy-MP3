import json

# Sua string JSON
string_json = '{\"id\":1140,\"name\":\"Crazy\",\"artist\":{\"id\":37,\"name\":\"Aerosmith\"},\"duration\":\"05:34\",\"tracks\":[{\"id\":11995,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/312db2535de8a233e881153e6b8c0549.mp3\",\"name\":\"Backing Vocal\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":12010,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/984658dd14df20ccc8a7d78a55a1cc46.mp3\",\"name\":\"Bateria\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":11983,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/186a1584d6fd2597d9cd18bea24b6f10.mp3\",\"name\":\"Contrabaixo\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":11989,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/b2ffc052b46810e97401f9b03656ac35.mp3\",\"name\":\"Cordas\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":11980,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/c92c9f9ba58363ca9acf4d9723295f0e.mp3\",\"name\":\"Gaita\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":11998,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/375ee4a0a2526ad4689f83037401c47e.mp3\",\"name\":\"Guitarra Base\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":11986,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/af24536beff2f7150682475dbd1f53e5.mp3\",\"name\":\"Guitarra Solo\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":11992,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/a0b048a753ea054eb99f0e5acd2b4b3f.mp3\",\"name\":\"Percuss\\u00e3o\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":12001,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/cbcd0294e0397505ccf9f66abcbfbdee.mp3\",\"name\":\"Piano\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":12007,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/be04338cabe1a4dd95b16b04cb24ccf4.mp3\",\"name\":\"Viol\\u00e3o\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},{\"id\":12004,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/21163ed4d157ef3ecdc9816fef260be8.mp3\",\"name\":\"Vocal\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1}],\"metronome\":{\"id\":12013,\"path\":\"https:\\/\\/storage.googleapis.com\\/songs.kovverapp.com\\/aerosmith_crazy_14215-multi\\/e6d0611a73eb7a14f4d5943b25c4c67d.mp3\",\"name\":\"Metr\\u00f4nomo\",\"left\":false,\"right\":false,\"muted\":false,\"volume\":1},\"favorite\":false,\"pitch\":0,\"tone\":\"A\",\"rate\":1,\"info\":\"Fonte: Tency Music\\r\\nInt\\u00e9rprete: Tency Music\\r\\nCompositor: Desmond Child \\/ Joe Perry \\/ Steven Tyler\\r\\n\\u00c1lbum: Get a Grip\\r\\nData de lan\\u00e7amento: 1994\",\"lyric\":true,\"bought\":false}'

# Converta a string JSON em um dicionário
dicionario = json.loads(string_json)

# Imprima o dicionário
print(dicionario)
print()
print(type(dicionario))
print()

path = dicionario['tracks'][0]['path']
name = dicionario['tracks'][0]['name']
print(path, name)

print()
