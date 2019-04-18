#ecoding="UTF-8"
from flask import Flask, request
from pymongo import MongoClient
from config import mongo_settings
import task,json

app = Flask(__name__)

try:
    conn = MongoClient(mongo_settings["ip"], mongo_settings["port"])
    db = conn[mongo_settings["db_name"]]
    my_set = db[mongo_settings["set_name"]]
except Exception as e:
    print(e)


@app.route('/task/new',methods=["GET","POST"])
def ask_new():
    task_name= request.form.get('task_name')
    scan_cfg= request.form.get('scan_cfg')
    tasks=task.Task(my_set)
    if tasks.new(task_name,scan_cfg):
        contect={
            "code":0,
            "id":tasks.taskid
        }
    else:
        contect ={
                "code":1,
                "msg":"error"
        }
    tasks.findAll()
    return json.dumps(contect,encoding="UTF-8", ensure_ascii=False)

@app.route('/task/stop',methods=["GET","POST"])
def task_stop():
    taskid= request.form.get('taskid')
    tasks = task.Task(my_set)
    if tasks.stop(taskid):
        contect = {
            "code": 0,
        }
    else:
        contect = {
            "code": 1,
            "msg": "error"
        }
    return json.dumps(contect, encoding="UTF-8", ensure_ascii=False)

@app.route('/task/delete',methods=["GET","POST"])
def task_delete():
    taskid = request.form.get('taskid')
    tasks = task.Task(my_set)
    if tasks.delete(taskid):
        contect = {
            "code": 0,
        }
    else:
        contect = {
            "code": 1,
            "msg": "error"
        }
    print contect
    return json.dumps(contect, encoding="UTF-8", ensure_ascii=False)

@app.route('/task/report',methods=["GET","POST"])
def task_report():
    taskid = request.form.get('taskid')
    tasks = task.Task(my_set)
    if tasks.report(taskid):
        contect = {
            "report_path":tasks.report_path
        }
    else:
        contect = {
            "code": 1,
            "msg": "error"
        }
    return json.dumps(contect, encoding="UTF-8", ensure_ascii=False)

@app.route('/task/status',methods=["GET","POST"])
def task_status():
    taskid = request.form.get('taskid')
    tasks = task.Task(my_set)
    if tasks.restatus(taskid):
        contect = {
            "status":tasks.status
        }
    else:
        contect = {
            "code": 1,
            "msg": "error"
        }
    return json.dumps(contect, encoding="UTF-8", ensure_ascii=False)
if __name__ == '__main__':
    app.run()

"""
#interface 1
#task/new
#write info to mogodb
#input
{"task_name":"","scan_cfg":{}}
#output
#successed
{"code":0,"id":"taskid"}
#failed
{"code":1,"msg":"error"}


#interface 2
#task/stop
#write info to mogodb
#input
{"id":"taskid"}
#output
#successed
{"code":0}
#failed
{"code":1,"msg":"error"}

#interface 3
#read status from mongodb
#task/delete
#input
#successed
{"code":0}
#failed
{"code":1,"msg":"error"}


#interface 4
#task/report
#read report  from mongodb
#input
{"id":"taskid"}
#output
{"report_path":""}
"""