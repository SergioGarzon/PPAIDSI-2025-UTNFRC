from Domain.Entities.DetalleMuestraSismica import DetalleMuestraSismica

class MuestraSismica:
    
    def __init__(self, fecha_hora_muestra):
        self.fecha_hora_muestra = fecha_hora_muestra

    # METODO 36 (Diagrama de secuencia)
    def get_datos(self):
        # METODO 37 (Diagrama de secuencia)
        self.crear_detalle_muestra()

        lista_dt = []

        for lista in self.lista_detalle_muestra:
            lista_dt.append(lista.get_datos())

        return [self.fecha_hora_muestra, lista_dt]
    

    def crear_detalle_muestra(self):
        self.lista_detalle_muestra = []

        lista_aux_dtmuestra = [
            ["valor 1", "ninguna 1", "ninguna unidad 1", 10],
            ["valor 2", "ninguna 2", "ninguna unidad 2", 10],
            ["valor 3", "ninguna 3", "ninguna unidad 3", 10],
            ["valor 4", "ninguna 4", "ninguna unidad 4", 10],
            ["valor 5", "ninguna 5", "ninguna unidad 5", 10],
            ["valor 6", "ninguna 6", "ninguna unidad 6", 10],
        ]

        for datos_dtmuestra in lista_aux_dtmuestra:
            self.dt_muestra = DetalleMuestraSismica(*datos_dtmuestra)
            self.lista_detalle_muestra.append(self.dt_muestra)