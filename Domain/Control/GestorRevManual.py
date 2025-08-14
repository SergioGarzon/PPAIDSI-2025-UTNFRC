from Domain.Entities.EventoSismico import EventoSismico
from Domain.Entities.Estado import Estado
from Domain.Entities.AlcanceSismo import AlcanceSismo
from Domain.Entities.Sesion import Sesion
from Domain.Entities.Usuario import Usuario
from Domain.Entities.Empleado import Empleado
from Domain.Entities.CambioEstado import CambioEstado
from Domain.Entities.OrigenDeGeneracion import OrigenDeGeneracion
from Domain.Entities.ClasificacionSismo import ClasificacionSismo
from Domain.Entities.Sismografo import Sismografo
from Domain.Entities.SerieTemporal import SerieTemporal
from Domain.Entities.EstacionSimologica import EstacionSimologica
from Domain.Entities.TiposDeDatos import TiposDeDatos
from Domain.Entities.DetalleMuestraSismica import DetalleMuestraSismica
from Domain.Entities.MuestraSismica import MuestraSismica
from datetime import datetime, timedelta
import string
import random

class GestorRevManual:

    def __init__(self):        
        self.valor_indice = 0
        self.evento_seleccionado = None
        self.fecha_hora_actual = None
        self.evento = None
        self.estado = None
        self.usuario = None
        self.sesion = None
        self.alcance = None
        self.origen_generacion = None
        self.clasificacion_sismo = None
        self.empleado = None        
        self.empleado_dato = None    
        self.cambio_estado = None
        self.serie_temporal = None      
        self.estacion_sismologica = None  
        self.sismografo = None    
        self.tipos_datos = None
        self.muestra_sismica = None
        self.eventos_sismicos_lista = None
        self.detalle_muestra_sismica = None
        self.lista_estados_evento_sismico = []
        self.lista_cambio_estado = []
        self.lista_serie_temporal = []       
        self.lista_sismografo = []
        self.lista_datos_mostrar = []
            
    #METODO 3 (Diagrama de secuencia)
    def nueva_rev_manual(self):     
        #METODO 4 (Diagrama de secuencia), aqui encontraremos el metodo  
        self.empleado_dato = self.generar_sesion_empleado().obtener_empleado() 
            
        print("\nSE OBTIENEN LOS DATOS DE LOS EMPLEADOS: \n[Nombre: " + str(self.empleado_dato.get_nombre()) +
        ", apellido: " + str(self.empleado_dato.get_apellido()) + 
        ", email: " + str(self.empleado.get_mail()) + 
        ", telefono: " + str(self.empleado_dato.get_telefono()) + "]")

        self.generar_series_temporales()
        self.buscar_eventos_sismicos_auto()

    # METODO 6 (Diagrama de secuencia)
    def buscar_eventos_sismicos_auto(self):

        self.generar_lista_eventos_sismicos()

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
            
        # METODO 15 (Diagrama de secuencia) 
        self.ordenar_eventos_sismicos()


    # METODO 15 (Diagrama de secuencia)                   
    def ordenar_eventos_sismicos(self):
        self.lista_enviar_vista = sorted(self.eventos_sismicos_lista_vista, key=lambda x: x[0], reverse=True)

    def obtener_eventos_para_mostrar(self): 
        return self.lista_enviar_vista

    # METODO 18 (Diagrama de secuencia)
    def tomar_seleccion_evento(self, lista_devolucion):              

        print("\nDATOS DEL EVENTO SISMICO SELECCIONADO:")
        print("Fecha hora ocurrencia: " + str(lista_devolucion[0]) + 
        ", latitud del epicentro: " + str(lista_devolucion[1]) + 
        ", latitud del hipocentro: " + str(lista_devolucion[2]) +
        ", longitud del epicentro: " + str(lista_devolucion[3]) +
        ", longitud del hipocentro: " + str(lista_devolucion[4]) + 
        ", valor de magnitud: " + str(lista_devolucion[5]))

        # Comparo que este todo correcto
        for indice, lista in enumerate(self.eventos_sismicos_lista):
            if (lista.get_fecha_hora_ocurrencia() == lista_devolucion[0] and
                lista.get_latitud_epicentro() == lista_devolucion[1] and
                lista.get_latitud_hipocentro() == lista_devolucion[2] and 
                lista.get_longitud_epicentro() == lista_devolucion[3] and
                lista.get_longitud_hipocentro() == lista_devolucion[4] and
                lista.get_valor_magnitud() == lista_devolucion[5]):
                    self.valor_indice = indice

        # METODO 19 (Diagrama de secuencia)  
        self.buscar_estado_bloq_en_revision()
                  
    # METODO 19 (Diagrama de secuencia) 
    def buscar_estado_bloq_en_revision(self): 
                      
        for lista in self.generar_lista_estados():
            # METODO 20, 21 (Diagrama de secuencia)
            if lista.es_ambito_evento_sismico() and lista.es_bloq_en_revision():
                self.estado_actual = lista
                print("\n\nSE OBTIENE EL ESTADO DEL AMBITO EVENTO SISMICO Y DE NOMBRE BLOQUEDO EN REVISION")
                print("[" + self.estado_actual.get_ambito() + ", " + self.estado_actual.get_nombre_estado() + "]")
                      
        # METODO 22 (Diagrama de secuencia)
        self.get_fecha_hora_actual(1)
        
    
    # METODO 22 (Diagrama de secuencia) 
    def get_fecha_hora_actual(self, verificacion):
        self.fecha_hora_actual = datetime.now()
        print("\n\nSE OBTIENE LA FECHA Y HORA ACTUAL\n" + str(self.fecha_hora_actual))
       
        if (verificacion == 1):
            # METODO 23 (Diagrama de secuencia)
            self.bloq_evento_sismico()


    # METODO 23 (Diagrama de secuencia)
    def bloq_evento_sismico(self):

        lista_cestado_estados = self.generar_datos_cambio_estados()

        print("\n\nMOSTRAMOS LOS CAMBIOS DE ESTADOS CREADOS\n")

        print("[fecha de inicio, fecha de fin, estado actual]")
        for l in lista_cestado_estados:
            print("[" + str(l.get_fecha_hora_inicio()) + ", " +
                str(l.get_fecha_hora_fin()) + ", [" + 
                str(l.get_estado().get_ambito()) + ", " + 
                str(l.get_estado().get_nombre_estado()) + "]]")
    
        # METODO 24 (Diagrama de secuencia)        
        self.lista_datos_restante = self.eventos_sismicos_lista[self.valor_indice].bloquear_evento(self.estado_actual, self.fecha_hora_actual, lista_cestado_estados)
        print("\nEVENTO BLOQUEADO CORRECTAMENTE")

        # METODO 30 (Diagrama de secuencia)
        self.buscar_datos_evento_selec()
    
    # METODO 30 (Diagrama de secuencia)
    def buscar_datos_evento_selec(self):
        # METODO 31 (Diagrama de secuencia)        
        self.evento_seleccionado_datos_totales = self.eventos_sismicos_lista[self.valor_indice].get_datos_restante()

        print("\nDATOS RESTANTES DEL EVENTO SISMICO SELECCIONADO")
        print("\n[Nombre de origen de generacion: " + self.evento_seleccionado_datos_totales[0] + ", " +
        "\nNombre del alcance: " + self.evento_seleccionado_datos_totales[1] + ", " + 
        "\nNombre de la clasificacion del sismo: " + self.evento_seleccionado_datos_totales[2] + "]")

        # METODO 35 (Diagrama de secuencia)
        self.obtener_sismografos()

    # METODO 35 (Diagrama de secuencia)
    def obtener_sismografos(self):
        datos_sismogafos = self.generar_datos_sismografos()

        print("\nDATOS DE LOS SISMOGRAFOS")

        print("\n\nSismografo[Numero serie, identificador, fecha adquisicion")
        print("Estacion sismologica[codigo, documento certificacion, latitud, longitud, nombre, numero certificacion ]]")
        for l in datos_sismogafos:
            print("\nSismografo[" + str(l.get_nro_serie()) + ", " + 
            str(l.get_identificacion()) + ", " + 
            str(l.get_fecha_adquisicion()) + ", Estacion Sismologica[" +
            str(l.get_estacion_sismologica().get_codigo_estacion()) + ", " +
            str(l.get_estacion_sismologica().get_documento_certifiacion_adq()) +  ", " + 
            str(l.get_estacion_sismologica().get_fecha_solicitud_certificacion()) + ", " +
            str(l.get_estacion_sismologica().get_latitud()) + ", " +
            str(l.get_estacion_sismologica().get_longitud()) + ", " + 
            str(l.get_estacion_sismologica().get_nombre()) + ", " +
            str(l.get_estacion_sismologica().get_nro_certificacion_adquisicion()) + "]")
            
            for setmp_lista in l.get_serie_temporal():
                print("\nSerie Temporal[" + str(setmp_lista.get_identificador()) + ", " +
                str(setmp_lista.get_condicion_nombre()) + ", " + 
                str(setmp_lista.get_fecha_hora_inicio_registro_muestra()) + ", " +
                str(setmp_lista.get_fecha_hora_registro()) + ", " + 
                str(setmp_lista.get_frecuencia_muestreo()) + ", ") 

                for data in setmp_lista.get_muestra_sismica():
                    print("Muestra Sismica[" + str(data.get_fecha_hora_muestra()) + "], ")

                    for it in data.get_detalle_muestra_sismica():
                        print("Detalle Muestra Sismica[" + str(it.get_valor()) + "]")

                        print("Tipos de Datos[" + str(it.get_tipos_datos().get_denominacion()) + ", " + 
                        str(it.get_tipos_datos().get_nombre_unidad_medida()) + ", " +
                        str(it.get_tipos_datos().get_valor_umbral()) + "]")                                
        
        # METODO 36 (Diagrama de secuencia)
        self.lista_datos_mostrar = self.eventos_sismicos_lista[self.valor_indice].obtener_datos_series_temporales(datos_sismogafos)

        print("\nSERIES TEMPORALES ASOCIADAS AL EVENTO SISMICO\n")
        print(self.lista_datos_mostrar)        


    ############################################################
    ##### METODOS AUXILIARES ###################################
    ############################################################


    # Este es el metodo para hardcodear datos del empleado
    def generar_sesion_empleado(self): 
        datos_empleado = ["Pablo", 
                          "Paez", 
                          "ppaez@sismos-conicet.com.ar", 
                          351000000]
        self.empleado = Empleado(*datos_empleado)

        datos_usuario = ["adminsismos", 
                         "1234", 
                         self.empleado.get_nombre(), 
                         self.empleado.get_apellido(),
                         self.empleado.get_mail(),
                         self.empleado.get_telefono()]
        self.usuario = Usuario(*datos_usuario)

        datos_sesion = [1, 
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                        None,
                        self.usuario.get_nombre_usuario(),
                        self.usuario.get_contrasenia(),
                        self.empleado.get_nombre(), 
                        self.empleado.get_apellido(),
                        self.empleado.get_mail(),
                        self.empleado.get_telefono()]  
             
        self.sesion = Sesion(*datos_sesion)   
        return self.sesion

    # Este es el metodo para hardcodear datos de los eventos sismicos
    def generar_lista_eventos_sismicos(self):

        self.eventos_sismicos_lista = []

        for i in range(30):

            estado_descripcion = ""
            estado_valor = random.randint(1, 10)

            if estado_valor >= 1 and estado_valor < 5:
                estado_descripcion = "Pendiente de revision"
            elif estado_valor >= 5 and estado_valor < 8:
                estado_descripcion = "Bloqueado en revision"
            elif estado_valor >= 8 and estado_valor <= 10:
                estado_descripcion = "Rechazado"

            lista_estados = [
                "Evento sismico", # Tipo de estado (Estado)
                estado_descripcion # Descripcion del estado (Estado)
            ]

            self.estado = Estado(*lista_estados)

            lista_alcance = [
                "nombre alcance " + str(i), # Nombre alcance (Clase Alcance)
                "descripcion alcance " + str(i), # Descripcion alcance (Clase Alcance)
            ]

            self.alcance = AlcanceSismo(*lista_alcance)

            lista_generacion = [
                "nombre generacion " + str(i), # Nombre Generacion (Clase OrigenGeneracion)
                "descripcion generacion " + str(i), # Descripcion Generacion (Clase OrigenGeneracion)
            ]

            self.origen_generacion = OrigenDeGeneracion(*lista_generacion)

            clasificacion_valor = random.randint(1, 11)
            clasificacion_descripcion = ""
            
            if clasificacion_valor == 1:
                clasificacion_descripcion = "Superficial"
            elif clasificacion_valor == 2:
                clasificacion_descripcion = "Muy Superficial"
            elif clasificacion_valor == 3:
                clasificacion_descripcion = "Poco Profundo"
            elif clasificacion_valor == 4:
                clasificacion_descripcion = "Media Profundidad"
            elif clasificacion_valor == 5:
                clasificacion_descripcion = "Sub-Intermedio 1"
            elif clasificacion_valor == 6:
                clasificacion_descripcion = "Sub-Intermedio 2"                
            elif clasificacion_valor == 7:
                clasificacion_descripcion = "Sub-Intermedio 3"     
            elif clasificacion_valor == 8:
                clasificacion_descripcion = "Sub-Intermedio 4"     
            elif clasificacion_valor == 9:
                clasificacion_descripcion = "Manto Superior"  
            elif clasificacion_valor == 10:
                clasificacion_descripcion = "Profundo extremo"  
            elif clasificacion_valor == 11:
                clasificacion_descripcion = "Zona de Subducción"  

            lista_clasificacion_sismo = [
                clasificacion_descripcion, # Nombre Clasificacion Sismo (Clase ClasificacionSismo) 
                random.randint(0, 800), # Kilometros profundidad desde (Clase ClasificacionSismo) 
                random.randint(0, 800) # Kilometros profundidad hasta (Clase ClasificacionSismo)  
            ]

            self.clasificacion_sismo = ClasificacionSismo(*lista_clasificacion_sismo)
    
            lista_datos_para_varios_sismos = [
                self.generar_fecha_hora_random().strftime("%Y-%m-%d %H:%M:%S"), # Fecha y hora ocurrencia (Clase EventoSismico)
                self.generar_fecha_hora_random().strftime("%Y-%m-%d %H:%M:%S"), # Fecha y hora fin (Clase EventoSismico)
                round(random.uniform(-100, 100), 2), # Latitud epicentro (Clase EventoSismico)
                round(random.uniform(-100, 100), 2), # Longuitud epicentro (Clase EventoSismico)
                round(random.uniform(-100, 100), 2), # Latitud hipocentro (Clase EventoSismico)
                round(random.uniform(-100, 100), 2), # Longuitud hipocentro (Clase EventoSismico)
                round(random.uniform(-100, 100), 2), # Magnitud (Clase EventoSismico)
                self.estado.get_ambito(), # Ambito estado (Clase Estado)
                self.estado.get_nombre_estado(), # Nombre estado (Clase Estado)
                self.alcance.get_nombre(), # Nombre alcance (Clase Alcance)
                self.alcance.get_descripcion(), # Descripcion alcance (Clase Alcance)
                self.origen_generacion.get_nombre(), # Nombre Generacion (Clase OrigenGeneracion)
                self.origen_generacion.get_descripcion(), # Descripcion Generacion (Clase OrigenGeneracion)
                self.clasificacion_sismo.get_nombre(), # Nombre Clasificacion Sismo (Clase ClasificacionSismo) 
                self.clasificacion_sismo.get_kilometro_profundidad_desde(), # Kilometros profundidad desde (Clase ClasificacionSismo) 
                self.clasificacion_sismo.get_kilometro_profundidad_hasta() # Kilometros profundidad hasta (Clase ClasificacionSismo)             
            ]

            self.evento = EventoSismico(*lista_datos_para_varios_sismos)

            for recorrer_lista in self.lista_serie_temporal:
                self.evento.set_serie_temporal(recorrer_lista)

            self.eventos_sismicos_lista.append(self.evento)


    # Este es un metodo que hice, es auxiliar y es para generar fecha y hora aleatoriamente
    def generar_fecha_hora_random(self, anio_inicio=1900, anio_fin=datetime.now().year):
    
        fecha_inicio = datetime(anio_inicio, 1, 1, 0, 0, 0)
        fecha_fin = datetime(anio_fin, 12, 31, 23, 59, 59)

        diferencia_horaria = fecha_fin - fecha_inicio
        segundos_total = int(diferencia_horaria.total_seconds())

        segundos_random = random.randint(0, segundos_total)

        fecha_hora_random = fecha_inicio + timedelta(seconds=segundos_random)

        return fecha_hora_random
    
    # Este metodo es para generar lista de estados
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
            self.lista_estados_evento_sismico.append(self.estado)

        return self.lista_estados_evento_sismico

    # Método para generar el cambio de estados
    def generar_datos_cambio_estados(self):      
        
        lista_cambio_estado_aux = [
            ["2025-07-15 09:30:10", "2025-07-20 11:45:00", self.estado_actual],
            ["2025-02-28 21:05:45", "2025-03-05 10:00:00", self.estado_actual],
            ["2025-11-03 14:18:22", "2025-11-08 16:30:00",self.estado_actual],
            ["2025-04-01 06:50:07", "", self.estado_actual]
        ]

        for datos_cestado in lista_cambio_estado_aux:
            self.cambio_estado = CambioEstado(*datos_cestado)
            self.lista_cambio_estado.append(self.cambio_estado)  

        return self.lista_cambio_estado

    # Metodo para generar los sismografos
    def generar_datos_sismografos(self):

        for i in range(2):
            lista_estacion_sismologica_aux = [
                str(random.randint(1, 10)),
                "131312222",
                self.generar_fecha_hora_random().strftime("%Y-%m-%d %H:%M:%S"),
                str(random.randint(1, 750)),
                str(random.randint(1, 800)),
                "Estacion " + str(random.randint(1, 10)),
                str(random.randint(1, 10))
            ]

            self.estacion_sismologica = EstacionSimologica(*lista_estacion_sismologica_aux)
        
        for i in range(2):
            lista_sismografo_aux = [
                "A1" + str(random.randint(1, 10)),
                str(random.randint(1, 9999)),
                self.generar_fecha_hora_random().strftime("%Y-%m-%d %H:%M:%S"),
                self.estacion_sismologica.get_codigo_estacion(),
                self.estacion_sismologica.get_documento_certifiacion_adq(),
                self.estacion_sismologica.get_fecha_solicitud_certificacion(),
                self.estacion_sismologica.get_latitud(),
                self.estacion_sismologica.get_longitud(),
                self.estacion_sismologica.get_nombre(),
                self.estacion_sismologica.get_nro_certificacion_adquisicion()
            ]
            self.sismografo = Sismografo(*lista_sismografo_aux)

            for recorrer_lista in self.lista_serie_temporal:
                self.sismografo.set_serie_temporal(recorrer_lista)            

            self.lista_sismografo.append(self.sismografo)

        return self.lista_sismografo

    # Metodo para generar las series temporales
    def generar_series_temporales(self):
  
        for i in range(random.randint(1,5)):

            lista_series_temporales_aux = [
                random.randint(0, 100),
                str(random.choice(string.ascii_letters)),
                self.generar_fecha_hora_random().strftime("%Y-%m-%d %H:%M:%S"),
                self.generar_fecha_hora_random().strftime("%Y-%m-%d %H:%M:%S"),
                random.randint(0, 25)
            ]

            self.serie_temporal = SerieTemporal(*lista_series_temporales_aux)  

            for i in range(random.randint(1, 2)):
                lista_muestra_sismica_aux = [
                    self.generar_fecha_hora_random().strftime("%Y-%m-%d %H:%M:%S")
                ]

                self.muestra_sismica = MuestraSismica(*lista_muestra_sismica_aux)                                

                for i in range(random.randint(1, 2)):

                    lista_tipo_datos_aux = [
                        str(random.choice(string.ascii_letters)),
                        str(random.choice(string.ascii_letters)),
                        random.randint(0, 800)
                    ]

                    self.tipos_datos = TiposDeDatos(*lista_tipo_datos_aux)

                    lista_detalle_muestra_sismica_aux = [
                        random.randint(0, 25),
                        self.tipos_datos.get_denominacion(),
                        self.tipos_datos.get_nombre_unidad_medida(),
                        self.tipos_datos.get_valor_umbral()
                    ]

                    self.detalle_muestra_sismica = DetalleMuestraSismica(*lista_detalle_muestra_sismica_aux)                
                    self.muestra_sismica.agregar_detalle_muestra_sismica(self.detalle_muestra_sismica)

                self.serie_temporal.agregar_muestra_sismica(self.muestra_sismica)

            self.lista_serie_temporal.append(self.serie_temporal)
        
        