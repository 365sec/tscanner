import urllib
import httplib
import json
import time
import requests

#res1 = requests.post("http://127.0.0.1:5000/task/new", data={"task_name":"task1","scan_cfg":{}})
#res1 = requests.post("http://127.0.0.1:5000/task/delete", data={"taskid":"baf102cf-61b6-11e9-8ef6-e0d55e8f99a0"})
#res1 = requests.post("http://127.0.0.1:5000/task/report", data={"taskid":"8e0e77c0-5aa4-11e9-b0d2-b88687bf8290"})
#res1 = requests.post("http://127.0.0.1:5000/task/stop", data={"taskid":"b2a321b0--11e-e0d55e8f99a0"})
res1 = requests.post("http://127.0.0.1:5000/task/status", data={"taskid":"6827ef80-61ea-11e9-96ce-b88687bf8290"})
print ("ask_new:",res1.json())
