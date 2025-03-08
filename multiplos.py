A = int(input("Adicione um número:"))
B = int(input("Adicione outro número:"))

if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")