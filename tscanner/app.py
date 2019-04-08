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