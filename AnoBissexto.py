from datetime import date
ano = int(input('Digite um ano qualquer, ele é bissexto ?. Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É Bissexto'.format(ano))
else:
    print('O ano {} Não é Bissexto'.format(ano))

x = date.today().day
print(x)