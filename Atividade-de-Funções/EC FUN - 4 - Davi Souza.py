'''Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere P, se seu argumento for positivo, 
e N, se seu argumento for zero ou negativo.'''
def posi_neg(n):
    if n > 0:
        return "P"
    else:
        return "N"
x = int(input("Digite um número: "))
print(" O número é: ", posi_neg(x))