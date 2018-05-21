import web
import pymysql
pymysql.install_as_MySQLdb()

db = web.database(dbn='mysql',host='172.16.199.70', user='l630003053', pw='student', db='l630003053')

render = web.template.render('templates/')


urls = (
    '/registerNew', 'registerNew',
    '/add','add',
    '/index', 'index',
    '/login', 'login'
)


class registerNew:
    def GET(self):
    	todos = db.select('todo1')
    	return render.registerNew()
        # return "Hello, world!"

class add:
    def POST(self):

        i = web.input()
        n = db.insert('todo1', UN=i.UN,PW=i.PW)
        #n = db.insert('todo1', PW=i.PW)
        raise web.seeother('/login')

class index:
    def GET(self):
        return render.index()
        # return "Hello, world!"

class login:
    def GET(self):
        return render.login()
        # return "Hello, world!"



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
