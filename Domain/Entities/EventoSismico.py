from Domain.Entities.Estado import Estado
from Domain.Entities.AlcanceSismo import AlcanceSismo
from Domain.Entities.OrigenDeGeneracion import OrigenDeGeneracion
from Domain.Entities.ClasificacionSismo import ClasificacionSismo
from Domain.Entities.CambioEstado import CambioEstado
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

        if(self.estado_actual.es_pendiente_revision() == 'Pendiente de revision'):
            valor = True  

        return valor    
    
    # METODO 24 (Diagrama de secuencia)
    def bloquear_evento(self, nuevo_estado, fecha_hora_actual):
        if isinstance(nuevo_estado, Estado):
            self.estado_actual = nuevo_estado
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


    # METODO 27 (Diagrama de secuencia)
    def set_fecha_hora_fin(self):
        print("SIN LA FECHA ACTUALIZADA")
        print(self.cambio_estado.get_fecha_hora_inicio())
        print(self.cambio_estado.get_fecha_hora_fin())

        self.cambio_estado.set_fecha_hora_fin(self.fecha_hora_seteo)

        print("CON LA FECHA ACTUALIZADA")
        print(self.cambio_estado)
        print(self.cambio_estado.get_fecha_hora_inicio())
        print(self.cambio_estado.get_fecha_hora_fin())

        # METODO 29 (Diagrama de secuencia)
        self.cambio_estado_bloq_rev = self.cambio_estado

    # METODO 31 (Diagrama de secuencia)
    def get_datos_restante(self):
        # METODO 32, 33, 34 (Diagrama de secuencia)
        datos = [
            self.alcance_sismo.get_nombre(), 
            self.generacion_sismo.get_nombre(), 
            self.clasificacion_sismo.get_nombre()
        ]

        self.obtener_datos_series_temporales()
        return datos
    
    # METODO 35 (Diagrama de secuencia)
    def obtener_datos_series_temporales(self):
        print("Llega aca para obtener datos de las series temporales")



    ############################################################
    ##### METODOS AUXILIARES ###################################
    ############################################################
    
    def obtener_cambio_estado_bloq_rev(self):
        return self.cambio_estado_bloq_rev

    def generar_datos_cambio_estados(self):

        self.lista_cambio_estado = []

        lista_aux = [
            ["2025-07-15 09:30:10", "2025-07-20 11:45:00", self.estado_actual ],
            ["2025-02-28 21:05:45", "2025-03-05 10:00:00", self.estado_actual],
            ["2025-11-03 14:18:22", "2025-11-08 16:30:00",self.estado_actual],
            ["2025-04-01 06:50:07", "", self.estado_actual]
        ]

        for datos_cestado in lista_aux:
            self.cambio_estado = CambioEstado(*datos_cestado)
            self.lista_cambio_estado.append(self.cambio_estado)
        
        return self.lista_cambio_estado

    



    
    
