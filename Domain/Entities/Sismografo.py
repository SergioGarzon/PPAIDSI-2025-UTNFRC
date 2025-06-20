from Domain.Entities.EstacionSimologica import EstacionSimologica
from random import randint

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
    
    
    ############################################################
    ##### METODOS AUXILIARES ###################################
    ############################################################
  
    
    # Metodo para generar datos de sismografos
    def generar_datos_sismografo(self):
        self.lista_sismografos = []
        lista_sismografos_aux = []

        lista_sismografos_aux = [
            [randint(0, 999999), randint(0, 100), "2024-09-22 12:00:00", randint(1, 20), randint(0, 400), "2022-11-15 23:00:00", -155.3, 545.5, "No tiene", randint(0, 1100000)],
            [randint(0, 999999), randint(0, 100), "2025-01-25 12:00:00", randint(1, 20), randint(0, 400), "2025-11-15 23:00:00", -155.3, 545.5, "No tiene", randint(0, 1100000)],
            [randint(0, 999999), randint(0, 100), "2023-06-12 12:00:00", randint(1, 20), randint(0, 400), "2024-11-15 23:00:00", -155.3, 545.5, "No tiene", randint(0, 1100000)]
        ]

        for sismografos_datos in lista_sismografos_aux:
            self.sismografos = Sismografo(*sismografos_datos)
            self.lista_sismografos.append(self.sismografos)
    
            
    # Metodo para devolver la lista de sismografo
    def retornar_lista(self):
        return self.lista_sismografos
