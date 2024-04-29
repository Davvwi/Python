#Faça um Programa que peça as quatro notas de 10 alunos, 
#calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias = []
acumulo = 0
for i in range(10):
    for j in range(4):
        nota = float(input(f"Digite a {j +1}ª nota: "))
        acumulo = acumulo + nota
    media = acumulo/4
    medias.append(media)
    print(medias)
    acumulo = 0
contador = 0
for i in range(len(medias)):
    if(medias[i] >= 7):
        contador +=1
print(f"A quantidade de alunos com médias acima de 7.0 é {contador}.")