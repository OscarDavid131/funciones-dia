import math
#Ejemplo para calcular el area del triangulo

# Variables de entrada
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

# Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

# Invocar la funcion
resultado = calcularAreaTriangulo(base,altura)

# Salida
print(f"El area del triangulo cuya base {base} y altura {altura} es: {resultado}")

#///////////////////////////////////
# Funcion con argumento predeterminados
def my_function(contry = "Colombia"):
    print("I am from"+contry)

# Invocamos la funcion
my_function()
my_function("Sweden")

#///////////////////////////////////
# Argumentor arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante: "+args[2])

# Invocar la funcion
mostrarEstudiantes("Emil","Tobias","Linus","Bill","Andres")

#///////////////////////////////////
def mostarCarros(carro1, carro2, carro3):
    print("El carro es: " + carro2)

mostarCarros(carro1 = "BMW", carro3 = "Ferrari", carro2 = "Ford")
#///////////////////////////////////
def mostrarCliente(**kwargs):
    print("Su apellido es: " + kwargs["telefono"])

mostrarCliente(nombre = "Tobias", apellido = "Refsnes", telefono = "323232")

#Declaracion de paso
def miFuncion():
    pass

#///////////////////////////////////
#Funciones integradas

#Hayar el minimo y el maximo
x = min(5,10,25)
y = max(5,10,25)
print(x)
print(y)
#Hayar la potencia
num1 = pow(7,4)
print(num1)
#Hayar la raiz cuadrada se debe importar el modulo math
num2 = math.sqrt(34)
print(num2)
#Redondear hacia arriba o hacia abajo
num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3) # returns 8
print(num4) # returns 7
