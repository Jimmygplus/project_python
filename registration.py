#-*- coding:utf-8 -*-
import importlib, sys
importlib.reload(sys)
print(sys.version)
import web
import pymysql
import hashlib
pymysql.install_as_MySQLdb()

db = web.database(dbn='mysql', host='mysql.uiccst.com', user='l630003053', pw='student', db='l630003053')

# render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/index', 'index',
    '/register', 'register',
    '/signUp', 'signUp',
    '/signUp2', 'signUp2',
    '/signIn', 'signIn',
    '/login', 'login',
    '/todayOnline', 'todayOnline',
    '/test', 'test',
    '/tdOl', 'tdOl',
    '/adNwUs', 'adNwUs',
    '/clAdmin', 'clAdmin',
    '/chOnlnTm', 'chOnlnTm',
    '/delUs', 'delUs',
    '/hisBil', 'hisBil',
    '/usInfo', 'usInfo',
    '/usProfil', 'usProfil',
    '/usRech', 'usRech',
    '/adminProfile', 'adminProfile',
    '/userAfterLogin', 'userAfterLogin',
    '/adminAfterLogin', 'adminAfterLogin',
    '/successful', 'successful',
    '/delete', 'delete'
)
# router

web.config.debug = False

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore('sessions'))


# class
# templates
render = web.template.render('templates/', globals={'context': session})

class register:
    def GET(self):
        return render.register()
        # return "Hello, world!"
        raise web.seeother('/login')

class index:
    def GET(self):
        return render.index()
        # return "Hello, world!"
        #raise web.seeother('/test')

class todayOnline:
    def GET(self):
        return render.todayOnline()
        # return "Hello, world!"
        #raise web.seeother('/test')

class tdOl:
    def GET(self):
        user = db.select('user')
        return render.tdOl(user)

class adNwUs:
    def GET(self):
        user = db.select('user')
        return render.adNwUs(user)
        raise web.seeother('/userAfterLogin')

class clAdmin:
    def GET(self):
        user = db.select('user')
        return render.clAdmin()

class chOnlnTm:
    def GET(self):
        user = db.select('user')
        return render.chOnlnTm()

class delUs:
    def GET(self):
        user = db.select('user')
        return render.delUs(user)

class hisBil:
    def GET(self):
        user = db.select('user')
        return render.hisBil()

class usInfo:
    def GET(self):
        user = db.select('user')
        return render.usInfo()

class usProfil:
    def GET(self):
        user = db.select('user')
        return render.usProfil()

class usRech:
    def GET(self):
        user = db.select('user')
        return render.usRech()

class adminProfile:
    def GET(self):
        user = db.select('user')
        return render.adminProfile()

class userAfterLogin:
    def GET(self):
        user = db.select('user')
        return render.userAfterLogin()

class adminAfterLogin:
    def GET(self):
        user = db.select('user')
        return render.adminAfterLogin()

class login:
    def GET(self):
        return render.login()
        # return "Hello, world!"

class successful:
    def GET(self):
        return render.successful()
        # return "Hello, world!"

class signUp:
    def POST(self):
        i = web.input()
        username = i.get('user_name')
        userID = i.get('user_ID')
        password = md5(i.get('password'))
        myvar = dict(user_name=username, user_ID = userID, user_pass=password)
        results = db.select('user', myvar, where="user_ID=$user_ID")
        if not results:
            n = db.insert('user', user_name=username, user_ID=userID, password=password)
            raise web.seeother('/login')
        else:
            return '<h1>Sign up error! The user ID have been sign in!!</h1></br><a href="/register ">sign in again</a >'

class signUp2:
    def POST(self):
        i = web.input()
        username = i.get('user_name')
        userID = i.get('user_ID')
        password = md5(i.get('password'))
        myvar = dict(user_name=username, user_ID = userID, user_pass=password)
        results = db.select('user', myvar, where="user_ID=$user_ID")
        if not results:
            n = db.insert('user', user_name=username, user_ID=userID, password=password)
            raise web.seeother('/successful')
        else:
            return '<h1>Sign up error! The user ID have been sign in!!</h1></br><a href="/adNwUs ">Add again</a >'


class signIn:
    def POST(self):
        i = web.input()
        userID = i.get('user_ID')
        password = md5(i.get('password'))
        myvar = dict(user_ID = userID, user_pass=password)
        results = db.select('user', myvar, where="user_ID=$user_ID and password=$user_pass")
        if results:
            r = results[0]
            session.logged_in = True
            session.uid = r.user_ID
            session.uname = r.user_name
            session.ubalance = r.balance
            raise web.seeother('/tdOl')
        else:
            return '<h1>Login Error!!!</h1></br><a href="/login">Login</a>'

class delete:
    def POST(self):
        i = web.input()
        userID = i.get('user_ID')
        #password = md5(i.get('password'))
        myvar = dict(user_ID = userID)
        results = db.delete('user', myvar, where="user_ID=$user_ID")
        if results:
            r = results[0]
            session.logged_in = False
            #raise web.seeother('/delUs')
            return render.delUs()
        else:
            return '<h1>Wrong pass word!!!</h1></br><a href="/delUs">Do it again</a>'

class test:
    def GET(self):  
       user = db.select('user')  
       return render.test(user)  

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
