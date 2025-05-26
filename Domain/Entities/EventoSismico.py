from Domain.Entities.Estado import Estado
from Domain.Entities.AlcanceSismo import AlcanceSismo
from Domain.Entities.OrigenDeGeneracion import OrigenDeGeneracion
from Domain.Entities.ClasificacionSismo import ClasificacionSismo
from datetime import datetime

class EventoSismico:
    
    def __init__(self, fecha_hora_fin, fecha_hora_ocurrencia, latitud_epicentro, latitud_hipocentro, 
                 longitud_epicentro, longitud_hipocentro, valor_magnitud, ambito, nombre_estado,
                 nombre_alcance, descripcion_alcance,
                 nombre_origen_generacion, descripcion_origen_generacion,
                 nombre_clasificacion_sismo, kilometro_profundidad_desde, kilometro_profundidad_hasta):
        self.fecha_hora_fin = datetime.strptime(fecha_hora_fin, "%Y-%m-%d %H:%M:%S")
        self.fecha_hora_ocurrencia = datetime.strptime(fecha_hora_ocurrencia, "%Y-%m-%d %H:%M:%S")
        self.latitud_epicentro = latitud_epicentro
        self.latitud_hipocentro = latitud_hipocentro
        self.longitud_epicentro = longitud_epicentro
        self.longitud_hipocentro = longitud_hipocentro
        self.valor_magnitud = valor_magnitud
        self.estado_actual = Estado(ambito, nombre_estado)
        self.alcance_sismo = AlcanceSismo(nombre_alcance, descripcion_alcance)
        self.generacion_sismo = OrigenDeGeneracion(nombre_origen_generacion, descripcion_origen_generacion)
        self.clasificacion_sismo = ClasificacionSismo(nombre_clasificacion_sismo, kilometro_profundidad_desde, kilometro_profundidad_hasta)
    
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
    
    # DATOS RESTANTES PARA BUSCAR TODOS
    def get_datos_restante(self):
        return AlcanceSismo.get_nombre() + OrigenDeGeneracion.get_nombre() + ClasificacionSismo.get_nombre()
    
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
    
    def obtener_datos_series_temporales():
        pass
    
