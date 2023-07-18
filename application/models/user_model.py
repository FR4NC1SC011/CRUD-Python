from bson import ObjectId
from pymongo import MongoClient

class User:
    def __init__(self, data=None):
        self.client = MongoClient("mongodb://localhost:27017/")  
      
        database = "Python-CRUD"
        collection = "people"
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data


    def read(self):
        documents = self.collection.find()
        return documents

    def write(self, data):
        new_document = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'age': data['age']
        }
        response = self.collection.insert_one(new_document)
        output = {
            'Status': 'Successfully Inserted',
            'Document_ID': str(response.inserted_id)
        }
        return output

    def update(self, id, data):
        user = self.get_user_by_id(id)
        if user:
            for field, value in data.items():
                user[field] = value
            self.collection.update_one({'_id': ObjectId(id)}, {'$set': user})
            return True
        return False

    def delete(self, id):
        response = self.collection.delete_one(
            {
                "_id": ObjectId(id)
            }
        )
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

    def get_user_by_id(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})
