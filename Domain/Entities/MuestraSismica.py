from Domain.Entities.DetalleMuestraSismica import DetalleMuestraSismica

class MuestraSismica:
    
    def __init__(self, fecha_hora_muestra):
        self.fecha_hora_muestra = fecha_hora_muestra
        self.detalle_muestra_sismica = None
        self.detalle_muestra_sismica_lista = []

    def get_fecha_hora_muestra(self):
        return self.fecha_hora_muestra

    def agregar_detalle_muestra_sismica(self, muestra_info):
        self.detalle_muestra_sismica = DetalleMuestraSismica(muestra_info.get_valor(), muestra_info.get_tipos_datos().get_denominacion(), muestra_info.get_tipos_datos().get_nombre_unidad_medida(), muestra_info.get_tipos_datos().get_valor_umbral())
        self.detalle_muestra_sismica_lista.append(self.detalle_muestra_sismica)

    def get_detalle_muestra_sismica(self):
        return self.detalle_muestra_sismica_lista