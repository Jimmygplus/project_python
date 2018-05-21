#-*- coding:utf-8 -*-

import web
import pymysql
import hashlib
pymysql.install_as_MySQLdb()

db = web.database(dbn='mysql', host='mysql.uiccst.com', user='l630003053', pw='student', db='l630003053')

render = web.template.render('templates/')


urls = (
    '/', 'register',
    '/register', 'register',
    '/signIn', 'signIn',
    '/login', 'login',
    '/index', 'index',
    '/login', 'login',
)



class register:
    def GET(self):
        todos = db.select('user')
        return render.register()
        # return "Hello, world!"
        raise web.seeother('/login')

class index:
    def GET(self):
        todos = db.select('user')
        return render.index()
        # return "Hello, world!"
        #raise web.seeother('/test')


class login:
    def GET(self):
        todos = db.select('user')
        return render.login()
        # return "Hello, world!"

class signIn:
    def POST(self):
        i = web.input()
        username = i.get('user_name')
        userID = i.get('user_ID')
        password = md5(i.get('password'))
        myvar = dict(user_name=username, user_ID = userID, user_pass=password)
        results = db.select('user', myvar, where="user_ID=$user_ID")
        if not results:
            n = db.insert('user', user_name=username, user_ID=userID, user_pass=password)
            raise web.seeother('/login')
        else:
            return '<h1>Sign in error! the username have been sign in!!</h1></br><a href="/register ">sign in again</a >'

def md5(s):
    if isinstance(s, str):
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        return m.hexdigest()
    else:
        return ''

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
