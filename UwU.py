import os, time, csv
from funciones import *


while True:

    menu()
    while True:
        try:
            opt=int(input("seleccione su opción: "))
            if opt in(1,2,3,4,5):
                break
            else:
                os.system('cls')
                print("debe seleccionar una de las opciones indicadas(1,2,3,4,5)")
        except:
            os.system('cls')
            print("la opcion debe ser un numero entero")

    if opt==1:
        bus=[["o","o","o","o"],
         ["o","o","o","o"],
         ["o","o","o","o"],
         ["o","o","o","o"],
         ["o","o","o","o"],
         ["o","o","o","o"],
         ["o","o","o","o"]
        ]
        for x in range(len(bus)):
            print(bus[x])
            
        print("los asientos disponibles se presentan con un o")

    elif opt == 2:
        while True:
            try:
                fila = int(input("Seleccione una fila (1-7): ")) - 1
                if fila in range(7):
                    break
                else:
                    print("Debe seleccionar una fila válida (1-7)")
            except ValueError:
                print("La fila seleccionada debe ser un número entero.")

        while True:
            try:
                asiento = int(input("Seleccione un asiento en la fila seleccionada (1-4): ")) - 1
                if asiento in range(4):
                    break
                else:
                    print("Debe seleccionar un asiento válido (1-4)")
            except ValueError:
                print("El asiento seleccionado debe ser un número entero.")

        # Verificar si el asiento está disponible
        if bus[fila][asiento] == "o":
            bus[fila][asiento] = "x"  # Cambiar "o" por "x" (indicativo de asiento reservado)
            print(f"¡Asiento en fila {fila + 1}, asiento {asiento + 1} reservado!")
        else:
            print("Este asiento ya está ocupado. Seleccione otro.")

        input("Presione Enter para continuar...")
          
    elif opt==3:
        pass
    elif opt==4:
        pass
    else:
        print("CHAO CTM")

    