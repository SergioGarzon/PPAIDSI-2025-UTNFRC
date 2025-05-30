class Estado:
    
    def __init__(self, ambito, nombre_estado):
        self.ambito = ambito
        self.nombre_estado = nombre_estado
    
    def get_ambito(self):
        return self.ambito
    
    # METODO 8 (Diagrama de secuencia)
    def es_pendiente_revision(self):
        control = False

        if(self.nombre_estado == 'Pendiente de revision'):
            return True
        
        return control
   
    # METODO 59 (Diagrama de secuencia)
    def es_rechazado(self):
        control = False

        if(self.nombre_estado == 'Rechazado'):
            return True
        
        return control
    
    # METODO 20 (Diagrama de secuencia)
    # METODO 58 (Diagrama de secuencia)
    def es_ambito_evento_sismico(self):
        control = False 

        if self.ambito == "Evento Sismico":
            control = True

        return control
    
    # METODO 21 (Diagrama de secuencia)
    def es_bloq_en_revision(self):
        control = False

        if self.nombre_estado == "Bloqueado en revision":
            control = True
        
        return control


    def get_nombre_estado(self):
        return self.nombre_estado       


    
    