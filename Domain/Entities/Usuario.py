class Usuario:
    
    def __init__(self, nombre_usuario, contrasenia, empleado=None):
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.empleado = empleado

    def obtener_empleado(self):
        return self.empleado
    
    def getRILogueado(self):
        return self.nombre_usuario + ", logueado con exito!"