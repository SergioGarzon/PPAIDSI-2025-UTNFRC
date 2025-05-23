from Entities.EventoSismico import EventoSismico
from datetime import datetime 

class GestorRevManual:

    def __init__(self):
        self.eventos_sismicos_lista = []
        self.eventos_sismicos_lista_vista = []
        self.datos_para_varios_sismos = []
        self.evento_seleccionado = None
    
    def nueva_revision_manual(self):        
        self.buscar_eventos_sismicos_auto()   

    def buscar_eventos_sismicos_auto(self):             
        self.generar_lista_datos()

        self.eventos_sismicos_lista = []

        for datos_evento in self.datos_para_varios_sismos:
            evento = EventoSismico(*datos_evento)

            if evento.es_pendiente_revision():
                self.eventos_sismicos_lista.append(evento)
     
        self.ordenarEventosSismicos()

    def ordenarEventosSismicos(self):        
        self.eventos_sismicos_lista.sort(key=lambda evento: evento.get_fecha_hora_ocurrencia(), reverse=True)

        for i, evento in enumerate(self.eventos_sismicos_lista):
            fecha_ocurrencia_str = evento.get_fecha_hora_ocurrencia().strftime("%d/%m/%Y")
            hora_ocurrencia_str = evento.get_fecha_hora_ocurrencia().strftime("%H:%M:%S")

            ubicacion_str = f"Lat: {evento.get_latitud_epicentro()} Lon: {evento.get_longitud_epicentro()}"
            magnitud_str = f"{evento.get_valor_magnitud()}°"

            fila_formateada = (fecha_ocurrencia_str, hora_ocurrencia_str, ubicacion_str, magnitud_str)
            self.eventos_sismicos_lista_vista.append(fila_formateada)


    def obtener_eventos_para_mostrar(self):        
        return self.eventos_sismicos_lista_vista
    
    def tomar_seleccion_evento(self, item_values):
        
        fecha_evento_str = item_values[1]
        hora_evento_str = item_values[2]
        ubicacion_str = item_values[3]
        magnitud_str = item_values[4]

        fecha_hora_combinada_str = f"{fecha_evento_str} {hora_evento_str}"

        try:
            fecha_hora_ocurrencia_dt = datetime.strptime(fecha_hora_combinada_str, "%d/%m/%Y %H:%M:%S")
        except ValueError as e:
            fecha_hora_ocurrencia_dt = None 
       
        latitud_epicentro = ubicacion_str[5:11]
        longitud_epicentro = ubicacion_str[16:23]
        magnitud = float(magnitud_str[:-1])

        print("\n\n\nSe ha seleccionado "+
                "\nUbicacion latitud epicentro: " +str(latitud_epicentro) +
                "\nUbicacion longitud epicentro: " + str(longitud_epicentro) +
                "\nfecha y hora ocurrencia: "+str(fecha_hora_ocurrencia_dt)+
                "\nMagnitud: " + str(magnitud)
        )

      
    def buscarEstadoBloqEnRevision():
        pass
    
    def get_fecha_hora_actual():
        pass

    def bloq_evento_sismico():
        pass

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

    def generar_lista_datos(self):
        self.datos_para_varios_sismos = [
            ["2025-05-22 15:00:00", "2025-05-22 14:30:00", -31.416, -31.420, -64.183, -64.190, 6.5, "Evento Sismico", "Pendiente"],
            ["2025-05-21 10:15:00", "2025-05-21 10:00:00", -32.000, -32.010, -65.000, -65.005, 4.2, "Evento Sismico", "Pendiente"],
            ["2025-05-20 08:00:00", "2025-05-20 07:50:00", -33.500, -33.510, -66.100, -66.105, 7.1, "Evento Sismico", "Pendiente"],
            ["2025-05-19 23:00:00", "2025-05-19 22:45:00", -30.123, -30.125, -63.456, -63.458, 3.8, "Evento Sismico", "Bloqueado"],
            ["2025-05-18 07:00:00", "2025-05-18 06:30:00", -29.000, -29.010, -62.000, -62.005, 5.0, "Evento Sismico", "Pendiente"],
            ["2025-05-17 02:30:00", "2025-05-17 02:00:00", -30.880, -30.885, -64.550, -64.552, 2.9, "Evento Sismico", "Pendiente"],
            ["2025-05-16 11:45:00", "2025-05-16 11:30:00", -31.700, -31.705, -63.900, -63.903, 5.5, "Evento Sismico", "Pendiente"],
            ["2025-05-15 20:00:00", "2025-05-15 19:50:00", -32.120, -32.125, -65.300, -65.305, 3.1, "Evento Sismico", "Bloqueado"],
            ["2025-05-14 05:10:00", "2025-05-14 05:00:00", -29.990, -29.992, -61.500, -61.501, 4.8, "Evento Sismico", "Pendiente"],
            ["2025-05-13 18:20:00", "2025-05-13 18:10:00", -30.500, -30.505, -62.800, -62.802, 6.0, "Evento Sismico", "Pendiente"],
            ["2025-05-12 09:00:00", "2025-05-12 08:55:00", -33.000, -33.001, -66.500, -66.501, 2.5, "Evento Sismico", "Pendiente"],
            ["2025-05-11 01:05:00", "2025-05-11 00:55:00", -31.250, -31.252, -64.050, -64.053, 5.9, "Evento Sismico", "Pendiente"],
            ["2025-05-10 16:30:00", "2025-05-10 16:15:00", -29.500, -29.501, -60.800, -60.803, 3.5, "Evento Sismico", "Bloqueado"],
            ["2025-05-09 04:40:00", "2025-05-09 04:30:00", -32.700, -32.705, -67.000, -67.008, 6.8, "Evento Sismico", "Pendiente"],
            ["2025-05-08 21:00:00", "2025-05-08 20:45:00", -30.000, -30.001, -63.000, -63.002, 4.0, "Evento Sismico", "Pendiente"]
        ]