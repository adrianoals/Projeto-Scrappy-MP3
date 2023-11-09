from pymongo import MongoClient

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
    try:
        inserted_document = db_connection[collection_name].insert_one(data)
        print("Documento inserido com sucesso. O ID do documento é: ", inserted_document.inserted_id)
        return inserted_document
    except Exception as e:
        print("Ocorreu um erro ao inserir o documento: ", e)


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

