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
        self.serie_temporal = None 
        self.serie_temporal_lista = []   

    def get_identificacion(self):
        return self.identificador_sismografo
    
    def get_nro_serie(self):
        return self.nro_serie
    
    def get_fecha_adquisicion(self):
        return self.fecha_adquisicion
    
    def get_estacion_sismologica(self):
        return self.estacion_sismologica

    def set_estado_actual(self):
        pass  

    def set_serie_temporal(self, serie):
        self.serie_temporal = serie
        self.serie_temporal_lista.append(self.serie_temporal)
    
    def get_serie_temporal(self):
        return self.serie_temporal_lista

    # METODO 42 (Diagrama de secuencia) 
    def get_datos(self):
        # METODO 43, 44 (Diagrama de secuencia) 
        return [self.get_estacion_sismologica().get_codigo_estacion(), self.get_estacion_sismologica().get_nombre()]