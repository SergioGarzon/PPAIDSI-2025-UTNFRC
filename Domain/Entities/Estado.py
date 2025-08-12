class Estado:
    
    def __init__(self, ambito, nombre_estado):
        self.ambito = ambito
        self.nombre_estado = nombre_estado
    
    def get_ambito(self):
        return self.ambito

    def get_nombre_estado(self):
        return self.nombre_estado       


    # METODO 8 (Diagrama de secuencia)
    def es_pendiente_revision(self):
        return (self.nombre_estado == 'Pendiente de revision')