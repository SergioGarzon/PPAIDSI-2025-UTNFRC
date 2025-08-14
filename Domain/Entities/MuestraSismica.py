from Domain.Entities.DetalleMuestraSismica import DetalleMuestraSismica

class MuestraSismica:
    
    def __init__(self, fecha_hora_muestra):
        self.fecha_hora_muestra = fecha_hora_muestra
        self.detalle_muestra_sismica = None
        self.detalle_muestra_sismica_lista = []

    def get_fecha_hora_muestra(self):
        return self.fecha_hora_muestra

    def agregar_detalle_muestra_sismica(self, muestra_info):
        self.detalle_muestra_sismica = muestra_info
        self.detalle_muestra_sismica_lista.append(self.detalle_muestra_sismica)

    def get_detalle_muestra_sismica(self):
        return self.detalle_muestra_sismica_lista

    # METODO 38 (Diagrama de secuencia)
    def get_datos(self):

        lista_aux = []
        
        for i in self.get_detalle_muestra_sismica():
            # METODO 39 (Diagrama de secuencia) 
            lista_aux.append(i.get_datos())
            
        lista_enviar = [self.get_fecha_hora_muestra(), lista_aux]
        
        return lista_enviar