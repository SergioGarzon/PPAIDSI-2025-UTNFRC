from Domain.Entities.EventoSismico import EventoSismico
from Domain.Entities.Estado import Estado
from Domain.Entities.AlcanceSismo import AlcanceSismo
from Domain.Entities.Sesion import Sesion
from Domain.Entities.Usuario import Usuario
from Domain.Entities.Empleado import Empleado
from datetime import datetime

class GestorRevManual:

    def __init__(self):        
        self.valor_indice = 0
        self.evento_seleccionado = None
        self.fecha_hora_actual = None
        self.evento = None
        self.estado = None
        self.usuario = None
        self.sesion = None
        self.empleado = None
        self.empleado_dato = None        
            
    #METODO 3 (Diagrama de secuencia)
    def nueva_rev_manual(self):     
        #METODO 4 (Diagrama de secuencia), aqui encontraremos el metodo  
        self.empleado_dato = self.generar_sesion_empleado().obtener_empleado()        
        print("\nSe obtiene el empleado\n" + str(self.empleado_dato))



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
        datos_para_varios_sismos = [
            "2025-05-22 16:00:00", # Fecha y hora ocurrencia (Clase EventoSismico)
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
            70 # Kilometros profundidad hasta (Clase ClasificacionSismo)             
            ]

