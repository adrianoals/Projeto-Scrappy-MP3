from pymongo import MongoClient
from pprint import pprint


def connect_to_db(connection_string, db_name):
    client = MongoClient(connection_string)
    db_connection = client[db_name]
    return db_connection

# connection_string = 'mongodb://admin:password@localhost:27017/?authSource=ad'
# db_name = 'VS_Musics'

def list_collections(db_connection):
    collections = db_connection.list_collection_names()
    return collections

def find_documents(db_connection, collection_name, query=None):
    if query is None:
        query = {}
    result = db_connection[collection_name].find(query)
    return result

def find_one_document(db_connection, collection_name, query):
    document = db_connection[collection_name].find_one(query)
    return document

def insert_one_document(db_connection, collection_name, data):
    inserted_document = db_connection[collection_name].insert_one(data)
    return inserted_document

def insert_many_documents(db_connection, collection_name, data):
    inserted_documents = db_connection[collection_name].insert_many(data)
    return inserted_documents

def delete_one_document(db_connection, collection_name, filter):
    db_connection[collection_name].delete_one(filter)

def delete_many_documents(db_connection, collection_name, filter):
    db_connection[collection_name].delete_many(filter)

def update_one_document(db_connection, collection_name, filter, update_data):
    db_connection[collection_name].update_one(filter, update_data)

def update_many_documents(db_connection, collection_name, filter, update):
    db_connection[collection_name].update_many(filter, update)

def unset_key(db_connection, collection_name, filter, key):
    update = {"$unset": {key: ""}}
    db_connection[collection_name].update_many(filter, update)



'''
connection_string = 'mongodb://localhost:27017/'
client = MongoClient(connection_string)

# Selecionando um banco especifico
db_connection = client['VS_Musicas']
print(db_connection)

print()

# Listando as coleções no banco de dados
collections = db_connection.list_collection_names()
print(f'Lista de collections: {collections}')

print()

# 1. Read (Leitura):
# Recuperar todos os documentos de uma coleção
result = db_connection['emp'].find()

for document in result:
    pprint(document)

print('-'*70)

# Consulta por um documento específico
query = {"Cargo": "Analista"}
result = db_connection['emp'].find(query)

for document in result:
    print(document)

print('-'*70)

# Consultando por um documento específico usando find_one
# find_one retorna apenas um dado e nao retorna um cursor por isso não é necessário Iterar nele
document = db_connection['emp'].find_one({"Cargo": "Desenvolvedor"})
if document:
    print(document)
else:
    print("Nenhum documento encontrado.")

print('-'*70)



# # Create(Inserir documentos)

# # Dados para inserção (um novo documento)
# data = {
#     'Nome': 'Junior', 'Idade': 25, 'Cargo': 'Engenheiro', 'Renumeracao': 12100}

# # Insirindo um documento na coleção
# inserted_document = db_connection['emp'].insert_one(data)

# # Verificando o insert
# document = db_connection['emp'].find_one({"Cargo": "Engenheiro"})
# print(document)

# print('-'*70)

# # Dados para inserção (um novo documento)
# data = [ 
#     {'Nome': 'Ralf', 'Idade': 28, 'Cargo': 'Analista', 'Renumeracao': 12000},
#     {'Nome': 'Gil', 'Idade': 26, 'Cargo': 'Analista', 'Renumeracao': 12000},
#     {'Nome': 'Cassio', 'Idade': 29, 'Cargo': 'Analista', 'Renumeracao': 12100},
#       ]

# # Insirindo um documento na coleção
# inserted_document = db_connection['emp'].insert_many(data)

# # Verificando o insert
# document = db_connection['emp'].find({"Cargo": "Analista"})

# for doc in document:
#     print(doc)


# Delete (Excluir documentos):

# Excluir um único documento
# filter = {"Nome": "Junior"}
# db_connection['emp'].delete_one(filter)

# # Excluir vários documentos
# filter = {"Nome": {"$in": ["Ralf", "Gil", "Cassio"]}} 

# db_connection['emp'].delete_many(filter)



# Update (Atualizar documentos):
# Atualizar um único documento
filter = {"Nome": "Gil"}
update_data = {"$set": {"Departamento": "Marketing"}}
db_connection['emp'].update_one(filter, update_data)

# Verificando o update
document = db_connection['emp'].find({"Departamento": "Marketing"})

for doc in document:
    print(doc)

print('-'*70)

# Atualizar vários documentos
filter = {"Cargo": "Analista"}
update = {"$inc":{"Renumeracao": 500}}
db_connection['emp'].update_many(filter, update)

# Verificando o update
document = db_connection['emp'].find({"Cargo":  "Analista"})
for doc in document:
    print(doc)



# Excluindo uma chave de um documento
filter = {"Cargo": "Analista"}
# Use o operador "$unset" para excluir a chave dos documentos correspondentes
update = {"$unset": {"Renumeração": ""}}

# Exclua a chave dos documentos que correspondem ao filtro
db_connection['emp'].update_many(filter, update)
# Verificando o update
document = db_connection['emp'].find({"Cargo":  "Analista"})
for doc in document:
    print(doc)

'''