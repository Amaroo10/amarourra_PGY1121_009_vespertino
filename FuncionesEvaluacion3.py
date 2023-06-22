import random

def grabar_vehiculo(registro):
    while True:
        tipo = input("Tipo de vehiculo: ")

        patente = input("Ingrese la patente: ")
        while len(patente) != 6:
            print("La patente debe tener 6 caracteres.")
            patente = input("Ingrese la patente: ")
        marca = input("Ingrese la marca del vehiculo: ")
        while len(marca) < 2 or len(marca) > 15:
            print("La marca debe tener entre 2 y 15 caracteres.")
            marca = input("Ingrese la marca del vehiculo: ")
        precio = input("Precio: ")
        while not precio.isdigit() or int(precio) <= 5000000:
            print("El precio debe ser mayor a $5.000.000 (Ingresar solo numeros).")
            precio = input("Precio: ")
        fecha_registro = input("Fecha de registro (DD/MM/AAAA): ")
        multas = []
        while True:
            tiene_multas = input("Posee multas? (S/N): ")
            if tiene_multas.upper() == "S":
                cantidad_multas = int(input("Ingrese la cantidad de multas: "))
                for i in range(cantidad_multas):
                    fecha_multa = input(f"Fecha de la multa {i+1}: ")
                    monto_multa = input("Monto de la multa: ")
                    multas.append({"Fecha": fecha_multa, "Monto": monto_multa})
                break       
            elif tiene_multas.upper() == "N":
                break
            else:
                print("Respuesta invalida. Por favor ingrese 'S' para si o 'N' para no (En mayusculas).")
        nombre_dueno = input("Nombre del dueño: ")

        registro[patente] = {
            "Tipo": tipo,
            "Marca": marca,
            "Precio": int(precio),
            "Multas": multas,
            "Fecha de registro": fecha_registro,
            "Nombre del dueño": nombre_dueno
        }
        print("Vehiculo registrado exitosamente.")
        break

def buscar_vehiculo(registro):
    patente = input("Ingrese la patente del vehiculo a buscar: ")
    
    if patente in registro:
        vehiculo = registro[patente]
        print("Informacion del vehiculo:")
        print(f"Nombre del dueño: {vehiculo['Nombre del dueño']}")
        print(f"Patente: {patente}")
        print(f"Marca: {vehiculo['Marca']}")
        print(f"Tipo: {vehiculo['Tipo']}")
        print(f"Precio: {vehiculo['Precio']}")
        print(f"Fecha de registro: {vehiculo['Fecha de registro']}")
        print("Multas:")
        if len(vehiculo['Multas']) > 0:
            i = 1
            for multa in vehiculo['Multas']:
                print(f"Fecha multa {i}: {multa['Fecha']}\nMonto: {multa['Monto']}")
                i += 1
        else:
            print("El vehículo no tiene multas registradas.")
    else:
        print("No se encontro ningun vehiculo con la patente ingresada.")

def imprimir_certificados(registro):
    patente = input("Ingrese la patente del vehiculo para imprimir los certificados: ")
    
    if patente in registro:
        vehiculo = registro[patente]
        certificado_emision = random.randint(1500, 3500)
        certificado_anotaciones = random.randint(1500, 3500)
        certificado_multas = random.randint(1500, 3500)
        
        while True:
            print("\nMenu Certificados.")
            print("1. Certificado de Emision de contaminantes")
            print("2. Certificado de anotaciones vigentes")
            print("3. Certificado de multas")
            print("4. Volver")
            
            opcion = input("Seleccione el certificado a imprimir: ")
            
            if opcion == "1":
                print("\nCertificado de Emision de contaminantes:")
                print(f"Patente del auto: {patente}")
                print(f"Dueño actual: {vehiculo['Nombre del dueño']}")
                print(f"Valor del certificado: ${certificado_emision}")
            elif opcion == "2":
                print("\nCertificado de anotaciones vigentes:")
                print(f"Patente del auto: {patente}")
                print(f"Dueño actual: {vehiculo['Nombre del dueño']}")
                print(f"Valor del certificado: ${certificado_anotaciones}")
            elif opcion == "3":
                print("\nCertificado de multas:")
                print(f"Patente del auto: {patente}")
                print(f"Dueño actual: {vehiculo['Nombre del dueño']}")
                print(f"Valor del certificado: ${certificado_multas}")
            elif opcion == "4":
                print("Volviendo al menu principal...")
                break
            else:
                print("Opción invalida. Intente nuevamente.")
    else:
        print("No se encontro ningun vehiculo con la patente ingresada.")
