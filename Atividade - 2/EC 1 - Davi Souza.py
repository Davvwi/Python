#1 - Escreva um programa que, dados três números inteiros, imprima o menor deles.
a = int(input("Digite um número para (a):"))
b = int(input("Digite um número para (b):"))
c = int(input("Digite um número para (c):"))

if(a == b == c):
    print("Os números digitados são iguais!")
elif (a < b) and (a < c):
    print("O número A é o menor: ", a)

elif (b < a) and (b < c):
    print("O número B é o menor: ", b)

elif (c < a) and (c < b):
    print("O número C é o menor: ", c)
    