#coding:utf-8
import sys
import os.path
import tornado.httpserver
import tornado.web
import tornado.options
import tornado.ioloop

reload(sys)
sys.setdefaultencoding("utf8")

class BaseHandler(tornado.web.RequestHandler):
        def get_current_user(self):
#                return self.get_secure_cookie("user")
		pass

class IndexHandler(BaseHandler):
        #@tornado.web.authenticated
        def get(self):
                #name = tornado.escape.xhtml_escape(self.current_user)
                #self.render('index.html',username=name)
		self.render('index.html')


        def post(self):
                pass
