from Domain.Entities.MuestraSismica import MuestraSismica
from Domain.Entities.Sismografo import Sismografo
from random import randint

class SerieTemporal:

    def __init__(self, condicion_nombre, fecha_hora_inicio_registro_muestra, fecha_hora_registro, frecuencia_muestreo):
        self.condicion_nombre = condicion_nombre
        self.fecha_hora_inicio_registro_muestra = fecha_hora_inicio_registro_muestra
        self.fecha_hora_registro = fecha_hora_registro
        self.frecuencia_muestreo = frecuencia_muestreo
        self.muestra_sismica = None

    # METODO 35 (Diagrama de secuencia)
    def get_datos(self):  
        self.generar_muestras_sismicas()
        
        datos = []

        for lista in self.lista_muestra_sism:
            # METODO 36 (Diagrama de secuencia)
            datos.append(lista.get_datos())

        self.buscar_estacion_sismologica()

        return [self.condicion_nombre, self.fecha_hora_inicio_registro_muestra, 
                self.fecha_hora_registro, self.frecuencia_muestreo, datos, self.sismografo.conocer_sismografo()] # METODO 41 (Diagrama de secuencia)
    

    # METODO 40 (Diagrama de secuencia)
    def buscar_estacion_sismologica(self):        
        self.sismografo = Sismografo(randint(0, 999999), randint(0, 100), "2024-09-22 12:00:00", 1, randint(0, 400), "2022-11-15 23:00:00", -155.3, 545.5, "No tiene", randint(0, 1100000))


    ############################################################
    ##### METODOS AUXILIARES ###################################
    ############################################################

    def generar_muestras_sismicas(self):

        self.lista_muestra_sism = []

        lista_aux = [
            ["2025-03-11 07:02:20"],
            ["2025-02-24 10:22:42"],
            ["2025-10-02 13:15:55"],
            ["2025-02-12 03:24:20"]
        ]

        for datos_msismica in lista_aux:
            self.muestra_sismica = MuestraSismica(*datos_msismica)
            self.lista_muestra_sism.append(self.muestra_sismica)  