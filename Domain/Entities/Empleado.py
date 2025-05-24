class Empleado:

    def __init__(self, nombre, apellido, mail, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono

    def obtener_mail(self):
        return self.mail
    
    def es_responsable_de_reparacion(self):
        return 0