from Domain.Entities.Estado import Estado

class CambioEstado:

    def __init__(self, fecha_hora_inicio, fecha_hora_fin, ambito, nombre_estado):
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin
        self.estado = Estado(ambito, nombre_estado)

    def es_estado_actual(self):
        if self.fecha_hora_fin == None:
            pass
    
    def set_fecha_hora_fin(self, fecha_hora_fin):
        self.fecha_hora_fin = fecha_hora_fin
            