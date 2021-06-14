def purchase_value():
    total = 0.0
    for i in range(2):
        prod = input().split()
        total += (int(prod[1]) * float(prod[2]))
    return total


print(f'VALOR A PAGAR: R$ {purchase_value():.2f}')
