from Domain.Entities.Empleado import Empleado

class Usuario:
    
    def __init__(self, nombre_usuario, contrasenia):
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.empleado = None

    #METODO 5 (Diagrama de secuencia)
    def obtener_empleado(self):
        self.empleado = Empleado("Pablo", "Paez", "ppaez@sismos-conicet.com.ar", 351000000)
        return (self.empleado)
    
    def getRILogueado(self):
        return self.nombre_usuario + ", logueado con exito!"