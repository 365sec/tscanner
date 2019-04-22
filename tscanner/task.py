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

    def setvalues(self,taskid = "",task_name = "",status = 0,msg = "",scan_cfg = {},report_path = "",start_time = "",end_time = ""):
        self.taskid = taskid
        self.task_name = task_name
        self.status = status
        self.msg = msg
        self.scan_cfg = scan_cfg
        self.report_path = report_path
        self.start_time = start_time
        self.end_time = end_time
        print "重构成功"

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

    def getstart_time(self):
        starttime_list=[]
        for task in self.my_set.find():
            ##setvalues(self, taskid="", task_name="", status=0, msg="", scan_cfg={}, report_path="",start_time="", end_time=""):
            starttime_list.append((task.get("taskid"),task.get("task_name"),task.get("status"),task.get("msg"),task.get("scan_cfg"),task.get("report_path"),task.get("start_time"),task.get("end_time")))
        return  starttime_list

    def getuuid(self):
        self.taskid=str(uuid.uuid1())

    def new(self,task_name,scan_cfg):
        self.task_name=task_name
        self.scan_cfg=scan_cfg
        self.getuuid()
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        save_obj ={
            "taskid":self.taskid,
            "task_name":self.task_name,
            "status":self.status,
            "msg":self.msg,
            "scan_cfg":self.scan_cfg,
            "report_path":self.report_path,
            "start_time":start_time,
            "end_time":self.end_time
        }
        return  self.insert(save_obj)

    def stop(self, taskid):
        self.taskid=taskid
        self.status=1
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        dic={"taskid":self.taskid}
        newdic={"status":1,"start_time":start_time}
        return self.update(dic, newdic )

    def delete(self, taskid):
        self.taskid=taskid
        dic={"taskid":self.taskid}
        return self.deleted(dic)

    def report(self, taskid):
        self.taskid=taskid
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        newdic={"start_time":start_time}
        dic = {"taskid": self.taskid}
        try:
            re=self.dbFind(dic)
            if re:
                self.report_path= re.get("report_path")
                self.update(dic,newdic)
                return True
            else:
                return False
        except Exception,e:
            return False

    def restatus(self, taskid):
        self.taskid=taskid
        dic = {"taskid": self.taskid}
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        newdic={"start_time":start_time}
        try:
            re=self.dbFind(dic)
            if re:
                self.status= re.get("status")
                self.update(dic,newdic)
                return True
            else:
                return False
        except Exception,e:
            return False