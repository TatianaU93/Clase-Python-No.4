'''
from empleado import Empleado

e1 = Empleado ()
e1.setNombre("Jonathan")
e1.apellido = "Campos Lozano"
e1.cargo = "profesor"
e1.salario = "20000"

print(e1)

e2 = Empleado ()
e2.setNombre("María")
e2.apellido = "Cardenas"
e2.cargo = "Gerente"
e2.salario = "5000000"

print(e2)

e3 = Empleado ()
e3.setNombre("Camilo")
e3.apellido = "Cardenas"
e3.cargo = "Gerente 2"
e3.salario = "5000000"

print(e3)
'''
'''
from Indicadores ()

print('TRM=',i.trm())
print('Salario minimo =', i.salariominimo()
)
'''

from nomina import Nomina

listaNomina = []

while True: 
    print("1. Calcular Nomina")
    print("10. Salir") 
    respuesta = input("Ingrese la opcion =  ")

    if respuesta == "1":
        renglon = [] 
        n = Nomina ()
        n.setSalario(float(input("Ingrese el salario basico: ")))
        n.setDiasLiquidados(int(input("Ingrese los dias liquidadas: ")))

        renglon.append({'variable':'Salario', 'resultado': n.getSalario()})
        renglon.append({'variable':'Dias Liqidados', 'resultado': n.getDiasLiquidados()})
        renglon.append({'variable':'Salario Devengado', 'resultado': n.SalarioDevengado()})
        renglon.append({'variable':'Auxilio de Transporte', 'resultado': n.auxiliodetransporte()})
        renglon.append({'variable':'Total Devengado', 'resultado': n.totalDevengado()})
        listaNomina.append(renglon)

    elif respuesta == "10":
        print("Saliendo")
        break

f = open('nomina_python.txt','w')
for i in listaNomina:
    f.write('--------------------------------- \n')
    for j in i:
        f.write(str(j) +'\n')
f.close()



