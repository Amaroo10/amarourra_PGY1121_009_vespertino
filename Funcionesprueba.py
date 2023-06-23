import FUNCIONES as fn;
import time;
print("Bienvenido al sistema de Auto Seguro\n------------------------------------");
while True:
    print("\nSeleccione opción:\n\t1. Grabar\n\t2. Buscar\n\t3. Imprimir Certificados\n\t4. Salir\n");
    print("Opción: ", end="");
    op=input();
    if op=='1': fn.grabar();
    elif op=='2': fn.buscar();
    elif op=='3': fn.certificados();
    elif op=='4': 
        print("Gracias por usar la aplicación Auto Seguro.\nVersión 1.0 - Desarrollada por Matías Morales Inzulza\n")
        print("Cerrando...")
        time.sleep(2)
        break;
    else: print("La opción ingresada no es válida\n");
