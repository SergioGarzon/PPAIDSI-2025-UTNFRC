from Domain.Entities.EventoSismico import EventoSismico
from Domain.Entities.Estado import Estado
from Domain.Entities.AlcanceSismo import AlcanceSismo
from Domain.Entities.Sesion import Sesion
from Domain.Entities.Usuario import Usuario
from Domain.Entities.Empleado import Empleado
from Domain.Entities.OrigenDeGeneracion import OrigenDeGeneracion
from Domain.Entities.ClasificacionSismo import ClasificacionSismo
from datetime import datetime
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
            
    #METODO 3 (Diagrama de secuencia)
    def nueva_rev_manual(self):     
        #METODO 4 (Diagrama de secuencia), aqui encontraremos el metodo  
        self.empleado_dato = self.generar_sesion_empleado().obtener_empleado()        
        print("\nSe obtiene el empleado\n" + str(self.empleado_dato))

        self.generar_lista_eventos_sismicos()



    ############################################################
    ##### METODOS AUXILIARES ###################################
    ############################################################


    # Este es el metodo para harcodear datos del empleado
    def generar_sesion_empleado(self): 
        datos_empleado = ["Pablo", 
                          "Paez", 
                          "ppaez@sismos-conicet.com.ar", 
                          351000000]
        self.empleado = Empleado(*datos_empleado)

        datos_usuario = ["adminsismos", 
                         "1234", 
                         self.empleado.get_nombre, 
                         self.empleado.get_apellido,
                         self.empleado.get_mail,
                         self.empleado.get_telefono]
        self.usuario = Usuario(*datos_usuario)

        datos_sesion = [1, 
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                        None,
                        self.usuario.get_nombre_usuario,
                        self.usuario.get_contrasenia,
                        self.empleado.get_nombre, 
                        self.empleado.get_apellido,
                        self.empleado.get_mail,
                        self.empleado.get_telefono]  
             
        self.sesion = Sesion(*datos_sesion)   
        return self.sesion

    def generar_lista_eventos_sismicos(self):

        for i in range(10):

            estado_descripcion = ""
            estado_valor = random.randint(1, 2)

            if estado_valor == 1:
                estado_descripcion = "Pendiente de revision"
            elif estado_valor == 2:
                estado_descripcion = "Bloqueado en revision"
            elif estado_valor == 3:
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
                "2025-05-22 16:00:00", # Fecha y hora ocurrencia (Clase EventoSismico)
                "2025-05-22 14:30:00", # Fecha y hora fin (Clase EventoSismico)
                -31.416, # Latitud epicentro (Clase EventoSismico)
                -31.420, # Longuitud epicentro (Clase EventoSismico)
                -64.183, # Latitud hipocentro (Clase EventoSismico)
                -64.190, # Longuitud hipocentro (Clase EventoSismico)
                2.5, # Magnitud (Clase EventoSismico)
                self.estado.get_ambito, # Ambito estado (Clase Estado)
                self.estado.get_nombre_estado, # Nombre estado (Clase Estado)
                self.alcance.get_nombre, # Nombre alcance (Clase Alcance)
                self.alcance.get_descripcion, # Descripcion alcance (Clase Alcance)
                self.origen_generacion.get_nombre, # Nombre Generacion (Clase OrigenGeneracion)
                self.origen_generacion.get_descripcion, # Descripcion Generacion (Clase OrigenGeneracion)
                self.clasificacion_sismo.get_nombre, # Nombre Clasificacion Sismo (Clase ClasificacionSismo) 
                self.clasificacion_sismo.get_kilometro_profundidad_desde, # Kilometros profundidad desde (Clase ClasificacionSismo) 
                self.clasificacion_sismo.get_kilometro_profundidad_hasta # Kilometros profundidad hasta (Clase ClasificacionSismo)             
            ]

            self.evento = EventoSismico(*lista_datos_para_varios_sismos)

            print(self.evento)

