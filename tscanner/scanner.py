#coding:utf-8
#auth shaochuyu@shunwang.com
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
  def __init__(self):
      threading.Thread.__init__(self)
      self.task={"ports":"80,22,88","iface":"eth0","rate":6000}
      self.domains=[]
      self.ip_domain=[]
      self.ipranges=netblock.IPRanges()
      print "now scanner"
    
  
  #stop   
  def stop(self):
      print "now am stoping"
      print "this is stop"
      
  #ifconfig   
  def status(self):
      print "get the status of scanner"

  #call process
  def call_subprocess(self,commands):
      #ls | grep t |grep e
      print commands
      ps=[]
      for i in range(len(commands)):
        if len(commands) == 1:
            ps.append(subprocess.Popen(commands[i])) 
        elif i == 0:
            ps.append(subprocess.Popen(commands[i], stdout=subprocess.PIPE))
        elif i ==len(commands)-1:
            ps.append(subprocess.Popen(commands[i], stdin=ps[-1].stdout))
        else:
            ps.append(subprocess.Popen(commands[i], stdin=ps[-1].stdout,stdout=subprocess.PIPE))
               
      while True:
            cmp_task=[]
            #----------------------
            for i in range(len(ps)):
               if i in cmp_task:
                   continue
               status = ps[i].poll()
               if status != None:
                   cmp_task.append(i)
               else:
                   time.sleep(1)
            #----------------------  
            #need stop taks
            #stop all task
            if len(cmp_task) == len(ps):
                break
      #Determines whether the program exits
      
  #parse dnsanswer
  def parse_dnsanswer(self,line):
        data=json.loads(line)
        iscname= False
        stat=data.get("status")
        domain = data.get("name")
        if stat == "NOERROR":
            for  answer in data.get("data",{}).get("answers",[]):
                if answer["type"] == "A" :
                    if iscname:
                        self.ip_domain.append((answer["answer"],domain ))
                        self.ipranges.addoddcidr(answer["answer"])
                        break 
                    self.ip_domain.append((answer["answer"],domain ))
                    self.ipranges.addoddcidr(answer["answer"])
                elif  answer["type"] == "CNAME" and domain == answer["name"]:
                    iscname=True
    
  #dns parser     
  def dns_parser(self):
        #./tdns  a  --timeout=25 --threads=1000 input-file=.tmp --output-file=  
        tmpinput="%s_input.tmp"%(uuid.uuid4())
        tmpoutput="%s_output.tmp"%(uuid.uuid4())
        cmd=["tdns","a"  ,"--timeout=25", "--threads=1000", "--input-file=%s"%tmpinput,"--output-file=%s"%tmpoutput]
        print cmd
        finput=open(tmpinput,"wb")
        for domain in self.domains:
            finput.write("%s\n"%(domain))
        finput.close()
        #do dns parser
        self.call_subprocess([cmd])
        #testing is a 
        fdns=open(tmpoutput,"rb")
        for l in fdns:
            text =l.rstrip().lstrip()
            if text=="":
                continue
            else:
                self.parse_dnsanswer(text)
        fdns.close()
        #delete temp file
        os.remove(tmpinput)
        os.remove(tmpoutput) 
           
  def scanpoc(self):   
      print "not start to scan poc"   
         
  #start .....     
  def run(self):
        try:
            f=open("target.txt","rb")
        except Exception as e:
            print "file %s not exit"%("target")
            return 
        print "this is  a line "
        for line in f :
            try:
                self.ipranges.addoddcidr(line.lstrip().rstrip())
            except Exception as e:
                self.domains.append(line.lstrip().rstrip())
        f.close()
        if len(self.domains) > 0 :
           self.dns_parser()       
        tmpip="%s_ip.tmp"%(uuid.uuid4())
        tmpipdomain="%s_ipdomain.tmp"%(uuid.uuid4())
        lenip=len(self.ipranges)
        lenipdomain=len(self.ip_domain)
        #--------------
        #set_status({"scanip":str(lenip),"scandomain":str(lenipdomain)})
        #--------------
        fip=open(tmpip,"wb")
        fipdomain=open(tmpipdomain,"wb")
        for ips in self.ipranges.tocidr():
            fip.write("%s\n"%ips)
        fip.close()
        
        command_ttag=["ttag","-O","ttag.outgoing.Mongo","-t","Task-%s"%(uuid.uuid4())] 
        
        #scanner ip target
        #-O ttag.outgoing.Mongo  -t Task-00010001
        command=["masscan","-i",self.task["iface"],"--rate=%d"%self.task["rate"],"-p",self.task["ports"],"-iL", tmpip]
        self.call_subprocess([command,["tprotocol"],command_ttag])
        os.remove(tmpip)
        
        #scanner domain target
        for ipdomain in self.ip_domain:
            fipdomain.write("%s,%s\n"%ipdomain)
        fipdomain.close()
        self.call_subprocess([["cat",tmpipdomain],["tprotocol"],command_ttag])
        os.remove(tmpipdomain) 
       
        #------------
        #now scanpoc
        self.scanpoc()
        
        #------------
        #set_status({"status":"FINISH"})
        print "--"
        print "#[%d,%d,%s,%s]"%(lenip,lenipdomain,tmpip,tmpipdomain)
        #now start scanpoc
    
    
if __name__ == "__main__":
    scan=Scanner()
    scan.start()
    print "ok"