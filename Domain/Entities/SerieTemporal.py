from Domain.Entities.MuestraSismica import MuestraSismica
from Domain.Entities.Sismografo import Sismografo


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

        # METODO 40 (Diagrama de secuencia)
        self.buscar_estacion_sismologica()

        return [self.condicion_nombre, self.fecha_hora_inicio_registro_muestra, 
                self.fecha_hora_registro, self.frecuencia_muestreo, datos] # METODO 41 (Diagrama de secuencia) , self.sismografo.conocer_sismografo()
    

    # METODO 40 (Diagrama de secuencia)
    def buscar_estacion_sismologica(self): 
        Sismografo.generar_datos_sismografo(self)       
        lista = Sismografo.retornar_lista(self)

        for l in lista:
            print(l)




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