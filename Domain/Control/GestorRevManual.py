from Domain.Entities.EventoSismico import EventoSismico
from Domain.Entities.Sesion import Sesion
from datetime import datetime
from Domain.Entities.Estado import Estado

class GestorRevManual:

    def __init__(self):
        self.eventos_sismicos_lista = []
        self.eventos_sismicos_lista_vista = []
        self.lista_enviar_vista = []
        self.lista_estados = []
        self.valor_indice = 0
        self.evento_seleccionado = None
        self.fecha_hora_actual = None
        self.evento = None
        self.estado = None
        self.empleado_dato = None 
        self.ambito_estado = ""  
        self.estado_bloq_rev = "" 
    
    #METODO 3 (Diagrama de secuencia)
    def nueva_revision_manual(self):        
        datos_sesion_usuario = self.generar_sesion_empleado()  

        self.sesion = Sesion(*datos_sesion_usuario)
        #METODO 4 (Diagrama de secuencia)
        self.empleado_dato = self.sesion.obtener_empleado()   

        self.buscar_eventos_sismicos_auto() 
        

    #METODO 6 (Diagrama de secuencia)
    def buscar_eventos_sismicos_auto(self):             
        self.generar_lista_datos()

        self.eventos_sismicos_lista_vista = []

        for datos in self.eventos_sismicos_lista:
            
            # METODO 7 (Diagrama de secuencia)
            if datos.es_pendiente_revision():
                
                lista_aux = [
                    # METODO 9 (Diagrama de secuencia)
                    datos.get_fecha_hora_ocurrencia(),                     
                    datos.get_fecha_hora_fin(),
                    # METODO 10 (Diagrama de secuencia) 
                    datos.get_latitud_epicentro(),
                    # METODO 11 (Diagrama de secuencia) 
                    datos.get_latitud_hipocentro(),
                    # METODO 12 (Diagrama de secuencia) 
                    datos.get_longitud_epicentro(),
                    # METODO 13 (Diagrama de secuencia)
                    datos.get_longitud_hipocentro(),
                    # METODO 14 (Diagrama de secuencia)
                    datos.get_valor_magnitud()
                ]

                self.eventos_sismicos_lista_vista.append(lista_aux)   
           
        self.ordenarEventosSismicos()

    # METODO 15 (Diagrama de secuencia) 
    def ordenarEventosSismicos(self):
        self.lista_enviar_vista = sorted(self.eventos_sismicos_lista_vista, key=lambda x: x[0], reverse=True)

    def obtener_eventos_para_mostrar(self): 
        return self.lista_enviar_vista
    
    # METODO 18 (Diagrama de secuencia)
    def tomar_seleccion_evento(self, lista_devolucion):              

        # Comparo que este todo correcto
        for indice, lista in enumerate(self.eventos_sismicos_lista):
            if (lista.get_fecha_hora_ocurrencia() == lista_devolucion[0] and
                lista.get_latitud_epicentro() == lista_devolucion[1] and
                lista.get_latitud_hipocentro() == lista_devolucion[2] and 
                lista.get_longitud_epicentro() == lista_devolucion[3] and
                lista.get_longitud_hipocentro() == lista_devolucion[4] and
                lista.get_valor_magnitud() == lista_devolucion[5]):
                    self.valor_indice = indice
   
        self.buscar_estado_bloq_en_revision()
                  
    # METODO 19 (Diagrama de secuencia) 
    def buscar_estado_bloq_en_revision(self):                    

        self.generar_lista_estados() 

        for lista in self.lista_estados:
            if lista.es_ambito_evento_sismico() != None and lista.es_bloq_en_revision() != None:
                # METODO 20 (Diagrama de secuencia)
                self.ambito_estado = lista.es_ambito_evento_sismico()

                # METODO 21 (Diagrama de secuencia)
                self.estado_bloq_rev = lista.es_bloq_en_revision()

        self.get_fecha_hora_actual()
    
    # METODO 22 (Diagrama de secuencia) 
    def get_fecha_hora_actual(self):
        self.fecha_hora_actual = datetime.now()
        self.bloq_evento_sismico()

    # METODO 23 (Diagrama de secuencia)
    def bloq_evento_sismico(self):
        # METODO 24 (Diagrama de secuencia)
        self.eventos_sismicos_lista[self.valor_indice].bloquear_evento(Estado(self.ambito_estado, self.estado_bloq_rev), self.fecha_hora_actual)
        print("Evento bloqueado correctamente")

        print("Obtencion del cambio de estado OK")
        print(self.eventos_sismicos_lista[self.valor_indice].obtener_cambio_estado_bloq_rev())

        self.buscar_datos_evento_selec()

    # METODO 30 (Diagrama de secuencia)
    def buscar_datos_evento_selec(self):
        # METODO 31 (Diagrama de secuencia)
        print(self.eventos_sismicos_lista[self.valor_indice].get_datos_restante())
        print("Empieza a buscar los datos del evento seleccionado")

    def clasificar_por_estacion():
        pass

    def tomar_seleccion_no_visualizacion():
        pass
    
    def tomarOpcionNoModificarDatosEventoSismico():
        pass

    def tomarOpcionSeleccionadaRechazarEvento():
        pass

    def tomarOpcionSeleccionadaRechazarEvento():
        pass
    
    def getFechaHoraActual():
        pass
    
    def rechazarEventoSismico():
        pass

    def fin_CU():
        pass

    ############################################################
    ##### METODOS AUXILIARES ###################################
    ############################################################

    def generar_sesion_empleado(self): 
        datos_sesion = [1, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), None, "adminsismos", "1234", "Pablo", "Paez", "ppaez@sismos-conicet.com.ar", 351000000]       
        return datos_sesion
        
    def generar_lista_estados(self):
        lista_datos_estado = [
            ["Evento Sismico", "Pendiente de revision"],
            ["Evento Sismico", "Bloqueado en revision"],
            ["Evento Sismico", "Rechazado"],
            ["Sismografo", ""],
            ["Orden de inspeccion", ""],
            ["Serie temporal", ""]
        ]

        for lista in lista_datos_estado:
            self.estado = Estado(*lista)
            self.lista_estados.append(self.estado)


    def generar_lista_datos(self):

        datos_para_varios_sismos = [
            ["2025-05-22 16:00:00", # Fecha y hora ocurrencia (Clase EventoSismico)
             "2025-05-22 14:30:00", # Fecha y hora fin (Clase EventoSismico)
             -31.416, # Latitud epicentro (Clase EventoSismico)
             -31.420, # Longuitud epicentro (Clase EventoSismico)
             -64.183, # Latitud hipocentro (Clase EventoSismico)
             -64.190, # Longuitud hipocentro (Clase EventoSismico)
             2.5, # Magnitud (Clase EventoSismico)
             "Evento Sismico", # Ambito estado (Clase Estado)
             "Pendiente de revision", # Nombre estado (Clase Estado)
             "nombre alcance 1", # Nombre alcance (Clase Alcance)
             "descripcion alcance 1", # Descripcion alcance (Clase Alcance)
             "nombre generacion 1", # Nombre Generacion (Clase OrigenGeneracion)
             "descripcion generacion 1", # Descripcion Generacion (Clase OrigenGeneracion)
             "Superficial", # Nombre Clasificacion Sismo (Clase ClasificacionSismo) 
             0, # Kilometros profundidad desde (Clase ClasificacionSismo) 
             70], # Kilometros profundidad hasta (Clase ClasificacionSismo) 

            ["2025-05-21 10:15:00", "2025-05-21 10:00:00", -32.000, -32.010, -65.000, -65.005, 2.2, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 2", "descripcion generacion 2", 
             "Intermedio Bajo", 70,  150],

            ["2025-05-20 08:00:00", "2025-05-20 07:50:00", -33.500, -33.510, -66.100, -66.105, 1.1, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 3", "descripcion generacion 3",
             "Intermedio Alto", 150, 300],

            ["2025-05-19 23:00:00", "2025-05-19 22:45:00", -30.123, -30.125, -63.456, -63.458, 3.8, 
             "Evento Sismico", "Bloqueado en revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 4",
             "descripcion generacion 4", "Profundo", 300, 700],

            ["2025-05-18 07:00:00", "2025-05-18 06:30:00", -29.000, -29.010, -62.000, -62.005, 1.0, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 5", "descripcion generacion 5", 
             "Muy Superficial", 0, 15],

            ["2025-05-22 02:30:00", "2025-05-17 02:00:00", -24.555, -30.885, -44.556, -64.552, 4.9, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 6", "descripcion generacion 6", 
             "Poco Profundo", 15, 40],

            ["2025-05-22 15:00:00", "2025-05-22 14:30:00", -31.416, -31.420, -64.183, -64.190, 0.5, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 7", "descripcion generacion 7", 
             "Media Profundidad", 40, 70],

            ["2025-05-16 11:45:00", "2025-05-16 11:30:00", -31.700, -31.705, -63.900, -63.903, 3.4, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 8", "descripcion generacion 8", 
             "Sub-Intermedio 1", 70, 100],

            ["2025-05-15 20:00:00", "2025-05-15 19:50:00", -32.120, -32.125, -65.300, -65.305, 3.1, "Evento Sismico", 
             "Bloqueado en revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 9", "descripcion generacion 9", 
             "Sub-Intermedio 2", 100, 150],

            ["2025-05-15 05:10:00", "2025-05-15 05:00:00", -29.990, -29.992, -61.500, -61.501, 3.3, "Evento Sismico",
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 10", "descripcion generacion 10", 
             "Sub-Intermedio 3", 150, 220],

            ["2025-05-15 18:20:00", "2025-05-13 18:10:00", -30.500, -30.505, -62.800, -62.802, 3.0, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 11", "descripcion generacion 11", 
             "Sub-Intermedio 4", 220, 300],

            ["2025-05-12 09:00:00", "2025-05-12 08:55:00", -33.000, -33.001, -66.500, -66.501, 2.5, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 12", "descripcion generacion 12", 
             "Profundo Leve", 300, 450],

            ["2025-05-11 01:05:00", "2025-05-11 00:55:00", -31.250, -31.252, -64.050, -64.053, 4.0, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 13", "descripcion generacion 13", 
             "Profundo Moderado", 450, 600],

            ["2025-05-10 16:30:00", "2025-05-10 16:15:00", -29.500, -29.501, -60.800, -60.803, 3.5, "Evento Sismico",
             "Bloqueado en revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 14", "descripcion generacion 14", 
             "Profundo Extremo", 600, 700],

            ["2025-05-22 04:40:00", "2025-05-09 04:30:00", -32.700, -32.705, -67.000, -67.008, 2.1, "Evento Sismico", 
             "Pendiente de revision", "nombre alcance 1", "descripcion alcance 1", "nombre generacion 15", "descripcion generacion 15", 
             "Manto Superior", 0, 400],

            ["2025-05-08 21:00:00", "2025-05-08 20:45:00", -30.000, -30.001, -63.000, -63.002, 4.0, "Evento Sismico", 
             "Rechazado", "nombre alcance 16", "descripcion alcance 16", "nombre generacion 16", "descripcion generacion 1", 
             "Zona de Subducción", 0, 700]
        ]

        self.eventos_sismicos_lista = []

        for datos_evento in datos_para_varios_sismos:
            self.evento = EventoSismico(*datos_evento)   
            self.eventos_sismicos_lista.append(self.evento)