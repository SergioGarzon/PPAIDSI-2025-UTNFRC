class OrigenDeGeneracion:

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    # METODO 33 (Diagrama de secuencia)
    def get_nombre(self):
        return self.nombre