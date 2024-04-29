caracter = []
for i in range(3):
    c = str(input(f"Digite {i+1} caractere: ").lower())
    caracter.append(c)

consoantes = 0
conso_achadas = []
for i in caracter:
    if i.isalpha() and i not in ["a", "e","i", "o", "u"]:
        consoantes += 1
        conso_achadas.append(i)
print(consoantes)
print(conso_achadas)