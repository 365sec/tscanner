#coding:utf-8
import uuid
import time


class Task:
    def __init__(self,my_set):
        self.my_set=my_set
        self.taskid=""
        self.task_name=""
        self.status=0
        self.msg=""
        self.scan_cfg={}
        self.report_path=""
        self.start_time=""
        self.end_time=""
        self.start_time = time.strftime('%Y.%m.%d %H-%M-%S', time.localtime(time.time()))


    def insert(self, dic):
        try:
            self.my_set.insert(dic)
            return True
        except Exception,e:
            return False

    def update(self, dic, newdic):
        try:
            self.my_set.update(dic,newdic,upsert=True)
            return True
        except Exception, e:
            return False

    def deleted(self,dic):
        try:
            self.my_set.remove(dic)
            return True
        except Exception,e:
            return False

    def dbFind(self, dic):
        data = self.my_set.find(dic)
        data = list(data)
        data1=data[0]
        return data1

    def findAll(self):
        for i in self.my_set.find():
            print(i)
    def getuuid(self):
        self.taskid=str(uuid.uuid1())

    def new(self,task_name,scan_cfg):
        self.task_name=task_name
        self.scan_cfg=scan_cfg
        self.getuuid()
        save_obj ={
            "taskid":self.taskid,
            "task_name":self.task_name,
            "status":self.status,
            "msg":self.msg,
            "scan_cfg":self.scan_cfg,
            "report_path":self.report_path,
            "start_time":self.start_time,
            "end_time":self.end_time
        }
        return  self.insert(save_obj)

    def stop(self, taskid):
        self.taskid=taskid
        self.status=1
        dic={"taskid":self.taskid}
        newdic={"$set":{"status":self.status}}
        return self.update(dic, newdic )

    def delete(self, taskid):
        self.taskid=taskid
        dic={"taskid":self.taskid}
        return self.deleted(dic)

    def report(self, taskid):
        self.taskid=taskid
        dic = {"taskid": self.taskid}
        try:
            re=self.dbFind(dic)
            self.report_path= re["report_path"]
            return True
        except Exception,e:
            return False
    def restatus(self, taskid):
        self.taskid=taskid
        dic = {"taskid": self.taskid}
        try:
            re=self.dbFind(dic)
            self.status= re["status"]
            return True
        except Exception,e:
            return False