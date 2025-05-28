class ClasificacionSismo:

    def __init__(self, nombre, kilometro_profundidad_desde, kilometro_profundidad_hasta):
        self.nombre = nombre
        self.kilometro_profundidad_desde = kilometro_profundidad_desde
        self.kilometro_profundidad_hasta = kilometro_profundidad_hasta

    # METODO 34 (Diagrama de secuencia)
    def get_nombre(self):
        return self.nombre