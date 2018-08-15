#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-15
import requests
from bs4 import BeautifulSoup
import sys,json
import re
from user import *

class smzdm:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0',
                        'Host': 'www.sucaihuo.com',
                        }
        self.session = requests.session()

    def login(self):
        data={}
        data['username'] = self.username
        data['pwd'] = self.password
        loginURL = 'http://www.sucaihuo.com/Login/check'
        try:
            req = self.session.post(loginURL, data=data, headers=self.headers,verify=False)
            #print req.text
            return req.json()['error']
        except urllib.error.HTTPError as e:
            print (e)
            sys.exit(1)

    def checkin(self):
        signURL = 'http://www.sucaihuo.com/Member/sign.html'
        self.headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0',
                        'Host': 'www.sucaihuo.com','Referer':'http://www.sucaihuo.com/',
                        }
        checkinREQ = self.session.get(signURL, headers=self.headers,verify=False)
        #print json.dumps(checkinREQ)
        #print checkinREQ.text
        matchObj = re.search( r'data-key="(.*?)"', checkinREQ.text, re.M|re.I)
        data={}
        data['key']=matchObj.group(1)
        print (data['key'])
        signURLS='http://www.sucaihuo.com/Member/signDay'
        checkinREQ2 = self.session.post(signURLS,data=data ,headers=self.headers,verify=False)
        #print json.loads(checkinREQ.text)
        #print checkinREQ.text
        
        #return checkinREQ.json()['data']
        print (checkinREQ2.text)
        return checkinREQ2.text

    def start(self):
        loginData = self.login()
        if loginData == 0:
            print ('登陆成功')
            print ('签到中....')

        checkinData = self.checkin()
        if checkinData=='-1':
            print ('签到失败，请重新检查')
        else:
            print ('签到成功')


if __name__ == "__main__":
    smzmdLogin = smzdm(UserName, PassWord)
    smzmdLogin.start()
