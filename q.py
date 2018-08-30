#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import http.cookiejar
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮件函数，i表示内容
def mail(i):
	ret=True
	my_sender= 'happy3star@hotmail.com'
	my_pass='252161194'
	receivers = ['252161194@qq.com']
	mail_host="smtp.office365.com"  #设置服务器
	mail_user="happy3star@hotmail.com"    #用户名
	mail_pass="252161194"   #口令 
	 
	 
	sender = 'happy3star@hotmail.com'
	receivers = '252161194@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	 
	message = MIMEText('{"error_code":99,"error_msg":"请先登录","data":[]}', 'plain', 'utf-8')
	message['From'] = 'happy3star@hotmail.com'
	message['To'] =  '252161194@qq.com'
	 
	subject = 'Python SMTP 邮件'
	message['Subject'] = Header(subject, 'utf-8')
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.ehlo()
	smtpObj.login(mail_user,mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print ("邮件发送成功")
	return ret
	# server=smtplib.SMTP("smtp-mail.outlook.com",587)
	# server.set_debuglevel(True)
	# server.ehlo()
	# server.starttls()
	# server.login(my_sender,my_pass)
	# server.sendmail(my_sender,[my_user],msg.as_string())
	# server.quit()
	#except Exception:
	#	ret=False
def login():
	filename = 'cookie.txt'
	cookie = http.cookiejar.MozillaCookieJar(filename)  #构造一个CookieJar对象
	opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))#声明opener实例
	postdata =urllib.parse.urlencode({
		'username':'17071592636',
		'password':'a252161194',
		'captcha':'',
		'redirect_url':'http://www.smzdm.com',
		'rememberme':'on'
	}).encode('utf-8')
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0',
							'Host': 'zhiyou.smzdm.com',
							}
	loginUrl = 'https://zhiyou.smzdm.com/user/login/ajax_check'
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0')]
	opener.addheaders=[('Host','zhiyou.smzdm.com')]
	opener.addheaders=[('Referer','http://www.smzdm.com/')]
	result = opener.open(loginUrl,postdata)
	cookie.save(ignore_discard=True,ignore_expires=True)#保存cookie
ret=mail('ff')
print(ret)
# cookie = http.cookiejar.MozillaCookieJar()  #构造一个CookieJar对象
# try:
# 	cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)#加载cookie
# except:
# 	login()
# 	mail('test')
# 	cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)#加载cookie

# req = urllib.request.Request("http://zhiyou.smzdm.com/user/checkin/jsonp_checkin")#签到链接
# opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))#声明opener实例
# #opener.addheaders=[('Host','zhiyou.smzdm.com')]
# opener.addheaders=[('Referer','http://www.smzdm.com/'),('Host','zhiyou.smzdm.com')]#加载头文件
# response = opener.open(req)#get打开签到链接
# strs=response.read()#读取返回并变成str类型
# checkinData=json.loads(strs)#将str变成json
# if checkinData['error_code'] == 0:#判断成功签到不？
# 	print ('签到成功')
# 	print ('本次签到增加积分:', checkinData['data']['add_point'])
# 	print ('连续签到次数:', checkinData['data']['checkin_num'])
# 	print ('总积分:', checkinData['data']['point'])
# else:
# 	#签到失败就尝试重新获取cookie签到
# 	login()
# 	gradeUrl= 'http://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
# 	response = opener.open(req)
# 	strs=response.read().decode()
# 	checkinData=json.loads(strs)
# 	if checkinData['error_code'] == 0:
# 		print ('签到成功')
# 		print ('本次签到增加积分:', checkinData['data']['add_point'])
# 		print ('连续签到次数:', checkinData['data']['checkin_num'])
# 		print ('总积分:', checkinData['data']['point'])
# 	else:#如果还是签到失败就发送邮件
# 		ret=mail(strs.decode('unicode-escape').encode('utf-8'))
# 		print (strs)
