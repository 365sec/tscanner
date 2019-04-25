#ecoding="UTF-8"
from flask import Flask, request
import task,json
from pymongo import MongoClient
app = Flask(__name__)


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
