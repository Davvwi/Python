#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
#Imprima os três vetores.
pares = []
impares = []

for i in range(10):
    num = int(input("Digite um número: "))

    if (num % 2 == 0):
        pares.append(num)
    else:
        impares.append(num)
print(pares)
print(impares)