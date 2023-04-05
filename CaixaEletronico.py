print('-'*40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('-'*40)
x = int(input('Digite o valor que deseja sacar R$'))
cedula_cem = cedula_cinquenta = cedula_vinte = cedula_dez = cedula_um = 0
while True:
    while x - 100 >= 0:
        x -= 100
        cedula_cem += 1
    while x - 50 >= 0:
        x -= 50
        cedula_cinquenta += 1
    while x - 20 >= 0:
        x -= 20
        cedula_vinte += 1
    while x - 10 >= 0:
        x -= 10
        cedula_dez += 1
    while x - 1 >= 0:
        x -= 1
        cedula_um += 1
    break
if cedula_cem != 0:
    print(f'Total de {cedula_cem} cedulas de R$100')
if cedula_cinquenta != 0:
    print(f'Total de {cedula_cinquenta} cedulas de R$50')
if cedula_vinte != 0:
    print(f'Total de {cedula_vinte} cedulas de R$20')
if cedula_dez != 0:
    print(f'Total de {cedula_dez} cedulas de R$10')
if cedula_um != 0:
    print(f'Total de {cedula_um} cedulas de R$1')
print('-' * 40)
print('Obrigado pela preferência !')