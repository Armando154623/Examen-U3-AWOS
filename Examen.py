import json

from ConexionMySQL import ConexionMySQL


def ejercicio_1():
    nocontrol = input("Ingrese un numero de control")
    if len(nocontrol) == 0:
        # Cadena vacia
        print("Numero de control no valido")
        return

    obj = ConexionMySQL()
    sql = f"select exists(select * from alumnos where NoControl = '{nocontrol}')"
    res = obj.consulta_sql(sql)
    if res[0][0] == 0:
        # No existe
        print("El estudiante no existe")
        return

    sql = f"select Nombre from alumnos where NoControl = '{nocontrol}'"
    res = obj.consulta_sql(sql)
    nombre = res[0][0]

    sql = f"select Materia, Calificacion from kardex where NoControl = {nocontrol}"
    res = obj.consulta_sql(sql)
    materias = []
    for materia, calificacion in res:
        materias.append({"Materia": materia, "Calificacion": float(calificacion)})

    dic = {"Nombre": nombre, "Materias": materias}
    print(json.dumps(dic))






ejercicio_1()
