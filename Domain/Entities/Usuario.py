from Domain.Entities.Empleado import Empleado

class Usuario:
    
    def __init__(self, nombre_usuario, contrasenia, nombre_empleado, apellido_empleado, 
                 mail_empleado, telefono_empleado):
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.empleado = Empleado(nombre_empleado, apellido_empleado, mail_empleado, telefono_empleado)

    #METODO 5 (Diagrama de secuencia)
    def obtener_empleado(self):
        return (str(self.empleado.get_nombre()))
    
    def getRILogueado(self):
        return self.nombre_usuario + ", logueado con exito!"