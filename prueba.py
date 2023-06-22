class Vehiculo:
    def __init__(self, tipo, patente, marca, precio, multas, fecha_registro, dueno):
        self.tipo = tipo
        self.patente = patente
        self.marca = marca
        self.precio = precio
        self.multas = multas
        self.fecha_registro = fecha_registro
        self.dueno = dueno

vehiculos = []

def grabar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo: ")
    patente = input("Ingrese la patente: ")
    marca = input("Ingrese la marca: ")
    precio = int(input("Ingrese el precio: "))
    multas = []
    fecha_registro = input("Ingrese la fecha de registro: ")
    dueno = input("Ingrese el nombre del dueño: ")

    # Verificar que la patente sea correcta
    # Aquí puedes implementar la lógica de validación de patente según las reglas de tu país

    if len(marca) < 2 or len(marca) > 15:
        print("La marca debe tener entre 2 y 15 caracteres.")
        return

    if precio <= 5000000:
        print("El precio debe ser mayor a $5.000.000.")
        return

    vehiculo = Vehiculo(tipo, patente, marca, precio, multas, fecha_registro, dueno)
    vehiculos.append(vehiculo)
    print("Vehículo registrado con éxito.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo a buscar: ")

    for vehiculo in vehiculos:
        if vehiculo.patente == patente:
            print("Tipo:", vehiculo.tipo)
            print("Marca:", vehiculo.marca)
            print("Precio:", vehiculo.precio)
            print("Multas:", vehiculo.multas)
            print("Fecha de registro:", vehiculo.fecha_registro)
            print("Dueño:", vehiculo.dueno)
            return

    print("Vehículo no encontrado.")

def imprimir_certificados():
    for vehiculo in vehiculos:
        certificado_emision = round(random.uniform(1500, 3500), 2)
        certificado_anotaciones = round(random.uniform(1500, 3500), 2)
        certificado_multas = round(random.uniform(1500, 3500), 2)

        print("Certificado de Emisión de Contaminantes")
        print("Patente:", vehiculo.patente)
        print("Dueño:", vehiculo.dueno)
        print("Valor: $", certificado_emision)

        print("Certificado de Anotaciones Vigentes")
        print("Patente:", vehiculo.patente)
        print("Dueño:", vehiculo.dueno)
        print("Valor: $", certificado_anotaciones)

        print("Certificado de Multas")
        print("Patente:", vehiculo.patente)
        print("Dueño:", vehiculo.dueno)
        print("Valor: $", certificado_multas)

def main():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    version = "1.0"

    print("Bienvenido(a) a Auto Seguro - Sistema de Registro de Vehículos")
    print("Versión:", version)
    print("Desarrollado por:", nombre, apellido)

    while True:
        print("\nMenú:")
        print("1. Grabar vehículo")
        print("2. Buscar vehículo")
        print("3. Imprimir certificados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            grabar_vehiculo()
        elif opcion == "2":
            buscar_vehiculo()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            print("Gracias por utilizar Auto Seguro. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()