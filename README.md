
# prueba 3

3ra evaluacion parcial del primer semestre de Ingenieria Informatica DUOC UC Sede Plaza Norte.
## Contexto:

#### Se plantea la siguiente situacion:

La automotora “Auto Seguro” necesita registrar todos los datos de los vehículos que en este periodo tienen a la venta. En el registro de vehículos que pertenece a la región metropolitana de Santiago de Chile, requiere construir un programa con un menú que contenga las siguientes opciones:
#### - Opción 1: Grabar.
Corresponde a guardar ciertos datos de un vehículo, entre ellos: Tipo, patente, marca y precio, multas (monto yfecha), fecha de registro del vehículo y nombre del dueño.Además, debe verificar que la patente sea correcta, la marca considere entre 2 y 15 caracteres y el precio sea mayor a$5.000.000.
#### - Opción 2: Buscar.
Corresponde buscar un auto por su patente y mostrar toda su información almacenada.
#### - Opción 3: Imprimir certificados.
Esta opción permite imprimir los certificados de Emisión de contaminantes, de anotaciones vigentesy de multas. Estos deben ser previamente ingresados con valores aleatorios entre $1.500 y $3.500. Al imprimir el certificado,debe mostrar el nombre del certificado, la patente del auto y los datos del dueño actual.
#### - Opción 4: Salir.
Salir del programa emitiendo un mensaje de salida. Considere, además, su nombre y apellido y laversión del programa.

## Instrucciones Generales.

Escribir un programa que contenga:
- Diseñe un menú con las opciones para acceder a cada función requerida.
- Cree las funciones solicitadas por cada requerimiento
- Considere el ingreso de datos y el despliegue de información.


# Desarrollo del programa.

Comenzamos con la creación de 2 archivos en extension `.py`

```
Evaluacion3.py
FuncionesEvaluacion3.py
```
En el archivo `Evaluacion3.py` creamos la función principal, en la cual se crea el menú y se llama a las funciones correspondientes, antecedemos a esto con un mensaje de bienvenida y la opción de ingresar el nombre de la persona que esta haciendo uso del programa.

```python
import time
import FuncionesEvaluacion3 as fn

print("Bienvenido a automotora Auto Seguro.")
usuario = input("Ingrese su nombre: ")

def main():
    registro = {}
    
    while True:
        print("\nPor favor elija una opcion: ")
        print("1. Grabar vehículo")
        print("2. Buscar vehículo")
        print("3. Imprimir certificados")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            fn.grabar_vehiculo(registro)
        elif opcion == "2":
            fn.buscar_vehiculo(registro)
        elif opcion == "3":
            fn.imprimir_certificados(registro)
        elif opcion == "4":
            print(f"Hasta luego {usuario}. Gracias por usar Auto Seguro.\nversion 1.0")
            print("Cerrando...")
            time.sleep(5)
            break
        else:
            print("Opcion invalida. Intente nuevamente.")
```
En el inicio del archivo importamos la libreria `time` para usar un `time.sleep` que le dará al programa una espera de 5 segundos antes de cerrar completamente.

Para finalizar el archivo principal `Evaluacion3.py`, le daremos la opcion de ser importado en un futuro hacia otro archivo, sin tener que ejecutarse sobre el mismo e importando solo las funciones de `FuncionesEvaluacion3.py`.

```python
if __name__ == "__main__":
    main()
```
## Desarrollo de las funciones.

En el archivo `FuncionesEvaluacion3.py` creamos las funciones correspondientes a cada una de las opciones del menú.

## Funciones

### 1. Grabar vehículo

```python
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
```

Esta función permite ingresar los datos de un vehículo y almacenarlos en el registro. Los datos solicitados incluyen:

- Tipo de vehículo
- Patente
- Marca
- Precio
- Fecha de registro
- Nombre del dueño

El programa realiza validaciones en los datos ingresados, como la longitud de la patente, la cantidad de caracteres de la marca y el precio mínimo.

Además, se ha agregado la opción de ingresar multas. Si el vehículo tiene multas, se puede indicar la cantidad de multas y luego ingresar la fecha y el monto de cada una.

### 2. Buscar vehículo

```python
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
```

Con esta función, es posible buscar un vehículo en el registro utilizando su patente. Si el vehículo se encuentra en el registro, se mostrará toda su información almacenada, incluyendo los detalles de las multas en caso de tener.

### 3. Imprimir certificados

```python
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
```

La opción de imprimir permite generar certificados para los vehículos registrados. Los certificados disponibles son:

- Certificado de Emisión de contaminantes
- Certificado de anotaciones vigentes
- Certificado de multas

Al seleccionar esta opción, se pedirá la patente del vehículo para el cual se generarán los certificados. Se mostrará un menú para elegir el certificado deseado y se imprimirá con la información correspondiente del vehículo y el valor del certificado generado aleatoriamente, para ello importamos la libreria `random`

```python
import random
```

### 4. Salir

Lo siguiente es parte del archivo `Evaluacion3.py`:
```python
print(f"Hasta luego {usuario}. Gracias por usar Auto Seguro.\nversion 1.0")
            print("Cerrando...")
            time.sleep(5)
            break
```

Esta opción permite salir del programa y finalizar la ejecución.

## Cómo utilizar el programa

1. Clona este repositorio o descarga el archivo ZIP y extraelo.
2. Asegúrate de tener Python instalado en tu sistema.
3. Abre una terminal y navega hasta la ubicación del archivo `Prueba3.py`.
4. Verifica que en la carpeta se encuentran ambos archivos: `Prueba3.py` y `FuncionesPrueba3.py`.
5. Ejecuta el programa directamente o con el comando `python Prueba3.py`.
6. Sigue las instrucciones del menú para utilizar las diferentes funciones.


---

Espero que este archivo `README.md` sea de ayuda. Puedes copiar y pegar su contenido en tu propio archivo `README.md` en tu repositorio de GitHub y modificarlo según tus necesidades. 
