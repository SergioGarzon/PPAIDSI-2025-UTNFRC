from Domain.Entities.Estado import Estado
from Domain.Entities.AlcanceSismo import AlcanceSismo
from Domain.Entities.OrigenDeGeneracion import OrigenDeGeneracion
from Domain.Entities.ClasificacionSismo import ClasificacionSismo
from Domain.Entities.SerieTemporal import SerieTemporal
from Domain.Entities.CambioEstado import CambioEstado
from datetime import datetime

class EventoSismico:
    
    def __init__(self, fecha_hora_ocurrencia, fecha_hora_fin, latitud_epicentro, latitud_hipocentro, 
                 longitud_epicentro, longitud_hipocentro, valor_magnitud, ambito, nombre_estado,
                 nombre_alcance, descripcion_alcance,
                 nombre_origen_generacion, descripcion_origen_generacion,
                 nombre_clasificacion_sismo, kilometro_profundidad_desde, kilometro_profundidad_hasta):        
        self.fecha_hora_ocurrencia = datetime.strptime(fecha_hora_ocurrencia, "%Y-%m-%d %H:%M:%S")
        self.fecha_hora_fin = datetime.strptime(fecha_hora_fin, "%Y-%m-%d %H:%M:%S")        
        self.latitud_epicentro = latitud_epicentro
        self.latitud_hipocentro = latitud_hipocentro
        self.longitud_epicentro = longitud_epicentro
        self.longitud_hipocentro = longitud_hipocentro
        self.valor_magnitud = valor_magnitud
        self.estado_actual = Estado(ambito, nombre_estado)
        self.alcance_sismo = AlcanceSismo(nombre_alcance, descripcion_alcance)
        self.generacion_sismo = OrigenDeGeneracion(nombre_origen_generacion, descripcion_origen_generacion)
        self.clasificacion_sismo = ClasificacionSismo(nombre_clasificacion_sismo, kilometro_profundidad_desde, kilometro_profundidad_hasta)
        self.serie_temporal = None
        self.cambio_estado_bloq_rev = None

    
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
    
    
    



    
    
