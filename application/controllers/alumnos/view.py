  
import web 
import app 

import application.models.model as alumnos

model_alumnos = alumnos.Alumnos()

render=web.template.render('application/views/alumnos')

class View():

    def GET(self, matricula):
      try:
        result = model_alumnos.view(matricula)[0]
        return render.view(result)
      except Exception as e:
        return "Error" + str(e.args)