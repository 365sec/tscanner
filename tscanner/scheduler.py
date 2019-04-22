#coding:utf-8
import time
from app import my_set
from task import Task

class Scheduler:
    def __init__(self,my_set,Task):
        self.task_list=[]
        self.my_set=my_set


    def checkon(self,value):
        for tasklist in self.task_list:
            if tasklist.taskid==value:
                return tasklist
            else:
                return False


    def working(self):
        print "--->"
        #time1 query  updatetime > time1
        #last_time<updatetime<next_time
        last_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        next_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        updatetime='2019-04-18 14:59:20'
        while(True):
            tasks = Task(my_set)
            starttime_list = tasks.getstart_time()
            #print starttime_list
            last_time=next_time
            next_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            timeArraylast = time.strptime(last_time, "%Y-%m-%d %H:%M:%S")
            timeStamplast = int(time.mktime(timeArraylast))
            for timetup1 in starttime_list:
                timeArrayup = time.strptime(timetup1[6], "%Y-%m-%d %H:%M:%S")
                timeStampup = int(time.mktime(timeArrayup))
                if timeStampup >= timeStamplast:
                    #setvalues(self, taskid="", task_name="", status=0, msg="", scan_cfg={}, report_path="",start_time="", end_time=""):
                    tasks.setvalues(timetup1[0],timetup1[1],timetup1[2],timetup1[3],timetup1[4],timetup1[5],timetup1[6],timetup1[7])
                    if self.checkon(timetup1[0]):
                        pass
                    else:
                        self.task_list.append(tasks)

            print self.task_list
            time.sleep(1)
        
        
if __name__ == "__main__":
    sche = Scheduler(my_set,Task)
    sche.working()

    
    
    
