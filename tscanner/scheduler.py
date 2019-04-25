#coding:utf-8
import time
from task import Task
from task import Task
from copy import deepcopy
from scanner_sub import Scanner

class Scheduler:
   
    
    def __init__(self):
        self.task_runing=[]
        self.task_wait =[]
 
    def scheduler(self,task):
        print "---"
        print "now i am scheduler task now"
        
    def working(self):
        print "--->"
        #time1 query  updatetime > time1
        #last_time<updatetime<next_time
        last_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        next_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        while(True):
            t=Task()
            tasks = deepcopy(t)
            starttime_list = tasks.getstart_time()
            #print starttime_list
            last_time=next_time
            next_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            timeArraylast = time.strptime(last_time, "%Y-%m-%d %H:%M:%S")
            timeStamplast = int(time.mktime(timeArraylast))
            for timetup1 in starttime_list:
                timeArrayup = time.strptime(timetup1[5], "%Y-%m-%d %H:%M:%S")
                timeStampup = int(time.mktime(timeArrayup))
                if timeStampup >= timeStamplast:
                    #setvalues(self, taskid="", task_name="", status=0, msg="", scan_cfg={,start_time="", end_time=""):
                    tasks.setvalues(timetup1[0],timetup1[1],timetup1[2],timetup1[3],timetup1[4],timetup1[5],timetup1[6])
                    self.scheduler(tasks)
            print "-----------------"
            
            #
            time.sleep(2)
        
        
if __name__ == "__main__":
    sche = Scheduler()
    sche.working()

    
    
    
