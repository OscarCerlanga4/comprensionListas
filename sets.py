#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe



# nums = { 1, 2, 2, 2, 3, 4 }
# print(type(nums))
# print(nums)
# listaNums = list(nums)
# print(type(listaNums))
# print(listaNums)
# listaNums.append(2)
# print(listaNums)

# print("cosas")
# cosas = { 11, 22, 23, "22", 3.14, 4 }
# print(type(cosas))
# print(cosas)
# print("intento meter un valor repetido: 22")
# cosas.add(22) # NO EXCEPTION. IGNORED
# print(cosas)


# print()

# listaCosas = list(cosas)
# print(type(listaCosas))
# print()

# print(listaCosas)
# listaCosas.append('22')
# print(listaCosas)

# # LISTA -> SET
# l = [x for x in "patata"]
# print(l)
# print(list(set(l)))

# comandos = { "new", "delete", "run", 'delete'}
# print(comandos)


# nums = { 21, 11, 42, 29, 22, 71, 18 }
# print(nums)
# lista = list(nums)
# print(lista)
# lista.sort()
# print(lista)
# nums = set(lista)
# print(nums)

setA = {11,22,33,44}
setB =       {33,44,55,66}

#union
print(setA.union(setB))
print(setB.union(setA))
print(setA | setB)
print(setB | setA)
print()

#interseccion
print(setA.intersection(setB))
print(setB.intersection(setA))
print(setA & setB)
print(setB & setA)
print()

#diferencia A-B 11, 22
print(setA.difference(setB))
print(setA - setB)

#diferencia B-A 55, 66
print(setB.difference(setA))
print(setB - setA)

#diferencia simetrica A^B == B^A
# A^B 
print(setA.symmetric_difference(setB))
print(setA ^ setB)

# B^A
print(setB.symmetric_difference(setA))
print(setB ^ setA)

colores = {"R", "B", "G"}
print(colores, type(colores))
colores.add("Y")
print(colores)

colores = frozenset(colores)
print(colores, type(colores))

colores = set(colores)
print(colores, type(colores))