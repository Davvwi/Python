#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def verificacao(x):
    count = 0
    for i in range(len(x)):
        count += 1
    return count
a = input("Digite um número inteiro: ")
print(f"Seu numero tem {verificacao(a)} digitos")