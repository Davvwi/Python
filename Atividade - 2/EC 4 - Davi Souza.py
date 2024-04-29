a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if (a != 0):
    if (b == 0):
        print("Não existe raiz.")
    else:
        x = (-c / b)
        print("A raiz é:", x)
else:    
    delta = (b**2) - (4 * a * c)
    if delta < 0: 
        print("Não exitem raízes reais.")
    else: 
        x1 = (-b + delta ** (1/2)) / (2*a)
        x2 = (-b + delta ** (1/2)) / (2*a)
        print("A primeira raiz é:", x1)
        print("A segunda raiz é:", x2)

