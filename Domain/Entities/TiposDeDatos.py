class TiposDeDatos:

    def __init__(self, denominacion, nombre_unidad_medida, valor_umbral):
        self.denominacion = denominacion
        self.nombre_unidad_medida = nombre_unidad_medida
        self.valor_umbral = valor_umbral

    def es_tu_denominacion(self):
        pass

    # METODO 40 (Diagrama de secuencia) 
    def get_denominacion(self):
        return self.denominacion
    
    def get_nombre_unidad_medida(self):
        return self.nombre_unidad_medida
    
    def get_valor_umbral(self):
        return self.valor_umbral   