import mysql.connector


class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root',
                password='utec',
                host='localhost',
                port=3306,
                database='alumnos'
            )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)
    def select(self):
        try:
            self.connect()
            query = ("SELECT * FROM ALUMNOS;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'matricula':row[1],
                    'nombre':row[2],
                    'primer_a':row[3],
                    'segundo_a':row[4],
                    'edad':row[5],
                    'fecha_nacimiento':row[6],
                    'sexo':row[7],
                    'estado':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    def view(self,matricula):
        try:
            self.connect()
            query = ("SELECT * FROM ALUMNOS WHERE MATRICULA = %s;")
            values = (matricula,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                diccionario = {
                    "id_alumno":row[0],
                    "matricula":row[1],
                    "nombre":row[2],
                    "primer_a":row[3],
                    "segundo_a":row[4],
                    "edad":row[5],
                    "fecha_nacimiento":row[6],
                    "sexo":row[7],
                    "estado":row[8]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)

    def insert(self, matricula, nombre, primer_a, segundo_a, edad, fecha_nacimiento, sexo, estado):
        try:
            self.connect()
            query = ("INSERT INTO ALUMNOS (matricula,nombre,primer_a,segundo_a,edad,fecha_nacimiento,sexo,estado) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula,nombre,primer_a,segundo_a,edad,fecha_nacimiento,sexo,estado)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, matricula):
        try:
            self.connect()
            query = ("DELETE FROM ALUMNOS WHERE matricula= %s;")
            values = (matricula,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, matricula, nombre,primer_a, segundo_a, edad, fecha_nacimiento,sexo,estado):
        try:
            self.connect()
            query = ("UPDATE ALUMNOS SET nombre=%s,primer_a=%s,segundo_a=%s,edad=%s,fecha_nacimiento=%s,sexo=%s,estado=%s WHERE matricula=%s;")
            values = (nombre,primer_a,segundo_a,edad,fecha_nacimiento,sexo,estado,matricula)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Alumnos()
objeto.connect() 
for row in objeto.select():
    print(row)