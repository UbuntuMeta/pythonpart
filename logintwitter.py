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
                 'cookie':'guest_id=v1%3A143814661152520214; webn=1867731360; lang=zh-cn; _gat=1; h=%5B%7B%22newer_tweet_id%22%3Anull%2C%22older_tweet_id%22%3A%22645515360523956224%22%2C%22promoted_content%22%3A%7B%22impression_id%22%3A%22756d1944ed6f0dfb%22%2C%22disclosure_type%22%3A%22promoted%22%2C%22disclosure_text%22%3A%22%22%7D%2C%22experiment_values%22%3A%7B%22website_card_variation%22%3A%220%22%7D%2C%22advertiser_id%22%3A%222350015015%22%2C%22created_at%22%3A%221442754230%22%2C%22tweet_id%22%3A%22638712495637565442%22%7D%2C%7B%22newer_tweet_id%22%3A%22645439335601303552%22%2C%22older_tweet_id%22%3A%22645438930976829440%22%2C%22promoted_content%22%3A%7B%22impression_id%22%3A%22756dafab0997514b%22%2C%22disclosure_type%22%3A%22promoted%22%2C%22disclosure_text%22%3A%22%22%7D%2C%22experiment_values%22%3A%7B%22suppress_media_forward%22%3A%22true%22%2C%22pac_in_timeline%22%3A%22true%22%7D%2C%22advertiser_id%22%3A%22487118986%22%2C%22created_at%22%3A%221442754230%22%2C%22tweet_id%22%3A%22608235822005907457%22%7D%2C%7B%22newer_tweet_id%22%3A%22645578423998509060%22%2C%22older_tweet_id%22%3A%22645571624952037376%22%2C%22promoted_content%22%3A%7B%22impression_id%22%3A%2275686759d2131b4b%22%2C%22disclosure_type%22%3A%22promoted%22%2C%22disclosure_text%22%3A%22%22%7D%2C%22experiment_values%22%3A%7B%22website_card_variation%22%3A%220%22%7D%2C%22advertiser_id%22%3A%2216334724%22%2C%22created_at%22%3A%221442753556%22%2C%22tweet_id%22%3A%22643841827443896320%22%7D%2C%7B%22newer_tweet_id%22%3A%22645530311711920128%22%2C%22older_tweet_id%22%3A%22645528152962428928%22%2C%22promoted_content%22%3A%7B%22impression_id%22%3A%227568bdca20406673%22%2C%22disclosure_type%22%3A%22promoted%22%2C%22disclosure_text%22%3A%22%22%7D%2C%22experiment_values%22%3A%7B%7D%2C%22advertiser_id%22%3A%22480858748%22%2C%22created_at%22%3A%221442753556%22%2C%22tweet_id%22%3A%22630899367986094080%22%7D%5D; kdt=Z7IyL6db9bkFsM3dTccUFEfuLReF5h2JH6YHr7oy; remember_checked_on=1; dnt=1; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCKQt0OpPAToMY3NyZl9p%250AZCIlODAwMzNiMDIyNDg4Njc3MDA2Y2ZjZTZmMjMzNTZhOGE6B2lkIiU5NjRi%250AMWQ3NjMzNDVjOTg5ZGRlYjY1ZTBmNWFmMDU0MjoJdXNlcmwrB6BRU28%253D--6e4386905f489a6f6cba8e151026d307cfa7553d; _ga=GA1.2.1939843525.1442753521',

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