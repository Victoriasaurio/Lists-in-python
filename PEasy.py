'''
Store in a elements list with the name of a country and 
amount of inhabitants.
Definir 3 funciones:
1. Ingresar elementos
2. Imprimir elementos
3. Mostrar el país con mayor cantidad de habitantes.
'''
lista = []
i = 1

print("\n1. Enter elements \n2. Print elements \n3. Show country with largest quantity \n4. Salir")
op = int(input("Enter opción » "))

if op == 1:
    n = int(input("Amount of countries and inhabitants » "))
    print("")
    while i <= n:
        country = input("Name country » " )
        inhabitants = int(input("Amount inhabitants » "))
        print("")
        lista.append((country, inhabitants))
        i += 1
    op = int(input("Enter opción » "))

if op == 2:
    print("\nCountries and Inhabitants")
    for x in range(len(lista)):
        print(lista[x])
    
    op = int(input("\nEnter opción » "))

if op == 3:
    pos = 0
    for x in range(1, len(lista)):
        if lista[x][1]>lista[pos][1]:
            pos = x
    print(f"Country with largest quantity is {lista[pos][0]}")
    op = int(input("\nEnter opción » "))

if op == 4:
    exit()