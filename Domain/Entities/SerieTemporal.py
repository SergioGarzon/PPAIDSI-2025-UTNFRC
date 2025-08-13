from Domain.Entities.MuestraSismica import MuestraSismica

class SerieTemporal:

    def __init__(self, identificador, condicion_nombre, fecha_hora_inicio_registro_muestra, fecha_hora_registro, frecuencia_muestreo):
        self.identificador = identificador
        self.condicion_nombre = condicion_nombre
        self.fecha_hora_inicio_registro_muestra = fecha_hora_inicio_registro_muestra
        self.fecha_hora_registro = fecha_hora_registro
        self.frecuencia_muestreo = frecuencia_muestreo
        self.muestra_sismica = []

    def agregar_muestra_sismica(self, muestra):
        self.muestra_sismica.append(muestra)

    def get_identificador(self):
        return self.identificador
    
    def get_condicion_nombre(self):
        return self.condicion_nombre

    def get_fecha_hora_inicio_registro_muestra(self):
        return self.fecha_hora_inicio_registro_muestra

    def get_fecha_hora_registro(self):
        return self.fecha_hora_registro
    
    def get_frecuencia_muestreo(self):
        return self.frecuencia_muestreo
