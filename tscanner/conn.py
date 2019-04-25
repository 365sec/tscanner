
class MongoConn:
    
    def __init__(self):
        print "++"
        
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
        for task in self.my_set.find():
            print(task)
