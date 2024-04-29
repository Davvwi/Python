opcoes = ("pedra", "papel", "tesoura")

jogador1 = input("Escolha pedra, papel ou tesoura: ")
print("#"*100)
print("#"*100)
print("#"*100)
print("#"*100)
print("#"*100)
print("#"*100)
print("#"*100)
print("#"*100)
print("#"*100)
print("#"*100)
print("#"*100)
jogador2 = input("Escolha pedra, papel ou tesoura: ")

print("O jogador 1 escolheu: ", jogador1)
print("O jogador 2 escolheu: ", jogador2)

if jogador1 == jogador2:
    print("Vocês jogaram sinais iguais!")
    print("O resultado é, EMPATE!")
elif(jogador1 == "pedra" and  jogador2 == "tesoura") | \
    (jogador1 == "papel" and jogador2 == "pedra") | \
    (jogador1 == "tesoura" and jogador2 == "papel"): 
    print("Jogador 1 ganhou!")
else:
    print("jogador 2 ganhou!")  