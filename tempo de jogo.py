horario_inicio = int(input("Digite o horario que começou o jogo: "))
horario_fim = int(input("Digite o horario que fechou o jogo: "))

if horario_inicio < horario_fim:
    duracao = horario_fim - horario_inicio
else:
    duracao = (24 - horario_inicio) + horario_fim

print(f"O JOGO DUROU {duracao} HORA(S)")