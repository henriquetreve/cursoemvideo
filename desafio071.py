# Caixa eletronico mostrando quais notas serão sacadas

print('=' * 40)
print(f'{"BANCO TREVE":^40}')
print('=' * 40)

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre!')
