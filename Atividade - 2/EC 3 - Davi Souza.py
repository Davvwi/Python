#Escreva um programa que, dadas duas datas, determine qual delas ocorreu cronologicamente primeiro. 
#Para cada uma das duas datas, leia três números referentes ao dia, mês e ano, respectivamente.
#Data 1:
d1 = int(input("Digite um número para (d1):"))
m1 = int(input("Digite um número para (m1):"))
a1 = int(input("Digite um número para (a1):"))
#Data 2:
d2 = int(input("Digite um número para (d2):"))
m2 = int(input("Digite um número para (m2):"))
a2 = int(input("Digite um número para (a2):"))

if (a1 > a2) and (m1 > m2) and (d1 > d2): 
    print("A data 1 ocorreu primeiro!")
elif (a1 == a2) and (m1 == m2) and (d1 == d2):
    print("As datas são iguais!")
else:
    print("A data 2 ocorreu primeiro!")


