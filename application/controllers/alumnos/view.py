import web 
import app 

render=web.template.render('application/views/alumnos/')

class View():

    def GET(self):
      try:
        return render.view()
      except Exception as e:
        return "Error" + str(e.args)