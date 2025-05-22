class Sesion:

    def __init__(self, fecha_hora_fin_sesion, fecha_hora_inicio_sesion, identificador_sesion, usuario=None):
        self.fecha_hora_fin_sesion = fecha_hora_fin_sesion
        self.fecha_hora_inicio_sesion = fecha_hora_inicio_sesion
        self.identificador_sesion = identificador_sesion
        self.usuario_actual = usuario

    def get_usuario(self):
        return self.usuario_actual
    
    
    