import urllib
import json
import time
import requests

res1 = requests.post("http://127.0.0.1:5000/task/new", data={"task_name":"task0","scan_cfg":{}})
#res1 = requests.post("http://127.0.0.1:5000/task/delete", data={"taskid":"4e417421-6739-11e9-aaf9-e0d55e8f99a0"})
#res1 = requests.post("http://127.0.0.1:5000/task/stop", data={"taskid":"bd1c2c56-680f-11e9-a9a3-000c2971424c"})
#res1 = requests.post("http://127.0.0.1:5000/task/status", data={"taskid":"604c0670-673a-11e9-bd1f-e0d55e8f99a0"})
print ("ask_new:",res1.json())
