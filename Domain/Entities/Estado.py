class Estado:
    
    def __init__(self):
        self.ambito = ""
        self.nombre_estado = ""

    def __init__(self, ambito, nombre_estado):
        self.ambito = ambito
        self.nombre_estado = nombre_estado

    def set_ambito(self, ambito):
        self.ambito = ambito
    
    def set_nombre_estado(self, nombre_estado):
        self.nombre_estado = nombre_estado

    def get_nombre_estado(self):
        return self.nombre_estado
    
    def get_ambito(self):
        return self.ambito 

    def es_ambito_evento_sismico(self):
        if self.ambito == "Evento Sismico":
            return self.ambito
    
    def esBloqEnRevision(self):
        if self.nombre_estado == "Bloqueado en revision":
            return self.nombre_estado


    
    