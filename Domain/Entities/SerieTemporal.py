class SerieTemporal:

    def __init__(self, condicion_nombre, fecha_hora_inicio_registro_muestra, fecha_hora_registro, frecuencia_muestreo):
        self.condicion_nombre = condicion_nombre
        self.fecha_hora_inicio_registro_muestra = fecha_hora_inicio_registro_muestra
        self.fecha_hora_registro = fecha_hora_registro
        self.frecuencia_muestreo = frecuencia_muestreo

    # METODO 36 (Diagrama de secuencia)
    def get_datos(self):

        lista_serie_aux = [
            self.condicion_nombre,
            self.fecha_hora_inicio_registro_muestra, 
            self.fecha_hora_registro,
            self.frecuencia_muestreo
        ]

        return lista_serie_aux 