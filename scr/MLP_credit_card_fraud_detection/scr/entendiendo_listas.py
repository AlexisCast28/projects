names = []
print(names)

#metodo apend para agregar elementos al final de la lista
names.append('Charly')
names.append('Mar')
names.append('Alexis')
names.append('Erick')
names.append('Jona')
names.append('Arce')

print(names)
print(type(names))
print(len(names))

#metodo insert para agregar elementos a la posiicion deseada
names.insert(1, 'hector')
print(names)

#metodo pop() sin indice para elimiinar el ultimo elemento de la lista
names.pop()
print(names)

#metodo pop() con indice para eliminar el elemento deseado de la lista
names.pop(2)
print(names)

#metodo remove(val) para eliminar un elemento por su valor
names.remove('hector')
print(names)