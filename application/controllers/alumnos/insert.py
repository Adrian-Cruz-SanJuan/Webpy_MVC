import web 
import app 

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
        print(form)
        print(form.matricula)
        print(form.nombre)
        print(form.primer_a)
        print(form.segundo_a)
        print(form.edad)
        print(form.fecha_nacimiento)
        print(form.sexo)
        print(form.estado)
        return render.insert()
      except Exception as e:
        return "Error en el registro" + str(e.args)