from cgi import print_arguments
from camelcase import CamelCase

instancia = CamelCase()
texto = "Hola mundo"
print(instancia.hump(texto))

def sumar(n1,n2=10):
  suma = n1 + n2
  if n2%2==0:
    print(suma/2)
  else :
    print(suma)

sumar(10)

def funcion(*args):
  print(args)

funcion("Hola","hola1")

def funcion2(**kwargs):
  print(kwargs)

funcion2(hola="1", hola2="3")

try:
  numero = int(input("Ingrese nombre: "))
  print(numero)
except ValueError:
  print()



def funcion3():
  valores = []
  for _ in range(7):
    try:
      valor = int(input("Ingrese un numero: "))
    except Exception:
      print("Numero mal ingresado")
    else:
      valores.append(valor)
  print(valores)  

funcion3()






