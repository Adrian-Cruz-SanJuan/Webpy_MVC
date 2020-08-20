import web 
import app 

render=web.template.render('application/views/alumnos/')

class Update():

    def GET(self):
      try:
        return render.update()
      except Exception as e:
        return "Error" + str(e.args)