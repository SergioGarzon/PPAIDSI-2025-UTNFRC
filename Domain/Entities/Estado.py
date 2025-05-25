class Estado:

    def __init__(self, ambito, nombre_estado):
        self.ambito = ambito
        self.nombre_estado = nombre_estado

    def get_nombre_estado(self):
        return self.nombre_estado
    
    def get_ambito(self):
        return self.ambito            
    
    