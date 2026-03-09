print('Este programa captura importes')
info = """
     CALCUKLA TU SUMA
     Este programa lleva el conteo de cuantos importes ha introducido un usuario
     va acumulando todos los importes que el usuario ingresa.    
     Si el usuario desea terminar el programa puede escribir cualquier momento la pa labra
     'EXIT', 'QUIT', 'TERMINAR'
                                                       Elaborado por por ALEXIS
"""
print(info)
conteo = 0
suma = 0.0
minimo = None
maximo = None

while True:
     user_message = """
     INGRESA TU IMPORTE (MXN) O ESCRIBE 'EXIT', 'QUIT' O 'TERMINAR' PARA FINALIZAR
"""
     line = input('Ingresa tu importe (MXN): ').lower()
     if line == "exit" or line == 'quit' or line == 'terminar':
          break
     try:
          value = float(line)
     except ValueError:
          print("Valor ingresado no es valido, intenta de nuevo (ej.125.5)")
          continue

     conteo +=1
     suma += value
     if minimo is None or value < minimo:
          minimo = value
     if maximo is None or value > maximo:
          maximo = value
if conteo == 0:
     print("No se capturaron importes")
else:
     print('='*32)     
     print (f'(La cantidad de numeros ingresados es: ', {conteo}')
