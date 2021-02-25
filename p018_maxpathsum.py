import numpy as np


# prepare data
text_file = open("p067_triangle.txt", "r")
lines = text_file.readlines()
data = []
for line in lines:
     oneL = line[:-1]
     oneL = oneL.split(' ')
     data.append([int(el) for el in oneL])

def printout(L):
    l = len(L)
    for i in range(l):
        print(' '*int((l-i)*1.6) , L[i])

printout(data)


def Algo(L):
    if len(L)==1:
        return L
    else:
        for k in range(len(L[-2])):
            L[-2][k] = L[-2][k] + max(L[-1][k], L[-1][k+1])
        L = L[:-1]
        print(L)
        return Algo(L)
    
print(Algo(data))