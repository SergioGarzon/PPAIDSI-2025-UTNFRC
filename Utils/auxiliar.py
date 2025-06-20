from Domain.Entities.EventoSismico import EventoSismico



class Auxiliar:

    def obtener_list_series(self):
        return EventoSismico.devolver_series_temporales(self)
    
