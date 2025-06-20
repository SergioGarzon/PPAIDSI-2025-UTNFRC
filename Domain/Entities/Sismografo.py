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

    # METODO 41 (Diagrama de secuencia)
    def conocer_sismografo(self):
        
        # METODO 42, 43 (Diagrama de secuencia)
        return [self.lista_sismografos]
    
    
    ############################################################
    ##### METODOS AUXILIARES ###################################
    ############################################################
  
    
    # Metodo para generar datos de sismografos
    def generar_datos_sismografo(self):
        self.lista_sismografos = []
        self.lista_estaciones = []
        self.lista_series = []

        lista_estaciones_aux = [
            [randint(1, 20), randint(0, 400), "2022-11-15 23:00:00", -155.3, 545.5, "No tiene", randint(0, 1100000)],
            [randint(1, 20), randint(0, 400), "2025-11-15 23:00:00", -155.3, 545.5, "No tiene", randint(0, 1100000)],
            [randint(1, 20), randint(0, 400), "2024-11-15 23:00:00", -155.3, 545.5, "No tiene", randint(0, 1100000)]
        ]
        
        for estaciones_datos in lista_estaciones_aux:
            self.estacion_sismologica = EstacionSimologica(*estaciones_datos)
            self.lista_estaciones.append(self.estacion_sismologica)

        lista_series_aux = [
            [1,"Monitoreo Volcánico", "2025-02-10 09:00:00", "2025-02-17 09:00:00", 160],
            [5,"Ejemplo SERIE TEMPORAL", "2025-02-10 09:00:00", "2025-02-17 09:00:00", 160],
            [6,"Monitoreo Volcánico", "2025-02-10 09:00:00", "2025-02-17 09:00:00", 160],
            [7,"Monitoreo Volcánico", "2025-02-10 09:00:00", "2025-02-17 09:00:00", 160],
        ]

        for series_datos in lista_series_aux:
            self.serie_temporal = SerieTemporal(*series_datos)
            self.lista_series.append(self.serie_temporal)
               
        
        lista_sismografos_aux = []

        for puntero in 3:
            lista_sismografos_aux.insert([randint(0, 999999), randint(0, 100), "2024-09-22 12:00:00"], self.lista_estaciones[puntero], self.lista_series[puntero])
            self.sismografos = Sismografo(*lista_sismografos_aux)
            self.lista_sismografos.append(self.sismografos)
        
        
        print("\n\n******************* DATOS SERIES TEMPORALES *******************")
        for lista in self.lista_sismografos:
            print(lista)

        print("\n\n**************************************")


        