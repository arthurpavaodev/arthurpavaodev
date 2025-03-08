tabela_precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
codigo, quantidade = map(int, input().split())
total = tabela_precos.get(codigo, 0) * quantidade
print(f"Total: R$ {total:.2f}")
