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

        lista_sismografo = []

        # METODO 41 (Diagrama de secuencia) 
        lista_sismografo = self.buscar_estacion_sismologica(datos_sismogafos)

        lista_aux = [
            self.get_identificador(), 
            self.get_condicion_nombre(), 
            self.get_fecha_hora_inicio_registro_muestra(), 
            self.get_fecha_hora_registro(), 
            self.get_frecuencia_muestreo(),
            lista_valor_aux, 
            lista_sismografo]     
         
        return lista_aux
    
    # METODO 41 (Diagrama de secuencia) 
    def buscar_estacion_sismologica(self, datos_sismogafos):
        
        lista_dsi = []

        # Aca se recorre entonces los sismografos para saber si tienen la misma
        # serie temporal
        for sism in datos_sismogafos:            
            for setmp_lista in sism.get_serie_temporal():
                if (setmp_lista.get_identificador() == self.get_identificador()):                    
                    lista_dsi.append(sism.get_datos()) 

        return lista_dsi