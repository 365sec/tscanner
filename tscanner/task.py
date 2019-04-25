#coding:utf-8
import uuid
import time
from conn import retuconn
from conn import MongoConn

class Task:
    TS_NEW=1
    TS_RUNING=2
    TS_STOP=3
    TS_ERROR=4
    TS_STOPED=5
    TS_COMPLETE=6
    
    def __init__(self):
        self.taskid=""
        self.task_name=""
        self.status=0
        self.msg=""
        self.scan_cfg={}
        self.start_time=""
        self.end_time=""

    def setvalues(self,taskid = "",task_name = "",status = 0,msg = "",scan_cfg = {},start_time = "",end_time = ""):
        self.taskid = taskid
        self.task_name = task_name
        self.status = status
        self.msg = msg
        self.scan_cfg = scan_cfg
        self.start_time = start_time
        self.end_time = end_time

    
    def getstart_time(self):
        starttime_list=[]
        conn1 = retuconn()
        opeartor = MongoConn(conn1)
        for task in opeartor.findAll():
            ##setvalues(self, taskid="", task_name="", status=0, msg="", scan_cfg={}, report_path="",start_time="", end_time=""):
            starttime_list.append((task.get("taskid"),task.get("task_name"),task.get("status"),task.get("msg"),task.get("scan_cfg"),task.get("start_time"),task.get("end_time")))
        return  starttime_list

    def getuuid(self):
        self.taskid=str(uuid.uuid1())

    def new(self,task_name,scan_cfg):
        self.task_name=task_name
        self.scan_cfg=scan_cfg
        self.getuuid()
        conn1 = retuconn()
        opeartor = MongoConn(conn1)
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        save_obj ={
            "taskid":self.taskid,
            "task_name":self.task_name,
            "status":self.status,
            "msg":self.msg,
            "scan_cfg":self.scan_cfg,
            "start_time":start_time,
            "end_time":self.end_time
        }
        return  opeartor.insert(save_obj)

    def stop(self, taskid):
        conn1 = retuconn()
        opeartor=MongoConn(conn1)
        self.taskid=taskid
        self.status=1
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        dic={"taskid":self.taskid}
        newdic={"status":1,"start_time":start_time}
        return opeartor.update(dic, newdic )

    def delete(self, taskid):
        conn1 = retuconn()
        opeartor = MongoConn(conn1)
        self.taskid=taskid
        dic={"taskid":self.taskid}
        conn1 = retuconn()
        return opeartor.deleted(dic)


    def get_status(self, taskid):
        self.taskid=taskid
        dic = {"taskid": self.taskid}
        try:
            conn1 = retuconn()
            opeartor = MongoConn(conn1)
            re=opeartor.dbFind(dic)
            print re
            if re:
                self.status= re.get("status")
                return True
            else:
                return False
        except Exception,e:
            return False