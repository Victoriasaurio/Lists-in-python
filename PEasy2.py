'''
Almacenar en una lista los nombres de los empleados de una
empresa junto a sus últimos 3 sueldo(estos 3 valores en
una tupla. El programa debe tener:
1. Cargar los nombres y los 3 sueldos.
2. Imprimir el monto total cobrado por cada empleados.
3. Imprimir el nombre de los empleados que tuvieron un 
ingreso trimestral mayor a 10000, en los últimos 3 meses.)
'''
lista = []
tupla = []

print(f"Elija una opción... \n1. INGRESAR: NOMBRES Y 3 SUELDOS. \n2. MONTO TOTAL. \n3. PERSONAS QUE RECIBIERON UN SUELDO MAYOR A LOS $10,000")
op = int(input("\nIngrese opción » "))

if op != 1 or 2 or 3:
    if op == 1:
        i = 1
        emp=""
        while i <= 5:
            suma=0
            name = input(f"Ingrese nombre del empleado {i} » ")
            lista.append(name)
            salary1 = float(input(f"Ingresar saldo No.1 » "))
            salary2 = float(input(f"Ingresar saldo No.2 » "))
            salary3 = float(input(f"Ingresar saldo No.3 » "))
            suma = (salary1 + salary2 + salary3)
            tupla.append((salary1,salary2,salary3, suma))
            i += 1
            print("")
        op = int(input("Ingrese opción » "))
    
    if op == 2:
        print("== El monto total de cada empleado ==")
        for s in range(3, len(lista)):
            if tupla[s][3] >
            print(f"El sueldo total del empleado {s} es » {tupla[]}")


            for x in range(1, len(lista)):
        if lista[x][1]>lista[pos][1]:
            pos = x

                '''
                print(f"El monto total del empleado {lista[s]} es » {tupla[f]}")
        op = int(input("\nIngrese opción » "))
    '''
    if op == 3:
        for p in range(len(lista)):
            for x in range(len(tupla)):
                if tupla[x] > 10000:
                    pos = tupla[x]
                    emp = lista[p]
                print(f"El empleado {emp} tiene un sueldo mayor a $10,000 pesos")
        op = int(input("\nIngrese opción » "))
else:
    exit()            