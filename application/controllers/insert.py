import web 
import app 

render=web.template.render('application/views/')

class Insert():

    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "Error" + str(e.args)