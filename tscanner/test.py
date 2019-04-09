import urllib
import httplib
import json
import time
import requests

#res1 = requests.post("http://127.0.0.1:5000/task/new", data={"task_name":"task_name","scan_cfg":{}})
#res1 = requests.post("http://127.0.0.1:5000/task/delete", data={"taskid":"2584de8f-5aa1-11e9-b2f9-b88687bf8290"})
#res1 = requests.post("http://127.0.0.1:5000/task/report", data={"taskid":"8e0e77c0-5aa4-11e9-b0d2-b88687bf8290"})
res1 = requests.post("http://127.0.0.1:5000/task/stop", data={"taskid":"dd32f09e-5abe-11e9-b17a-b88687bf8290"})
#res1 = requests.post("http://127.0.0.1:5000/task/status", data={"taskid":"8e0e77c0-5aa4-11e9-b0d2-b88687bf8290"})
print ("ask_new:",res1.json())