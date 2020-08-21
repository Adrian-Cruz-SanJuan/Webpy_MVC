import web 
import app 

import application.models.model as alumnos

model_alumnos = alumnos.Alumnos()

render=web.template.render('application/views/alumnos')

class Delete():

    def GET(self, matricula):
      try:
        result = model_alumnos.view(matricula)[0]
        return render.delete(result)
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self, matricula):
      try:
        form = web.input()
        matricula = form['matricula']
        result = model_alumnos.delete(matricula)
        web.seeother('/list')
      except Exception as e:
        print(e)
        return "Error"