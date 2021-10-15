""" Importamos la libreria de base de datos"""
import mysql.connector
""" Creamos una clase para las operaciones del inventario"""
class Articulos:
    """ Metodo que permite abrir una conexion a la base de datos de inventario en AWS"""
    """ AWS es un servicio de amazon, que nos permite tener bases de datos o maquinas virtuales en la nube"""
    def abrir(self):
        conexion = mysql.connector.connect(host="proyectointegrador.cjzvbkkw3p9t.us-east-2.rds.amazonaws.com",
                                           user="alexia",
                                           passwd="vekMTpwupe-458",
                                           database="ProyectoIntegrador")
        return conexion
    """ Metodo que toma los datos del formulario y los agrega a la base de datos de inventario """
    def alta(self, datos):
        """ Abrimos la conexion a la base de datos"""
        cone = self.abrir()
        """ Creamos un puntero para indicar donde escribiremos nuestros datos en la base de datos"""
        cursor = cone.cursor()
        """ Hacemos un comando de base de datos agregandole los datos de nuestra lista"""
        sql = "insert into inventario(modelo,nombre, precio,cantidad) values (%s,%s,%s,%s)"
        """ Ejecutamos el comando en la base de datos, tomando como valores los datos del formulario """
        cursor.execute(sql, datos)
        """ Validamos que los cambios se hayan realizado en la base de datos"""
        cone.commit()
        """ Cerramos la conexion a la base de datos"""
        cone.close()


    """ Metodo que toma los datos del formulario de ventas y los agrega a la base de datos de ventas """
    def altav(self, datos):
        """ Abrimos la conexion a la base de datos"""
        cone = self.abrir()
        """ Creamos un puntero para indicar donde escribiremos nuestros datos en la base de datos"""
        cursor = cone.cursor()
        """ Hacemos un comando de base de datos agregandole los datos de nuestra lista"""
        sql = "insert into ventas(cantidad,vendedor,fecha,modelo) values (%s,%s,curdate(),%s)"
        """ Ejecutamos el comando en la base de datos, tomando como valores los datos del formulario """
        cursor.execute(sql, datos)
        """ Validamos que los cambios se hayan realizado en la base de datos"""
        cone.commit()
        """ Cerramos la conexion a la base de datos"""
        cone.close()



    """ Metodo que nos permite obtener todos los datos de las ventas de un producto en especifico """
    def generarRVM(self, datos):
        """ Abrimos la conexion a la base de datos"""
        cone = self.abrir()
        """ Creamos un puntero para indicar donde escribiremos nuestros datos en la base de datos"""
        cursor = cone.cursor()
        """ Ejecutamos el comando en la base de datos, tomando como valores los datos del formulario """
        sql = "select modelo, cantidad,vendedor from ventas where modelo=%s"
        """ Cerramos la conexion a la base de datos"""
        cursor.execute(sql, datos)
        """ Cerramos la conexion a la base de datos"""
        cone.close()
        """ Cerramos la conexion a la base de datos"""
        return cursor.fetchall()

    """ Metodo que nos permite obtener todos los datos de las ventas de un vendedor en especifico """
    def generarRVV(self, datos):
        """ Abrimos la conexion a la base de datos"""
        cone = self.abrir()
        """ Creamos un puntero para indicar donde escribiremos nuestros datos en la base de datos"""
        cursor = cone.cursor()
        """ Ejecutamos el comando en la base de datos, tomando como valores los datos del formulario """
        sql = "select modelo, cantidad,vendedor from ventas where vendedor=%s"
        """ Cerramos la conexion a la base de datos"""
        cursor.execute(sql, datos)
        """ Cerramos la conexion a la base de datos"""
        cone.close()
        """ Cerramos la conexion a la base de datos"""
        return cursor.fetchall()

    """ Metodo que nos permite obtener todos los datos del inventario """
    def recuperar_todos(self):
        """ Abrimos la conexion a la base de datos"""
        cone = self.abrir()
        """ Creamos un puntero para indicar donde escribiremos nuestros datos en la base de datos"""
        cursor = cone.cursor()
        """ Ejecutamos el comando en la base de datos, tomando como valores los datos del formulario """
        sql = "select modelo,nombre, precio, cantidad from inventario"
        cursor.execute(sql)
        """ Cerramos la conexion a la base de datos"""
        cone.close()
        """ Devuelve una lista con los daots de todos los productos del inventario """
        return cursor.fetchall()

    """ Metodo que nos permite obtener todos los datos del inventario de todas las ventas"""
    def recuperar_ventas(self):
        """ Abrimos la conexion a la base de datos"""
        cone = self.abrir()
        """ Creamos un puntero para indicar donde escribiremos nuestros datos en la base de datos"""
        cursor = cone.cursor()
        """ Ejecutamos el comando en la base de datos, tomando como valores los datos del formulario """
        sql = "select modelo,cantidad, vendedor from ventas"
        cursor.execute(sql)
        """ Cerramos la conexion a la base de datos"""
        cone.close()
        """ Devuelve una lista con los daots de todos los productos del inventario """
        return cursor.fetchall()

    """ Metodo que nos permite validar que la cantidad en inventario es mayor a la cantidad a vender """
    def validar_inventario(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select cantidad from inventario where modelo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    """ Metodo que nos permite restar la cantidad de la venta a la cantidad en inventario"""
    def actualizar_inventario(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "update inventario set cantidad=%s where modelo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount
