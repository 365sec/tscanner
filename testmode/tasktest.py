#encoding:utf-8

import json
import unittest
from tscanner.main import  app
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import sys

class TaskTest(unittest.TestCase):
    def setUp(self):
        print "---"
        app.testing = True
        self.client = app.test_client()

    def test_new(self):
            """测试用户名与密码为空的情况[当参数不全的话，返回errcode=-2]"""
            response = self.client.post('/task/new',data={"ask_name":"task_name","scan_cfg":""})
            json_data = response.data
            json_dict = json.loads(json_data)
            print "--->",json_dict
            self.assertIn('code', json_dict, '数据格式返回错误')
            self.assertEqual(json_dict['code'], 0, '状态码返回错误')

    def test_stop(self):
            """测试用户名与密码为空的情况[当参数不全的话，返回errcode=-2]"""
            response = self.client.post('/task/stop',data={"taskid":"2584de8f-5aa1-11e9-b2f9-b88687bf8290"})
            json_data = response.data
            json_dict = json.loads(json_data)
            print "--->",json_dict
            self.assertIn('code', json_dict, '数据格式返回错误')
            self.assertEqual(json_dict['code'], 0, '状态码返回错误')
    def test_report(self):
            """测试用户名与密码为空的情况[当参数不全的话，返回errcode=-2]"""
            response = self.client.post('/task/report',data={"taskid":"2584de8f-5aa1-11e9-b2f9-b88687bf8290"})
            json_data = response.data
            json_dict = json.loads(json_data)
            print "--->",json_dict
            self.assertIn('report_path', json_dict, '数据格式返回错误')
            self.assertEqual(json_dict['report_path'], "", '状态码返回错误')
    def test_status(self):
            """测试用户名与密码为空的情况[当参数不全的话，返回errcode=-2]"""
            response = self.client.post('/task/status',data={"taskid":"2584de8f-5aa1-11e9-b2f9-b88687bf8290"})
            json_data = response.data
            json_dict = json.loads(json_data)
            print "--->",json_dict
            self.assertIn('status', json_dict, '数据格式返回错误')
            self.assertEqual(json_dict['status'], 0, '状态码返回错误')
    def test_delete(self):
            """测试用户名与密码为空的情况[当参数不全的话，返回errcode=-2]"""
            response = self.client.post('/task/delete',data={"taskid":"2584de8f-5aa1-11e9-b2f9-b88687bf8290"})
            json_data = response.data
            json_dict = json.loads(json_data)
            print "--->",json_dict
            self.assertIn('code', json_dict, '数据格式返回错误')
            self.assertEqual(json_dict['code'], 0, '状态码返回错误')

    def atest_error_username_password(self):
                """测试用户名和密码错误的情况[当登录名和密码错误的时候，返回 errcode = -1]"""
                response = self.client.post('/login', data={"username": "aaaaa", "password": "12343"})
                json_data = response.data
                json_dict = json.loads(json_data)
                self.assertIn('errcode', json_dict, '数据格式返回错误')
                self.assertEqual(json_dict['errcode'], -1, '状态码返回错误')
"""
class TestAdd (unittest.TestCase):
    def setUp(self):
        print("test TestAdd :")
    def test_bbb(self):
        print("test bbb")
    def tearDown(self):
        pass
"""



if __name__ == '__main__':
    """
     suite = unittest.TestSuite()
    suite.addTest(TaskTest('test_new'))
    suite.addTest(TaskTest('test_stop'))
    suite.addTest(TaskTest('test_report'))
    #suite.addTest(TaskTest('test_status'))
    suite.addTest(TaskTest('test_delete'))
    run = unittest.TextTestRunner()
    run.run(suite)
    """
