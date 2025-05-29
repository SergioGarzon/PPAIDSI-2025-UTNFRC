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

    # METODO 43 (Diagrama de secuencia)
    def get_nombre(self):
        return self.nombre
    
    # METODO 42 (Diagrama de secuencia)
    def get_codigo_estacion(self):
        return self.codigo_estacion