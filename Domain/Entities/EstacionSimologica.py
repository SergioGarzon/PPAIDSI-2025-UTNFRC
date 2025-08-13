class EstacionSimologica:

    def __init__(self, codigo_estacion, documento_certifiacion_adq, 
                 fecha_solicitud_certificacion, latitud, longitud, nombre, nro_certificacion_adquisicion):
        self.codigo_estacion = codigo_estacion
        self.documento_certifiacion_adq = documento_certifiacion_adq
        self.fecha_solicitud_certificacion = fecha_solicitud_certificacion
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre
        self.nro_certificacion_adquisicion = nro_certificacion_adquisicion

    def get_nombre(self):
        return self.nombre
    
    def get_codigo_estacion(self):
        return self.codigo_estacion

    def get_documento_certifiacion_adq(self):
        return self.documento_certifiacion_adq
    
    def get_fecha_solicitud_certificacion(self):
        return self.fecha_solicitud_certificacion

    def get_latitud(self):
        return self.latitud
    
    def get_longitud(self):
        return self.longitud
    
    def get_nombre(self):
        return self.nombre
    
    def get_nro_certificacion_adquisicion(self):
        return self.nro_certificacion_adquisicion