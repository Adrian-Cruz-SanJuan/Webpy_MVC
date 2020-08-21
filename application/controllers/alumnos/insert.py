import web 
import app 
import application.models.model as alumnos

model_alumnos = alumnos.Alumnos()
render=web.template.render('application/views/alumnos/')

class Insert():

    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self):
      try:
        form = web.input()
        matricula = form.matricula
        nombre = form.nombre
        primer_a = form.primer_a
        segundo_a = form.segundo_a
        edad = form.edad
        fecha_nacimiento = form.fecha_nacimiento
        sexo = form.sexo
        estado = form.estado
        model_alumnos.insert(matricula,nombre,primer_a,segundo_a,edad,fecha_nacimiento,sexo,estado)
        web.seeother('/list')
      except Exception as e:
        print(e)
        return render.insert()