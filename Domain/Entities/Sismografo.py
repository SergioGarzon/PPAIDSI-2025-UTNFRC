from Domain.Entities.EstacionSimologica import EstacionSimologica

class Sismografo:

    def __init__(self, nro_serie, identificador_sismografo, fecha_adquisicion
                   , codigo_estacion, documento_certifiacion_adq, fecha_solicitud_certificacion, 
                    latitud, longitud, nombre, nro_certificacion_adquisicion):
        self.nro_serie = nro_serie
        self.identificador_sismografo = identificador_sismografo
        self.fecha_adquisicion = fecha_adquisicion
        self.estacion_sismologica = EstacionSimologica(codigo_estacion, documento_certifiacion_adq, fecha_solicitud_certificacion, 
                    latitud, longitud, nombre, nro_certificacion_adquisicion)

    def get_identificacion(self):
        return self.identificador_sismografo
    
    def set_estado_actual(self):
        pass

    # METODO 41 (Diagrama de secuencia)
    def conocer_sismografo(self):
        # METODO 42, 43 (Diagrama de secuencia)
        return [self.estacion_sismologica.get_codigo_estacion(), self.estacion_sismologica.get_nombre()]
