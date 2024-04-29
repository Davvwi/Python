"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor
entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é
 seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto,
 se tirar um 7 antes de tirar este Ponto novamente."""
import random


def jogo():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    soma = d1 + d2
    print(f"A soma dos dados sorteados é: {soma}")
    if soma == 7 or soma == 11:
        print("Você é (natural) e ganhou!")

    elif soma == 2 or soma == 3 or soma == 12:
        print("CRAPS, e você perdeu")

    else:
        ponto = soma
        print(f"Sua pontuação é: {ponto}")
        while True:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            soma = d1 + d2
            print(f"A soma dos dados sorteados é: {soma}")
            if soma == ponto:
                print("Você fez o ponto! Você ganhou!")
                break
            elif soma == 7:
                print("Você tirou um 7! Você perdeu!")
                break
jogo()