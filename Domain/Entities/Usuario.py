from Domain.Entities.Empleado import Empleado

class Usuario:
    
    def __init__(self, nombre_usuario, contrasenia, nombre, apellido, mail, telefono):
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.empleado = Empleado(nombre, apellido, mail, telefono)

    #METODO 5 (Diagrama de secuencia)
    def obtener_empleado(self):
        return (self.empleado)
    
    def getRILogueado(self):
        return self.nombre_usuario + ", logueado con exito!"