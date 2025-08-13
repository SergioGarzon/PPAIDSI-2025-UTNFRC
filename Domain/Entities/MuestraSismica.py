from Domain.Entities.DetalleMuestraSismica import DetalleMuestraSismica

class MuestraSismica:
    
    def __init__(self, fecha_hora_muestra):
        self.fecha_hora_muestra = fecha_hora_muestra
        self.detalle_muestra_sismica = []

    def get_fecha_hora_muestra(self):
        return self.fecha_hora_muestra

    def agregar_detalle_muestra_sismica(self, muestra_info):
        self.detalle_muestra_sismica.append(muestra_info)

