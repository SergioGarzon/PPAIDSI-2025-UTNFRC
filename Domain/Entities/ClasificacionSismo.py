class ClasificacionSismo:

    def __init__(self, nombre, kilometro_profundidad_desde, kilometro_profundidad_hasta):
        self.nombre = nombre
        self.kilometro_profundidad_desde = kilometro_profundidad_desde
        self.kilometro_profundidad_hasta = kilometro_profundidad_hasta

    def get_nombre(self):
        return self.nombre
    
    def get_kilometro_profundidad_desde(self):
        return self.kilometro_profundidad_desde
    
    def get_kilometro_profundidad_hasta(self):
        return self.kilometro_profundidad_hasta