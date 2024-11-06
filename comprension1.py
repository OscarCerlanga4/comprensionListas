#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe



r0 = range(16+1)
print(r0, type(r0))

l0 = []
for item in r0:
    l0.append(item)
   
print(l0, type(l0)) 


l0 = [x for x in range(17)]
print(l0, type(l0))

l1 = [x*x for x in range(17)]
print(l1, type(l1))  
    
ListaEntrada = [x for x in range (17)]
ListaPares = [x for x in ListaEntrada if x%2==0]
print(ListaPares)

ListaIpares = [x for x in ListaEntrada if x%2!=0]
print(ListaIpares)

a = [1, 2, 3, 4, 5, 6]
print(a)

cuadrados = [e * 2 for e in a]
print(cuadrados)



# C temp
rangoClimasC = range(19, 30) 
ClimasC = [c for c in range(19, 30)]
print(ClimasC)

# F temp
ClimasF = [c * 9/5 + 32 for c in rangoClimasC]
print(ClimasF)

# filtrar aritméticamente valores positivos
a = [-4, 2, 0, -1, 12, -3]
b = [e for e in a if e > 0]
print(b)


# filtrar por tipos de dato
from math import pi
input = ['a', 2, 'patata', 12, 3, 'd', "3.14", 3.14, pi]
notStrT = [x for x in input if type(x) != str]
StrT    = [x for x in input if type(x) == str]

print(notStrT)
print(StrT)


def is_vowel(c):
    vowels = 'aeiou'
    if c in vowels: return True
    return False

sentence = 'En un lugar de la Mancha de cuyo nombre no quiero... '
vowels = [c for c in sentence if not is_vowel(c)]
print(vowels)

#l0 = [11,22,33,22]
#print (l0, type(l0))
#s = set(l0)
#print(s, type(s))