from Domain.Entities.Estado import Estado

class CambioEstado:

    def __init__(self, fecha_hora_inicio, fecha_hora_fin, estado):
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin
        self.estado = estado

    def get_fecha_hora_inicio(self):
        return self.fecha_hora_inicio    
    
    def get_fecha_hora_fin(self):
        return self.fecha_hora_fin
    
    def get_estado(self):
        return self.estado

    # METODO 26 (Diagrama de secuencia)
    def es_estado_actual(self):
        return self.fecha_hora_fin == ""

    # METODO 27, 65 (Diagrama de secuencia)
    def set_fecha_hora_fin(self, fecha_hora_fin):
        self.fecha_hora_fin = fecha_hora_fin
            
            