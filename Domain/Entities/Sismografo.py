from Domain.Entities.EstacionSimologica import EstacionSimologica
from Domain.Entities.SerieTemporal import SerieTemporal
from random import randint

class Sismografo:
    
    def __init__(self, nro_serie, identificador_sismografo, fecha_adquisicion
                   , codigo_estacion, documento_certifiacion_adq, fecha_solicitud_certificacion, 
                    latitud, longitud, nombre, nro_certificacion_adquisicion, 
                    identificador, condicion_nombre,
                    fecha_hora_inicio_registro_muestra, fecha_hora_registro, frecuencia_muestreo):
        self.nro_serie = nro_serie
        self.identificador_sismografo = identificador_sismografo
        self.fecha_adquisicion = fecha_adquisicion
        self.estacion_sismologica = EstacionSimologica(codigo_estacion, documento_certifiacion_adq, fecha_solicitud_certificacion, 
                    latitud, longitud, nombre, nro_certificacion_adquisicion)
        self.series_temporal = SerieTemporal(identificador, condicion_nombre,
                    fecha_hora_inicio_registro_muestra, fecha_hora_registro, frecuencia_muestreo)
        self.muestra_sismica = None


    def get_identificacion(self):
        return self.identificador_sismografo
    
    
    def set_estado_actual(self):
        pass

    