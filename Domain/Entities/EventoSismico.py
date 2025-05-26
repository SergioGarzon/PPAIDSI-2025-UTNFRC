from Domain.Entities.Estado import Estado
from datetime import datetime

class EventoSismico:
    
    def __init__(self, fecha_hora_fin, fecha_hora_ocurrencia, latitud_epicentro, latitud_hipocentro, 
                 longitud_epicentro, longitud_hipocentro, valor_magnitud, ambito, nombre_estado):
        self.fecha_hora_fin = datetime.strptime(fecha_hora_fin, "%Y-%m-%d %H:%M:%S")
        self.fecha_hora_ocurrencia = datetime.strptime(fecha_hora_ocurrencia, "%Y-%m-%d %H:%M:%S")
        self.latitud_epicentro = latitud_epicentro
        self.latitud_hipocentro = latitud_hipocentro
        self.longitud_epicentro = longitud_epicentro
        self.longitud_hipocentro = longitud_hipocentro
        self.valor_magnitud = valor_magnitud
        self.estado_actual = Estado(ambito, nombre_estado)
    
    def get_fecha_hora_ocurrencia(self):
        return self.fecha_hora_ocurrencia
    
    def get_fecha_hora_fin(self):
        return self.fecha_hora_fin
    
    def get_latitud_epicentro(self):
        return self.longitud_hipocentro

    def get_latitud_hipocentro(self):
        return self.latitud_hipocentro
    
    def get_longitud_epicentro(self):
        return self.longitud_epicentro
    
    def get_longitud_hipocentro(self):
        return self.longitud_hipocentro
    
    def get_valor_magnitud(self):
        return self.valor_magnitud
    
    def es_pendiente_revision(self):
        valor = False

        if(self.estado_actual.get_nombre_estado() == 'Pendiente en revision'):
            valor = True  

        return valor    
    
    def set_estado_actual(self, nuevo_estado):
        if isinstance(nuevo_estado, Estado):
            self.estado_actual = nuevo_estado
        else:
            raise TypeError("Error")

    def es_ambito_evento_sismico(self):        
        if(self.estado_actual.get_ambito() == 'Evento Sismico'):
            return True
        return False  
    
    def get_datos_restantes():
        pass
    
