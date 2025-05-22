from Entities.EventoSismico import EventoSismico

class GestorRevManual:

    def __init__(self):
        self.eventos_sismicos_lista = []


    
    def nueva_revision_manual(self):        
        self.buscar_eventos_sismicos_auto()  
       


    def buscar_eventos_sismicos_auto(self):
      
        datos_para_varios_sismos = [
            ["2025-05-22 15:00:00", "2025-05-22 14:30:00", -31.416, -31.420, -64.183, -64.190, 6.5, "Evento Sismico", "Pendiente"],
            ["2025-05-21 10:15:00", "2025-05-21 10:00:00", -32.000, -32.010, -65.000, -65.005, 4.2, "Evento Sismico", "Pendiente"],
            ["2025-05-20 08:00:00", "2025-05-20 07:50:00", -33.500, -33.510, -66.100, -66.105, 7.1, "Evento Sismico", "Pendiente"],
            ["2025-05-19 23:00:00", "2025-05-19 22:45:00", -30.123, -30.125, -63.456, -63.458, 3.8, "Evento Sismico", "Bloqueado"],
            ["2025-05-18 07:00:00", "2025-05-18 06:30:00", -29.000, -29.010, -62.000, -62.005, 5.0, "Evento Sismico", "Pendiente"]
        ]

        self.eventos_sismicos_lista = []

        for datos_evento in datos_para_varios_sismos:
            evento = EventoSismico(*datos_evento)

            if evento.es_pendiente_revision():
                self.eventos_sismicos_lista.append(evento)
     
        self.ordenarEventosSismicos()




    def ordenarEventosSismicos(self):        
        self.eventos_sismicos_lista.sort(key=lambda evento: evento.get_fecha_hora_ocurrencia())       


    def obtener_eventos_para_mostrar(self):        
        return self.eventos_sismicos_lista
    
    def tomarSeleccionEvento():
        pass
    
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