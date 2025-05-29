from Domain.Entities.TiposDeDatos import TiposDeDatos

class DetalleMuestraSismica:

    def __init__(self, valor, denominacion, nombre_unidad_medida, valor_umbral):
        self.valor = valor
        self.tipos_datos = TiposDeDatos(denominacion, nombre_unidad_medida, valor_umbral)

    # METODO 38 (Diagrama de secuencia)
    def get_datos(self):
        # METODO 39 (Diagrama de secuencia)
        return [self.valor, self.tipos_datos.get_denominacion()]
        
    
