import web 
import app 

render=web.template.render('application/views/')

class Update():

    def GET(self):
      try:
        return render.update()
      except Exception as e:
        return "Error" + str(e.args)