import web 
import app 
import application.models.model as alumnos

model_alumnos = alumnos.Alumnos()

render=web.template.render('application/views/alumnos/')

class List():

    def GET(self):
      try:
        result = model_alumnos.select()
        return render.list(result)
      except Exception as e:
        return "Error 1" + str(e.args)