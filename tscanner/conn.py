from config import mongo_settings
from pymongo import MongoClient

def retuconn():
    try:
        conn = MongoClient(mongo_settings["ip"], mongo_settings["port"])
        db = conn[mongo_settings["db_name"]]
        my_set = db[mongo_settings["set_name"]]
        return my_set
    except Exception as e:
        print(e)



class MongoConn:
    
    def __init__(self,my_set):
        print "++"
        self.my_set=my_set

    def insert(self, dic):
        try:
            self.my_set.insert(dic)
            return True
        except Exception,e:
            return False

    def update(self, dic, newdic):
        if self.dbFind(dic) != False:
            try:
                self.my_set.update(dic,{ '$set':newdic},upsert=True)
                self.findAll()
                return True
            except Exception, e:
                return False
        else:
            return False

    def deleted(self,dic):
        if self.dbFind(dic) != False:
            try:
                self.my_set.remove(dic)
                return True
            except Exception,e:
                return False
        else:
            return False

    def dbFind(self, dic):
        data = self.my_set.find(dic)
        if data.count()==0:
            return False
        else:
            data = list(data)
            data1=data[0]
            return data1

    def findAll(self):
        return self.my_set.find()

