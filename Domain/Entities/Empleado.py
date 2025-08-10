class Empleado:

    def __init__(self, nombre, apellido, mail, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono

    def obtener_mail(self):
        return self.mail

    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido

    def get_mail(self):
        return self.mail

    def get_telefono(self):
        return self.telefono
    
    def es_responsable_de_reparacion(self):
        pass