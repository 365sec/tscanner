#coding:utf-8
#auth shaochuyu@shunwang.com
import pytz
import os
import json
import uuid
import netblock
import subprocess
import time

import threading

class Scanner(threading.Thread):
  """
   scanner for task
  """ 
  def __init__(self,task):
      threading.Thread.__init__(self)
      self.task=task
      print "now scanner"

  #stop   
  def stop(self):
      print "now am stoping"
      print "this is stop"
      
  #ifconfig   
  def get_status(self):
      print "get the status of scanner"
  
  def set_status(self,status,info):
      print "get the status of scanner"
  #start .....     
  def run(self):
     print "start ..."
    
if __name__ == "__main__":
    scan=Scanner(None)
    scan.start()
    print "ok"