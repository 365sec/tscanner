#coding:utf-8
import time


class Scheduler:
    
    def __init__(self):
        print "--"
        self.task_list=[]
    
       
    def working(self):
        print "--->"
        #time1 query  updatetime > time1 
        #last_time<updatetime<next_time
        #last_time=time.now
        while(True):
           #time1+2 >
           #step 1: 
           #last_time=next_time
           #next_time=time.now
           ##last_time<=updatetime<next_time
           print "Get new tasks"
           
           #step 2:
           print "check task status"
           
           time.sleep(1)
        
        
if __name__ == "__main__":
    print "++hellow"
    sche = Scheduler()
    sche.working()
    
    
    
