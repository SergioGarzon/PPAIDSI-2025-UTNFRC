from Domain.Entities.Estado import Estado

class CambioEstado:

    # METODO 29 (Diagrama de secuencia)
    def __init__(self, fecha_hora_inicio, fecha_hora_fin, estado):
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin
        self.estado = estado

    # METODO 26 (Diagrama de secuencia)
    def es_estado_actual(self):
        if self.fecha_hora_fin == "":
            return True
    
        return False
    
    def set_fecha_hora_fin(self, fecha_hora_fin):
        self.fecha_hora_fin = fecha_hora_fin


    ##############################################################################################
    ##### METODOS AUXILIARES PARA MOSTRAR PERO NO ESTAN EN EL DIAGRAMA DE CLASES DE ANALISIS #####
    ##############################################################################################
    def get_fecha_hora_inicio(self):
        return self.fecha_hora_inicio    
    
    def get_fecha_hora_fin(self):
        return self.fecha_hora_fin
            