import mysql.connector


class ConexionMySQL:

    def __init__(self, local: bool = False):
        if local:
            self.MYSQL_HOST = "localhost"
            self.MYSQL_USER = "root"
            self.MYSQL_PASSWORD = "DoItRodriguez"
            self.MYSQL_DATABASE = "itjalumnos"
            self.MYSQL_CONNECTION = None
            self.MYSQL_CURSOR = None
        else:
            self.MYSQL_HOST = "b4zqeb08si5mnzd7sfro-mysql.services.clever-cloud.com"
            self.MYSQL_USER = "uw80gdenbynhciqh"
            self.MYSQL_PASSWORD = "w5tCBZ2Etekv0IFbSNbC"
            self.MYSQL_DATABASE = "b4zqeb08si5mnzd7sfro"
            self.MYSQL_CONNECTION = None
            self.MYSQL_CURSOR = None

    def conectar_mysql(self):
        conecto = False
        try:
            self.MYSQL_CONNECTION = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD,
                database=self.MYSQL_DATABASE,
                auth_plugin='mysql_native_password')
            conecto = self.MYSQL_CONNECTION is not None
        except Exception as error:
            print("Error al conectar: ", error)
        return conecto

    def desconectar_mysql(self):
        if self.MYSQL_CONNECTION is not None:
            self.MYSQL_CONNECTION.close()
            self.MYSQL_CONNECTION = None

    def consulta_sql(self, sql):
        resultado = []
        if self.conectar_mysql():
            try:
                self.MYSQL_CURSOR = self.MYSQL_CONNECTION.cursor()
                self.MYSQL_CURSOR.execute(sql)

                for reg in self.MYSQL_CURSOR:
                    resultado.append(reg)

                self.MYSQL_CONNECTION.commit()
                self.MYSQL_CURSOR.close()
                self.desconectar_mysql()
            except Exception as error:
                print("Error en la consulta: ", error)
        return resultado
