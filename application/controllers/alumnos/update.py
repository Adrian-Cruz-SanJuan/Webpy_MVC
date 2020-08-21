import web 
import app 

import application.models.model as alumnos

model_alumnos = alumnos.Alumnos()

render=web.template.render('application/views/alumnos')

class Update():

    def GET(self, matricula):
      try:
        result = model_alumnos.view(matricula)[0]
        return render.update(result)
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self, matricula):
        try:
            form = web.input()
            matricula = form.matricula
            nombre = form.name
            primer_a = form.primer_a
            segundo = form.segundo_a
            edad = form.edad
            fecha_nacimiento = form.fecha_nacimiento
            sexo = form.sexo
            estado = form.estado
            result = model_alumnos.update(matricula,nombre,primer_a,segundo_a,edad,fecha_nacimiento,sexo,estado)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"