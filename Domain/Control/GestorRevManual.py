from Domain.Entities.EventoSismico import EventoSismico
from datetime import datetime
from Domain.Entities.Estado import Estado

class GestorRevManual:

    def __init__(self):
        self.eventos_sismicos_lista = []
        self.eventos_sismicos_lista_vista = []
        self.datos_para_varios_sismos = []
        self.lista_estados = []
        self.evento_seleccionado = None
        self.evento = None
        self.estado = None           
    
    #METODO 3 (Diagrama de secuencia)
    def nueva_revision_manual(self):        
        self.buscar_eventos_sismicos_auto()   

    #METODO 4 (Diagrama de secuencia)
    def buscar_eventos_sismicos_auto(self):             
        self.generar_lista_datos()

        self.eventos_sismicos_lista = []

        for datos_evento in self.datos_para_varios_sismos:
            self.evento = EventoSismico(*datos_evento)            

            if self.evento.es_pendiente_revision():
                self.eventos_sismicos_lista.append(self.evento)
            
        self.ordenarEventosSismicos()

    #METODO 5 (Diagrama de secuencia)
    def ordenarEventosSismicos(self): 
        self.eventos_sismicos_lista.sort(key=lambda evento: self.evento.get_fecha_hora_ocurrencia(), reverse=True)

        for i, evento in enumerate(self.eventos_sismicos_lista):
            fecha_ocurrencia_str = evento.get_fecha_hora_ocurrencia().strftime("%d/%m/%Y")
            hora_ocurrencia_str = evento.get_fecha_hora_ocurrencia().strftime("%H:%M:%S")

            epicentro_str = f"Latitud: {evento.get_latitud_epicentro()} Longitud: {evento.get_longitud_epicentro()}"
            hipocentro_str = f"Latitud: {evento.get_latitud_hipocentro()} Longitud: {evento.get_longitud_hipocentro()}"
            magnitud_str = f"{evento.get_valor_magnitud()}°"

            fila_formateada = (fecha_ocurrencia_str, hora_ocurrencia_str, epicentro_str, hipocentro_str,magnitud_str)
            self.eventos_sismicos_lista_vista.append(fila_formateada)
        

    #METODO 6 (Diagrama de secuencia)
    def obtener_eventos_para_mostrar(self): 
        return self.eventos_sismicos_lista_vista
    
    #METODO 9 (Diagrama de secuencia)
    def tomar_seleccion_evento(self, item_values):
                
        fecha_evento_str = item_values[1]
        hora_evento_str = item_values[2]
        ubicacion_epicentro_str = str(item_values[3])
        ubicacion_hipocentro_str = str(item_values[4])
        magnitud_str = item_values[5]

        fecha_hora_combinada_str = f"{fecha_evento_str} {hora_evento_str}"

        try:
            fecha_hora_ocurrencia_dt = datetime.strptime(fecha_hora_combinada_str, "%d/%m/%Y %H:%M:%S")
        except ValueError as e:
            fecha_hora_ocurrencia_dt = None        

        cadena = ubicacion_epicentro_str
        posicion = 0
        lista_espacio = []

        while True:
            posicion = cadena.find(" ", posicion)
            if posicion == -1:
                break 
            lista_espacio.append(posicion)
            posicion += 1  

        cadena_2 = ubicacion_hipocentro_str
        posicion_2 = 0
        lista_espacio_2 = []

        while True:
            posicion_2 = cadena_2.find(" ", posicion_2)
            if posicion_2 == -1:
                break 
            lista_espacio_2.append(posicion_2)
            posicion_2 += 1  
        
        latitud_epicentro = float(ubicacion_epicentro_str[lista_espacio[0]:lista_espacio[1]])
        longitud_epicentro = float(ubicacion_epicentro_str[lista_espacio[2]:len(ubicacion_epicentro_str)])
        latitud_hipocentro = float(ubicacion_hipocentro_str[lista_espacio_2[0]:lista_espacio_2[1]])
        longitud_hipocentro = float(ubicacion_hipocentro_str[lista_espacio_2[2]:len(ubicacion_hipocentro_str)])
        magnitud = float(magnitud_str[:-1])

        # Aqui compara los estados
        for lista in self.eventos_sismicos_lista:
            if(lista.get_valor_magnitud() == magnitud and
               lista.get_fecha_hora_ocurrencia() == fecha_hora_ocurrencia_dt and
               lista.get_latitud_epicentro() == latitud_epicentro and
               lista.get_longitud_epicentro() == longitud_epicentro and
               lista.get_latitud_hipocentro() == latitud_hipocentro and
               lista.get_longitud_hipocentro() == longitud_hipocentro):
                print("COMPARA Y ESTA TODO OK")

        self.buscarEstadoBloqEnRevision()
       
      
    #METODO 10 (Diagrama de secuencia) 
    def buscarEstadoBloqEnRevision(self):
        ambito_evento_sismico = ""
        nombre_estado_bloqueado_revision = ""     

        self.generar_lista_estados()   
        
        for lista in self.lista_estados:
            # METODO 11 (Diagrama de secuencia)
            ambito_evento_sismico = lista.es_ambito_evento_sismico()

            # METODO 12 (Diagrama de secuencia)
            nombre_estado_bloqueado_revision = lista.esBloqEnRevision()

        print("Ambito evento sismico: " + str(ambito_evento_sismico))
        print("Nombre estado bloqueado en revision: " + str(nombre_estado_bloqueado_revision))
       
        self.get_fecha_hora_actual()   
    
    # METODO 13 (Diagrama de secuencia)
    def get_fecha_hora_actual(self):
        fecha_hora_actual = datetime.now()
        print("Fecha y hora actual: " + str(fecha_hora_actual))
        self.bloq_evento_sismico()

    # METODO 14 (Diagrama de secuencia)
    def bloq_evento_sismico(self):
        print("Hasta aqui se llega")
        # ------ COMPLETAR ESTE METODO, FALTA DESDE EL METODO 14 HASTA EL METODO 20 ------


    # METODO 21 (Diagrama de secuencia)
    def buscar_datos_evento_selec():
        pass

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

    def generar_lista_estados(self):
        lista_datos_estado = [
            ["Evento Sismico", "Pendiente en revision"],
            ["Evento Sismico", "Bloqueado en revision"]
        ]

        for lista in lista_datos_estado:
            self.estado = Estado(*lista)
            self.lista_estados.append(self.estado)

    def generar_lista_datos(self):
        self.datos_para_varios_sismos = [
            # magnitud no debe superar el valor 4.0
            # Pendiente de revision (cambiarlos), Bloqueado en revision, Rechazado
            ["2025-05-22 15:00:00", "2025-05-22 14:30:00", -31.416, -31.420, -64.183, -64.190, 6.5, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-21 10:15:00", "2025-05-21 10:00:00", -32.000, -32.010, -65.000, -65.005, 4.2, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-20 08:00:00", "2025-05-20 07:50:00", -33.500, -33.510, -66.100, -66.105, 7.1, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-19 23:00:00", "2025-05-19 22:45:00", -30.123, -30.125, -63.456, -63.458, 3.8, "Evento Sismico", "Bloqueado en revision", "", "", "", "", "", 0, 0],
            ["2025-05-18 07:00:00", "2025-05-18 06:30:00", -29.000, -29.010, -62.000, -62.005, 5.0, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-17 02:30:00", "2025-05-17 02:00:00", -30.880, -30.885, -64.550, -64.552, 2.9, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-16 11:45:00", "2025-05-16 11:30:00", -31.700, -31.705, -63.900, -63.903, 5.5, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-15 20:00:00", "2025-05-15 19:50:00", -32.120, -32.125, -65.300, -65.305, 3.1, "Evento Sismico", "Bloqueado en revision", "", "", "", "", "", 0, 0],
            ["2025-05-15 05:10:00", "2025-05-15 05:00:00", -29.990, -29.992, -61.500, -61.501, 4.8, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-13 18:20:00", "2025-05-13 18:10:00", -30.500, -30.505, -62.800, -62.802, 6.0, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-12 09:00:00", "2025-05-12 08:55:00", -33.000, -33.001, -66.500, -66.501, 2.5, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-11 01:05:00", "2025-05-11 00:55:00", -31.250, -31.252, -64.050, -64.053, 5.9, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-10 16:30:00", "2025-05-10 16:15:00", -29.500, -29.501, -60.800, -60.803, 3.5, "Evento Sismico", "Bloqueado en revision", "", "", "", "", "", 0, 0],
            ["2025-05-09 04:40:00", "2025-05-09 04:30:00", -32.700, -32.705, -67.000, -67.008, 6.8, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0],
            ["2025-05-08 21:00:00", "2025-05-08 20:45:00", -30.000, -30.001, -63.000, -63.002, 4.0, "Evento Sismico", "Pendiente en revision", "", "", "", "", "", 0, 0]
        ]