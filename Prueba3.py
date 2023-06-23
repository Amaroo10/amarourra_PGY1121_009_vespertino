import random, re

vehiculos=[]

def grabar_vehiculo():
    print("\n**GRABAR VEHICULO**\n")
    opciones=["Moto", "moto", "Auto", "auto", "Camioneta", "camioneta", "Furgon", "furgon", "Furgón", "furgón", "Camion", "camion", "camión", "Camión", "Bus", "bus"]
    while True:
        tipo_vehiculo=input("Ingrese el tipo de vehículo (Moto, Auto, Camioneta, Furgón, Camión o Bus): ")
        if tipo_vehiculo in opciones:
            break
        else:
            print("Tipo de vehículo no válido. Intenta nuevamente")
    
    while True:
        patente = input("Ingrese la patente (Ej. AAA-111 o AA-1111): ")
        if re.match(r'^[A-Z]{2}-\d{4}$', patente) or re.match(r'^[A-Z]{3}-\d{3}$', patente):
            break
        else:
            print("La patente ingresada no es válida. Intenta nuevamente.")

    while True:
        marca=input("Ingrese la marca: ")
        if len(marca)>=2 and len(marca)<=15:
            break
        else:
            print("La marca debe tener entre 2 y 15 caracteres. Intente nuevamente.")

    while True:
        precio=int(input("Ingrese el precio($): "))
        if precio>5000000:
            break
        else:
            print("El precio debe ser mayor a $5.000.000. Intenta nuevamente")
    
    multas=input("¿Posee multas? si/no: ")
    if multas=="si":
        valor_multa=int(input("Ingrese el valor de la multa($): "))
        fecha_multa=input("Ingrese la fecha de la multa: ")
        while True:
            multa=input("Desea agregar otra multa? si/no: ")
            if multa=="no":
                break
            else:
                valor_multa=int(input("Ingrese el valor de la multa($): "))
                fecha_multa=input("Ingrese la fecha de la multa: ")
        
    fecha_registro = input("Ingrese le fecha de registro del vehículo: ")   
    nombre_dueño=input("Ingrese el nombre del dueño: ")
    print("Vehiculo grabado exitosamente!!")

    vehiculo=(tipo_vehiculo, patente, marca, precio, multas, fecha_registro, nombre_dueño)

    vehiculos.append(vehiculo)

def buscar_vehiculo():
    print("\n**BUSCAR VEHICULO**")
    buscar_patente=input("Ingrese la patente del vehiculo (Ej. AAA-111 o AA-1111): ")
    for vehiculo in vehiculos:
        if buscar_patente==vehiculo[1]:
            print("\nTipo de vehículo: ", vehiculo[0])
            print("Patente: ", vehiculo[1])
            print("Marca: ", vehiculo[2])
            print("Precio: $", vehiculo[3])
            print("Multas: ", vehiculo[4])
            print("Fecha de registro: ", vehiculo[5])
            print("Nombre del dueño: ", vehiculo[6])
        else:
            print("La patente no se encuentra en el registro")

def imprimir_certificado():
    print("\n**IMPRIMIR CERTIFICADOS**")
    busca_patente=input("Ingresa la patente del vehiculo (Ej. AAA-111 o AA-1111): ")
    for vehiculo in vehiculos:
        if busca_patente==vehiculo[1]:
            print("\n==Bienvenido al sistema de impresión de certificados==")
            certificado=input("1- Certificado de emisión de contaminantes\n2- Certificado de anotaciones vigente\n3- Certificado de multas\nElige una opción: ")
            if certificado=="1":
                print("\n**Certificado de emisión de contaminantes**")
                print("Valor: $", random.randint(1500, 3500))
                print("Patente: ", vehiculo[1])
                print("Nombre del dueño: ", vehiculo[6])
            if certificado=="2":
                print("\n**Certificado de anotaciones vigentes**")
                print("Valor: $", random.randint(1500, 3500))
                print("Patente: ", vehiculo[1])
                print("Nombre del dueño: ", vehiculo[6])
            if certificado=="3":
                print("\n**Certificado de multas**")
                print("Valor: $", random.randint(1500, 3500))
                print("Patente: ", vehiculo[1])
                print("Nombre del dueño: ", vehiculo[6])

def salir():
    print("\nGracias por utilizar el sistema Auto Seguro!! Hasta pronto!!\n\n\n")

def datos():
    nombre = "\nCreado por: Felipe Echeverria"
    version = "Versión 1.0"
    print(nombre)
    print(version)
    
while True:
    print("\n==BIENVENIDO AL SISTEMA AUTO SEGURO==\n")
    print("1- Grabar vehículo")
    print("2- Buscar vehículo")
    print("3- Imprimir certificados")
    print("4- Salir")
    opcion=input("Ingrese una opción: ")

    if opcion=="1":
        grabar_vehiculo()
    if opcion=="2":
        buscar_vehiculo()
    if opcion=="3":
        imprimir_certificado()
    if opcion=="4":
        salir()
        datos()
        break
