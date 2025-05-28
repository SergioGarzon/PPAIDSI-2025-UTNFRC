from Domain.Entities.Usuario import Usuario

class Sesion:

    def __init__(self, identificador_sesion, fecha_hora_inicio_sesion, fecha_hora_fin_sesion, nombre_usuario, contrasenia, nombre_empleado, apellido_empleado, 
                 mail_empleado, telefono_empleado):
        self.identificador_sesion = identificador_sesion
        self.fecha_hora_inicio_sesion = fecha_hora_inicio_sesion
        self.fecha_hora_fin_sesion = fecha_hora_fin_sesion
        self.usuario_actual = Usuario(nombre_usuario, contrasenia, nombre_empleado, apellido_empleado, mail_empleado, telefono_empleado)

    def get_usuario(self):
        return self.usuario_actual
    
    #METODO 4 (Diagrama de secuencia)
    def obtener_empleado(self):
        return self.usuario_actual.obtener_empleado()
    
    
    