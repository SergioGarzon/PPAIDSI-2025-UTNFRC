from Domain.Entities.MuestraSismica import MuestraSismica

class SerieTemporal:

    def __init__(self, identificador, condicion_nombre, fecha_hora_inicio_registro_muestra, fecha_hora_registro, frecuencia_muestreo):
        self.identificador = identificador
        self.condicion_nombre = condicion_nombre
        self.fecha_hora_inicio_registro_muestra = fecha_hora_inicio_registro_muestra
        self.fecha_hora_registro = fecha_hora_registro
        self.frecuencia_muestreo = frecuencia_muestreo
        self.muestra_sismica = None
        self.muestra_sismica_lista = []

    def agregar_muestra_sismica(self, muestra):
        self.muestra_sismica = muestra
        self.muestra_sismica_lista.append(self.muestra_sismica)
    
    def get_muestra_sismica(self):
        return self.muestra_sismica_lista

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

    # METODO 37 (Diagrama de secuencia)
    def get_datos(self, datos_sismogafos):  
        
        lista_valor_aux = []

        for data in self.get_muestra_sismica():
            # METODO 38 (Diagrama de secuencia)
            lista_valor_aux.append(data.get_datos())

        lista_aux = [
            self.get_identificador(), 
            self.get_condicion_nombre(), 
            self.get_fecha_hora_inicio_registro_muestra(), 
            self.get_fecha_hora_registro(), 
            self.get_frecuencia_muestreo(),
            lista_valor_aux]     

        self.buscar_estacion_sismologica()   

        return lista_aux