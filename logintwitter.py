 #!/usr/bin/python
 # -*- coding: utf-8 -*-

# session[username_or_email]]

# session[password]]

# https://twitter.com/sessions

import urllib
import urllib2

#模拟witter
class Twitter:
    def __init__(self):
        # 登陆url
        self.loginUrl = "https://twitter.com/sessions"
        self.loginHeaders = {
                'cache-control':'max-age=0',
                'content-length':1347,
                'content-type':'application/x-www-form-urlencoded',
                'cookie':'xxxx',
                'origin':'https://twitter.com',
                'referer':'https://twitter.com/download?logged_out=1&lang=zh-cn',
                'upgrade-insecure-requests':1,
                'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'
                }
        self.user = 'xxxx'   # enter your username 
        self.password = 'xxx'; # enter your password
        self.post = {'session[username_or_email]':self.user,
                    'session[password]':self.password,
                    'remember_me':'1',
                    'return_to_ssl':'true',
                    'scribe_log':'',
                    'redirect_after_login':'/',
                    'authenticity_token':'xxxx', # your token in browser
                    }

    def login(self):       
        self.postData=urllib.urlencode(self.post) #编码
        request = urllib2.Request(self.loginUrl,self.postData)
        #得到第一次登录尝试的相应
        response = urllib2.urlopen(request)
        #获取其中的内容
        content = response.read()
        status = response.getcode()
        if status == 200:
            print "success\n"
            print content
        else:
            print "login fail by som reason!"


twitter = Twitter()
twitter.login()