class Estado:
    
    def __init__(self, ambito, nombre_estado):
        self.ambito = ambito
        self.nombre_estado = nombre_estado
    
    def get_ambito(self):
        return self.ambito
    
    # METODO 8 (Diagrama de secuencia)
    def es_pendiente_revision(self):
        control = False

        while(self.nombre_estado == 'Pendiente de revision'):
            return True
        
        return control
   
   # METODO 20 (Diagrama de secuencia)
    def es_ambito_evento_sismico(self):
        if self.ambito == "Evento Sismico":
            return self.ambito
    
    # METODO 21 (Diagrama de secuencia)
    def es_bloq_en_revision(self):
        while self.nombre_estado == "Bloqueado en revision":
            return self.nombre_estado        


    
    