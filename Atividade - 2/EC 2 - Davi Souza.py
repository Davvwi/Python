#2 - Escreva um programa que, dados três números inteiros, imprima os números em ordem crescente.
a = int(input("Digite um número para (a):"))
b = int(input("Digite um número para (b):"))
c = int(input("Digite um número para (c):"))

if (a <= b) and (b <= c):
    print(a, b, c)
elif (a <= c) and (c <= b):
    print(a, c, b)
elif (b <= a) and (a <= c):
    print(b, a, c)
elif (b <= c) and (c <= a):
    print(b, c, a)
elif (c <= a) and (a <= b):
    print(c, a, b)
else:
    print(c, b, a)