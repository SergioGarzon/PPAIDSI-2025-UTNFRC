from Domain.Entities.Estado import Estado
from Domain.Entities.AlcanceSismo import AlcanceSismo
from Domain.Entities.OrigenDeGeneracion import OrigenDeGeneracion
from Domain.Entities.ClasificacionSismo import ClasificacionSismo
from Domain.Entities.SerieTemporal import SerieTemporal
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
        self.serie_temporal = None
        self.fecha_hora_seteo = None
        self.cambio_estado_bloq_rev = None
        self.cambio_estado = None
        self.serie_temporal_lista = []
        self.lista_datos_serie_temporal = []

    def set_serie_temporal(self, serie):
        self.serie_temporal = serie
        self.serie_temporal_lista.append(self.serie_temporal)
    
    def get_serie_temporal(self):
        return self.serie_temporal_lista
    
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
        return self.estado_actual.es_pendiente_revision()
    
    # METODO 24 (Diagrama de secuencia)
    def bloquear_evento(self, nuevo_estado, fecha_hora_actual, lista_cambio_estado):
        if isinstance(nuevo_estado, Estado):
            self.estado_actual = nuevo_estado # Aqui setea al estado actual el evento sismico seleccionado
            self.fecha_hora_seteo = fecha_hora_actual
            self.lista_cestado_dato = lista_cambio_estado
            # METODO 25 (Diagrama de secuencia)        
            self.buscar_estado_actual()
        else:
            raise TypeError("Error")
    
    # METODO 25 (Diagrama de secuencia)
    def buscar_estado_actual(self):        

        print("\n\nSE OBTIENE EL CAMBIO DE ESTADO SIN FECHA DE FIN\n")

        print("[fecha de inicio, fecha de fin, estado actual]")
        for lista in self.lista_cestado_dato:
            # METODO 26 (Diagrama de secuencia)
            if lista.es_estado_actual():                
                self.cambio_estado = lista                
                print("[" + str(self.cambio_estado.get_fecha_hora_inicio()) + ", " + 
                str(self.cambio_estado.get_fecha_hora_fin()) + ", [" + 
                str(self.cambio_estado.get_estado().get_ambito()) + ", " +
                str(self.cambio_estado.get_estado().get_nombre_estado()) + "]]")                
                print("\n")

        # METODO 27 (Diagrama de secuencia)
        self.set_fecha_hora_fin()        
        
        print("\nSETEAMOS LA FECHA Y HORA DE FIN Y MOSTRAMOS NUEVAMENTE EL CAMBIO DE ESTADO\n")
        print("[fecha de inicio, fecha de fin, estado actual]")
        for lista in self.lista_cestado_dato:
            # METODO 26 (Diagrama de secuencia)
            if lista.es_estado_actual():                
                self.cambio_estado = lista                
                print("[" + str(self.cambio_estado.get_fecha_hora_inicio()) + ", " + 
                str(self.cambio_estado.get_fecha_hora_fin()) + ", [" + 
                str(self.cambio_estado.get_estado().get_ambito()) + ", " +
                str(self.cambio_estado.get_estado().get_nombre_estado()) + "]]")                
                print("\n")

         # METODO 28 (Diagrama de secuencia)
        self.crear_cambio_estado()

    # METODO 27, 65 (Diagrama de secuencia)
    def set_fecha_hora_fin(self):

        for lista in self.lista_cestado_dato:
            if lista.es_estado_actual():                
                self.cambio_estado = lista 

        # METODO 27, 65 (Diagrama de secuencia)        
        self.cambio_estado.set_fecha_hora_fin(self.fecha_hora_seteo.strftime("%Y-%m-%d %H:%M:%S"))
        
        for list in self.lista_cestado_dato:            
            if list == self.cambio_estado:
                list.set_fecha_hora_fin(self.fecha_hora_seteo.strftime("%Y-%m-%d %H:%M:%S"))

        print("\n\nSETEO DE LA FECHA Y HORA ACTUAL")
        print("\n[fecha de inicio, fecha de fin, estado actual]")
        for lista in self.lista_cestado_dato:
            print("[" + lista.get_fecha_hora_inicio() + 
                  ", " + lista.get_fecha_hora_fin() + ", [" + 
                  lista.get_estado().get_ambito() + ", " + 
                  lista.get_estado().get_nombre_estado() + "]]")
        
    
    # METODO 28, 66 (Diagrama de secuencia)
    def crear_cambio_estado(self):  
        # METODO 29, 67 (Diagrama de secuencia)
        new_cambio_estado = CambioEstado(self.fecha_hora_seteo.strftime("%Y-%m-%d %H:%M:%S"), "", self.estado_actual)
        self.lista_cestado_dato.append(new_cambio_estado)

        print("\n\nSE CREA UN NUEVO CAMBIO DE ESTADO, DATOS DE LOS CAMBIOS DE ESTADOS:")
        print("\n[fecha de inicio, fecha de fin, estado actual]")
        for lista in self.lista_cestado_dato:
            print("[" + lista.get_fecha_hora_inicio() + 
                  ", " + lista.get_fecha_hora_fin() + ", [" + 
                  lista.get_estado().get_ambito() + ", " + 
                  lista.get_estado().get_nombre_estado() + "]]")

        print("\n\nCAMBIO DE ESTADO CREADO CORRECTAMENTE")

    # METODO 31 (Diagrama de secuencia)
    def get_datos_restante(self):

        print("\nSERIES TEMPORALES DEL EVENTO SISMICO SELECCIONADO (Cantidad " + str(len(self.get_serie_temporal())) + ")\n") 

        lista_enviada = []
        
        for lista_enviar in self.get_serie_temporal():
            print("Serie Temporal[" + str(lista_enviar.get_identificador()) + ", " +
                str(lista_enviar.get_condicion_nombre()) + ", " + 
                str(lista_enviar.get_fecha_hora_inicio_registro_muestra()) + ", " +
                str(lista_enviar.get_fecha_hora_registro()) + ", " + 
                str(lista_enviar.get_frecuencia_muestreo()) + "]")                 

        # METODO 32, 33, 34 (Diagrama de secuencia)
        datos = [
            # METODO 32 (Diagrama de secuencia)
            self.generacion_sismo.get_nombre(),
            # METODO 33 (Diagrama de secuencia)            
            self.alcance_sismo.get_nombre(),           
            # METODO 34 (Diagrama de secuencia)   
            self.clasificacion_sismo.get_nombre()
        ]
        
        return datos
    
    # METODO 36 (Diagrama de secuencia)
    def obtener_datos_series_temporales(self, datos_sismogafos):
        # METODO 37 (Diagrama de secuencia)
        for datos_serie_tmp in self.get_serie_temporal():
            self.lista_datos_serie_temporal = datos_serie_tmp.get_datos(datos_sismogafos)

        return self.lista_datos_serie_temporal

    # METODO 64 (Diagrama de secuencia)
    def rechazar_evento_sismico(self, nuevo_estado, fecha_hora_actual):
        if isinstance(nuevo_estado, Estado):
            self.estado_actual = nuevo_estado # Aqui setea al estado actual el evento sismico seleccionado
            self.fecha_hora_seteo = fecha_hora_actual
           
            # METODO 65 (Diagrama de secuencia) 
            self.set_fecha_hora_fin()

            # METODO 66 (Diagrama de secuencia)
            self.crear_cambio_estado()
        else:
            raise TypeError("Error")