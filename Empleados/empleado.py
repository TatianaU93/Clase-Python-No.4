


class Empleado:
    
    def __init__(self):
        self.__nombre = None  #No reconoce el nombre con las dos lineas al piso
        self.apellido = None
        self.cargo = None 
        self.salario = None 

def getNombre(self):
    return self.__nombre

def setNombre(self, nombre):
    self.__nombre = nombre 

    def __str__(self):
        return str("nombre: {} \n"
            "apellido: {} \n"
            "cargo: {} \n"
            "salario: {} \n").format(
                self.nombre,
                self.apellido,
                self.cargo,
                self.salario)