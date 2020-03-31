lista = []
for i in range(10):
    lista.append(i)
print(lista)
for i in range(len(lista)):
    temp = lista
    if (i%4 == 0):
        temp.remove(i)
        print (temp)

lista = temp

print(lista)