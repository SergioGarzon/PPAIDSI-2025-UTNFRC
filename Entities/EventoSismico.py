class EventoSismico:
    
    def __init__(self, fecha_hora_fin, fecha_hora_ocurrencia, latitud_epicentro, latitud_hipocentro, 
                 longitud_epicentro, longitud_hipocentro, valor_magnitud):
        self.fecha_hora_fin = fecha_hora_fin
        self.fecha_hora_ocurrencia = fecha_hora_ocurrencia
        self.latitud_epicentro = latitud_epicentro
        self.latitud_hipocentro = latitud_hipocentro
        self.longitud_epicentro = longitud_epicentro
        self.longitud_hipocentro = longitud_hipocentro
        self.valor_magnitud = valor_magnitud
    
    def get_fecha_hora_ocurrencia(self):
        return self.fecha_hora_ocurrencia
    
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
    
    def es_pendiente_revision():
        d