"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721."""
def reverse(num):
    num_rev = str(num)[::-1]
    reverso = int(num_rev)
    return num_rev

numero = int(input("Digite um número: "))
print(f"O reverso desse número é: {reverse(numero)}")