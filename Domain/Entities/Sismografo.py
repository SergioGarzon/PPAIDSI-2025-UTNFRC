from Domain.Entities.EstacionSimologica import EstacionSimologica
from Domain.Entities.SerieTemporal import SerieTemporal
from random import randint

class Sismografo:
    
    def __init__(self, nro_serie, identificador_sismografo, fecha_adquisicion
                   , codigo_estacion, documento_certifiacion_adq, fecha_solicitud_certificacion, 
                    latitud, longitud, nombre, nro_certificacion_adquisicion):
        self.nro_serie = nro_serie
        self.identificador_sismografo = identificador_sismografo
        self.fecha_adquisicion = fecha_adquisicion
        self.estacion_sismologica = EstacionSimologica(codigo_estacion, documento_certifiacion_adq, fecha_solicitud_certificacion, 
                    latitud, longitud, nombre, nro_certificacion_adquisicion)
        self.series_temporal = []       

    def get_identificacion(self):
        return self.identificador_sismografo
    
    def get_nro_serie(self):
        return self.nro_serie
    
    def get_fecha_adquisicion(self):
        return self.fecha_adquisicion
    
    def get_estacion_sismologica(self):
        return self.estacion_sismologica

    def agregar_serie_temporal(self, serie_temp):
        self.serie_temporal = serie_temp

    def set_estado_actual(self):
        pass  