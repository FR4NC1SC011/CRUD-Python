from bson import ObjectId
from pymongo import MongoClient
import logging as log

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
        # output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return documents

    # def write(self, data):
    #     log.info('Writing Data')
    #     new_document = data['Document']
    #     response = self.collection.insert_one(new_document)
    #     output = {'Status': 'Successfully Inserted',
    #                 'Document_ID': str(response.inserted_id)}
    #     return output

    def write(self, data):
        log.info('Writing Data')
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

    # def update(self):
    #     filt = self.data['Filter']
    #     updated_data = {"$set": self.data['DataToBeUpdated']}
    #     response = self.collection.update_one(filt, updated_data)
    #     output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
    #     return output

    def update(self, id, data):
        user = self.get_user_by_id(id)
        if user:
            for field, value in data.items():
                user[field] = value
            self.collection.update_one({'_id': ObjectId(id)}, {'$set': user})
            return True
        return False

    def delete(self, id):
        # filt = data['Filter']
        # response = self.collection.delete_one(filt)
        response = self.collection.delete_one(
            {
                "_id": ObjectId(id)
            }
        )
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

    def get_user_by_id(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})
