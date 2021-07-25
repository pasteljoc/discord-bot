from datetime import datetime

import sqlite3

class Santoral:
    def __init__(self,dbPath):
        self.dbPath=dbPath

    def saludaSanto(self,fecha):
        fecha=datetime.now() if fecha == None else fecha
        conn=sqlite3.connect(self.dbPath)
        cursor=conn.cursor()
        try:
            sqlqry=f"SELECT santo FROM santoral WHERE mes = {fecha.month} AND dia = {fecha.day}"
            cursor.execute(sqlqry)
            santo=cursor.fetchall()[0][0]

            message=f"El santoral del día de hoy saluda a {santo}. Muchas felicidades!"
            return message

        except AttributeError:
            print("Error: Se requiere un argumento de tipo 'datetime.datetime'")
            return "Error fueron cometidos"

        finally:
            cursor.close()
            conn.close()
