def piramide(x):
    x = x + 1
    i = 1
    j = 0
    for i in range(1, n + 1):
        for j in range(1, i+1):
            print(j, end = " ")
        print()

n = int(input("Digite um número: "))
piramide(n)