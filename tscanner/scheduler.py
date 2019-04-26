#coding:utf-8
import time
from task import Task
from copy import deepcopy
from scanner_sub import Scanner

class Scheduler:
   
    
    def __init__(self):
        self.task_scanner=[]
        

 
    
    def scheduler(self,task):
        print "now i am scheduler task now"
        print task.task_name
        print task.taskid
        print task.status
        if task.status == Task.TS_NEW :
            print "add a new Task"
            scanner=Scanner(task,self.scanner_status_callback)
            self.task_scanner.append(scanner)
            scanner.start() 
        elif task.status == Task.TS_STOP:
            print "now stop a task"
            for scanner in self.task_scanner:
                if scanner.task.taskid== task.taskid:
                   scanner.stop()
                   
        #step 1 : judge task_runing
        
        
    def flush_task(self):
        print "now flush_task"
        #{"status":status,"info":info}
        for scanner in self.task_scanner:
            msg = scanner.get_message()
            if msg != None:
                print msg["status"],msg["info"]
                print "here need change status"
                scanner.task.set_status(msg["status"],msg["info"])
        
        
        #print "-->",scanner.task.status
     
    def scanner_status_callback(self,taskid,status,msg):
        print "scanner_status_callback->",taskid,status,msg
        
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
            
            self.flush_task()
            #
            time.sleep(3)
        
        
if __name__ == "__main__":
    sche = Scheduler()
    sche.working()

    
    
    
