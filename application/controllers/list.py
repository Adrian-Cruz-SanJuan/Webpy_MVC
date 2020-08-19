import web 
import app 

render=web.template.render('application/views/')

class List():

    def GET(self):
      try:
        return render.list()
      except Exception as e:
        return "Error" + str(e.args)