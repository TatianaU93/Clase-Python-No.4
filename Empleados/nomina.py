from indicadores import Indicadores

class Nomina (Indicadores):

    def __init__(self):
        self.__salarioBasico = 0
        self.__diaslLiquidado = 0
        self.__auxiliodetransporte = 106454
        self.__smmlv = self.salariominimo() 

    def setSalario(self, salarioBasico:float):
        #self.__salarioBasico = salarioBasico
        if str(type(salarioBasico)) == "<class 'float'>" or str(type(salarioBasico))== "<class 'int'>":
            if self.__smmlv<= salarioBasico:
                self.__salarioBasico = salarioBasico
            else:
                print("El salario Básico no puede ser inferior al SMMLV (Salario Minimo Mensual Legal Vigente)")
        else:
            print("Error")
        

    def getSalario(self):
        return self.__salarioBasico

    def setDiasLiquidados(self, diasLiquidados:int):
        self.__diasLiquidados = diasLiquidados
    
    def getDiasLiquidados(self):
        return self.__diasLiquidados
    
    def SalarioDevengado(self):
        try:
            return (self.__salarioBasico/30)*self.__diasLiquidados
        except:
            print("Error en alguna de las variables")
        
    def auxiliodetransporte(self):
        if self.__salarioBasico > (self.__smmlv *2):
            return 0
        else:
            return (self.__auxiliodetransporte/30 * self.__diasLiquidados)

    def totalDevengado(self):
        return self.SalarioDevengado() + self.auxiliodetransporte()
    def __str__(self):
        return str("salario Basico: {} \n"
                    "dias Liquidados: {} \n"
                    "Salario Devengado: {} \n"
                    "Auxilio de transporte: {} \n"
                    "Total Devengado: {} \n").format(
                        self.__salarioBasico,
                        self.__diasLiquidados,
                        self.SalarioDevengado(),
                        self.auxiliodetransporte(),
                        self.totalDevengado())


