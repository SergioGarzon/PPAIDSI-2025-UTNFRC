from Domain.Entities.TiposDeDatos import TiposDeDatos

class DetalleMuestraSismica:

    def __init__(self, valor, denominacion, nombre_unidad_medida, valor_umbral):
        self.valor = valor
        self.tipos_datos = TiposDeDatos(denominacion, nombre_unidad_medida, valor_umbral)

    def get_valor(self):
        return self.valor
    
    def get_tipos_datos(self):
        return self.tipos_datos
  
    
