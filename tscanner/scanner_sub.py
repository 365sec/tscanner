#coding:utf-8
#auth shaochuyu@shunwang.com
#import pytz
#import netblock
import os
import json
import uuid
import subprocess
import threading
import copy
import time
from task import Task

class Scanner(threading.Thread):
  """
   scanner for task
  """ 
  def __init__(self,task,cb):
      threading.Thread.__init__(self)
      self.task=task
      self.callback=cb
      self.msg=None
      self.msg_lock= threading.Lock()
      print "now scanner"
  
  #stop   
  def stop(self):
      print "now am stoping"
      print "this is stop"
      self.task.status=self.task.TS_STOP
      
  def set_message(self,status,info):
      self.msg_lock.acquire()
      self.msg={"status":status,"info":info}
      self.msg_lock.release()
      
  def get_message(self):
      msg= None
      self.msg_lock.acquire()
      if self.msg !=None:
         msg= copy.deepcopy(self.msg)
         self.msg=None
      self.msg_lock.release()
      return msg
  
  #start .....     
  def run(self):
     print "start ..."
     self.task.status=self.task.TS_RUNING
     self.set_message(self.task.TS_RUNING,"正在扫描中")
     self.callback(self.task.taskid,self.task.status,"now am TS_RUNING")
     for i in range(30):
         if  self.task.status==self.task.TS_STOP:
             self.task.status=self.task.TS_STOPED
             self.set_message(self.task.TS_STOPED,"扫描停止")
             self.callback(self.task.taskid,self.task.status,"now am TS_STOPED")
             return 
         time.sleep(3)  
         
     self.task.status=self.task.TS_COMPLETE
     self.set_message(self.task.TS_COMPLETE,"扫描完成")
     self.callback(self.task.taskid,self.task.status,"now am TS_COMPLETE")
    
if __name__ == "__main__":
    scan=Scanner(None)
    scan.start()
    print "ok"