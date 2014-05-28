#coding:utf-8
import sys
import os.path
import tornado.httpserver
import tornado.web
import tornado.options
import tornado.ioloop
from MySQL import MysqlQuery

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

		#top 5
		top1 = MysqlQuery().query_select('SELECT title,content,url,imgUrl FROM Articles.topArticle order by id desc limit 1')
		top4 = MysqlQuery().query_select('SELECT title,content,url,imgUrl FROM Articles.topArticle order by id desc limit 1,5')
		#imgUrl=MysqlQuery().query_select('SELECT imgUrl FROM Articles.topArticle order by id desc limit 1')[0][0]
		newArticles = MysqlQuery().query_select('SELECT title,shortCut,url,comeTag,imgUrl,readCount,comment,keyWords,addTime FROM Articles.Articles order by id desc')
		
		self.render('index.html',top1Item = top1,top4Items = top4,articlesItems = newArticles)


        def post(self):
                pass
class TopHandler(BaseHandler):
	def get(self,topId):
		reInfo = MysqlQuery().query_select('SELECT title,content,url,imgUrl FROM Articles.topArticle where url="%s"' %(topId))
		#self.render('top.html')
		self.render('top.html',topid=topId,info=reInfo)
	def post(self):
		#self.render('top.html')
		pass

class NewHandler(BaseHandler):
        def get(self,articleId):
                reInfo = MysqlQuery().query_select('SELECT title,content,url,imgUrl FROM Articles.topArticle where url="%s"' %(articleId))
                #self.render('top.html')
                self.render('top.html',topid=articleId,info=reInfo)
        def post(self):
                #self.render('top.html')
                pass

if __name__ == "__main__":
	a = MysqlQuery().query_select('SELECT * FROM Articles.topArticle')
	print MysqlQuery().query_select('SELECT imgUrl FROM Articles.topArticle order by id desc limit 1')[0][0]
	print a[0][2].decode('utf8')
