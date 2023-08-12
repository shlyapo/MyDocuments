from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['my_document']

collection = db['user']
collection_contracts = db['documents']
collection_partners = db['roles']


class DbHelper(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = client['my_document']
        self.user_collection = db['users']
        # self.doc_collection = db['documents']
        self.role_collection = db['roles']
        # self.comp_collection = db['companies']

    @staticmethod
    def find_document(collection, elements, multiple=False):
        if multiple:
            results = collection.find(elements)
            return [r for r in results]
        else:
            print(collection.find_one(elements))
            return collection.find_one(elements)

    def get_collection(self, key):
        return db[key]

