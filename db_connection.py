import pymongo

client = "" 
db = client.storage

class UserRepo :
    col = db.user
    
    def insertOne(self, data) :
        return self.col.insert_one(data)

    def findByUsername(self, username) :
        return self.col.find_one({"username": username})
    
    def findByUsernameAndPassword(self, username, password):
        return self.col.find_one({"username": username, "password": password})
