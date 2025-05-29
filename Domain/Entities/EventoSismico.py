from Domain.Entities.Estado import Estado
from Domain.Entities.AlcanceSismo import AlcanceSismo
from Domain.Entities.OrigenDeGeneracion import OrigenDeGeneracion
from Domain.Entities.ClasificacionSismo import ClasificacionSismo
from Domain.Entities.SerieTemporal import SerieTemporal
from Domain.Entities.CambioEstado import CambioEstado
from Domain.Entities.Sismografo import Sismografo
from datetime import datetime

class EventoSismico:
    
    def __init__(self, fecha_hora_ocurrencia, fecha_hora_fin, latitud_epicentro, latitud_hipocentro, 
                 longitud_epicentro, longitud_hipocentro, valor_magnitud, ambito, nombre_estado,
                 nombre_alcance, descripcion_alcance,
                 nombre_origen_generacion, descripcion_origen_generacion,
                 nombre_clasificacion_sismo, kilometro_profundidad_desde, kilometro_profundidad_hasta):        
        self.fecha_hora_ocurrencia = datetime.strptime(fecha_hora_ocurrencia, "%Y-%m-%d %H:%M:%S")
        self.fecha_hora_fin = datetime.strptime(fecha_hora_fin, "%Y-%m-%d %H:%M:%S")        
        self.latitud_epicentro = latitud_epicentro
        self.latitud_hipocentro = latitud_hipocentro
        self.longitud_epicentro = longitud_epicentro
        self.longitud_hipocentro = longitud_hipocentro
        self.valor_magnitud = valor_magnitud
        self.estado_actual = Estado(ambito, nombre_estado)
        self.alcance_sismo = AlcanceSismo(nombre_alcance, descripcion_alcance)
        self.generacion_sismo = OrigenDeGeneracion(nombre_origen_generacion, descripcion_origen_generacion)
        self.clasificacion_sismo = ClasificacionSismo(nombre_clasificacion_sismo, kilometro_profundidad_desde, kilometro_profundidad_hasta)
        self.serie_temporal = None
        self.cambio_estado_bloq_rev = None

    
    # METODO 9 (Diagrama de secuencia)
    def get_fecha_hora_ocurrencia(self):
        return self.fecha_hora_ocurrencia
    
    def get_fecha_hora_fin(self):
        return self.fecha_hora_fin
    
    # METODO 10 (Diagrama de secuencia) 
    def get_latitud_epicentro(self):
        return self.longitud_hipocentro

    # METODO 11 (Diagrama de secuencia) 
    def get_latitud_hipocentro(self):
        return self.latitud_hipocentro
    
    # METODO 12 (Diagrama de secuencia)
    def get_longitud_epicentro(self):
        return self.longitud_epicentro
    
    # METODO 13 (Diagrama de secuencia)
    def get_longitud_hipocentro(self):
        return self.longitud_hipocentro
    
    # METODO 14 (Diagrama de secuencia)
    def get_valor_magnitud(self):
        return self.valor_magnitud
    
    # METODO 7 (Diagrama de secuencia)
    def es_pendiente_revision(self):
        valor = False

        if self.estado_actual.es_pendiente_revision() :
            valor = True  

        return valor    
    
    # METODO 24 (Diagrama de secuencia)
    def bloquear_evento(self, nuevo_estado, fecha_hora_actual):
        if isinstance(nuevo_estado, Estado):
            self.estado_actual = nuevo_estado # Aqui setea al estado actual el evento sismico seleccionado
            self.fecha_hora_seteo = fecha_hora_actual
            self.buscar_estado_actual()
        else:
            raise TypeError("Error")

    # METODO 25 (Diagrama de secuencia)
    def buscar_estado_actual(self):
        
        self.cambio_estado = None

        self.generar_datos_cambio_estados()

        for lista in self.lista_cambio_estado:
            # METODO 26 (Diagrama de secuencia)
            if lista.es_estado_actual():                
                self.cambio_estado = lista
        
        # METODO 27 (Diagrama de secuencia) 
        self.set_fecha_hora_fin()
        # METODO 28 (Diagrama de secuencia)
        self.crear_cambio_estado()

    # METODO 27 (Diagrama de secuencia)
    def set_fecha_hora_fin(self):        
        self.cambio_estado.set_fecha_hora_fin(self.fecha_hora_seteo.strftime("%Y-%m-%d %H:%M:%S"))

    # METODO 28 (Diagrama de secuencia)
    def crear_cambio_estado(self):        
        new_cambio_estado = CambioEstado(self.fecha_hora_seteo.strftime("%Y-%m-%d %H:%M:%S"), "", self.estado_actual)
        self.lista_cambio_estado.append(new_cambio_estado)
        
    # METODO 30 (Diagrama de secuencia)
    def get_datos_restante(self):
        # METODO 31, 32, 33 (Diagrama de secuencia)
        datos = [
            self.alcance_sismo.get_nombre(), 
            self.generacion_sismo.get_nombre(), 
            self.clasificacion_sismo.get_nombre()
        ]

        # METODO 34 (Diagrama de secuencia)
        lista_devuelta = self.obtener_datos_series_temporales()  
        datos.append(lista_devuelta)
        
        return datos
    
    # METODO 34 (Diagrama de secuencia)
    def obtener_datos_series_temporales(self):
               
        self.generar_datos_series_temporales()

        lista_stemp_aux = []

        for lista in self.lista_serie_temp:
            # METODO 35 (Diagrama de secuencia)
            lista_stemp_aux.append(lista.get_datos())

        
        print("Llega aca para obtener datos de las series temporales")
        return lista_stemp_aux
        

    ############################################################
    ##### METODOS AUXILIARES ###################################
    ############################################################
    
    def generar_datos_cambio_estados(self):

        self.lista_cambio_estado = []
        
        lista_aux = [
            ["2025-07-15 09:30:10", "2025-07-20 11:45:00", self.estado_actual],
            ["2025-02-28 21:05:45", "2025-03-05 10:00:00", self.estado_actual],
            ["2025-11-03 14:18:22", "2025-11-08 16:30:00",self.estado_actual],
            ["2025-04-01 06:50:07", "", self.estado_actual]
        ]

        for datos_cestado in lista_aux:
            self.cambio_estado = CambioEstado(*datos_cestado)
            self.lista_cambio_estado.append(self.cambio_estado)       
    
    
    def generar_datos_series_temporales(self):
    
        self.lista_serie_temp = []

        lista_aux_serie = [            
            ["Monitoreo Volcánico", "2025-02-10 09:00:00", "2025-02-17 09:00:00", 160],
            ["Pequeño Enjambre Sísmico", "2025-12-01 03:00:00", "2025-12-02 03:00:00", 200],
            ["Sismo Distante", "2025-07-01 15:00:00", "2025-07-01 17:00:00", 100],
            ["Actividad Diaria Normal", "2025-02-28 21:05:45", "2025-03-05 10:00:00", 50]
        ]

        for datos_stemporales in lista_aux_serie:
            self.serie_temporal = SerieTemporal(*datos_stemporales)
            self.lista_serie_temp.append(self.serie_temporal)



    



    
    
