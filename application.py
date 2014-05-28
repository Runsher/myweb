#-*- encoding:utf-8 -*-
import sys
sys.path.append('/root/ye/myjob/myweb/controllers')

import os
import tornado.ioloop
import tornado.web
import Home

from tornado.options import define, options
define("port", default = 80, help = "run on the given port", type = int)

settings = {
        #"cookie_secret" : "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        #"login_url"     : "/login",
        "static_path"   : os.path.join(os.path.dirname(__file__), "static"),
        "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
        #"xsrf_cookies"  : True,
        "debug" : True,
        }

if __name__ == '__main__':
        tornado.options.parse_command_line()
        app=tornado.web.Application(
                handlers=[
                        (r'/',Home.IndexHandler),
                        (r'/f/(.*)',Home.TopHandler),
                        (r'/new/(.*)',Home.NewHandler)
			],**settings
		)

        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
