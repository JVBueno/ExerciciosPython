cont = 0
n = int(input('Digite um número'))
for c in range (1, n+1):
    if n % c == 0:
        cont = cont + 1
print('O número {} foi divisivel {} vezes'.format(n, cont))

if cont == 2:
    print('NÚMERO É PRIMO')
else:
    print('NÃO É PRIMO')
