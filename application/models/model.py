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

objeto = Alumnos()
objeto.connect() 
for row in objeto.select():
    print(row)