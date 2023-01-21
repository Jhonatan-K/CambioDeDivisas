def change_pesosC_dolar(pesoC): # funcion de cambio P a D
    return pesoC/4802.67

def changeDolar_pesosC(dolar): # funcion de cambio D a P
    return dolar*4802.67

print("\tBienvenido \nCambio de Divisas") # bienvenida y menu con bucle
while True:
    print('''\t.:MENU:.
1. Convertir Peso Colombiano a Dólares
2. Convertir de Dólares a Peso Colombiano
3. Salir''')
    options = int(input('Digite una opcion: '))
    
    print()
    
    if options ==1: # pedir cantidad de pesos hacia dolar
        pesoC = float(input("Digite la cantidad de Pesos Colombianos: "))
        print(f'Dólar -> ${change_pesosC_dolar(pesoC):.2f}') # funcion
    
    elif options ==2: # pedir cantidad de dolar a peso
        dolar = float(input("Digite la cantidad de Dólares: "))
        print(f'Pesos Colombianos -> ${changeDolar_pesosC(dolar):.2f}') # funcion
        
    elif options ==3: # salir
        print("Gracias por usar el cambio de divisas")
        break # romper bucle
        
    else: # mensaje de error
        print('\t Error!\nSe equivoco de opcion de menu')
print()