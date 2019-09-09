print('digite valores a somar seguido de .')
print('para encerrar digite zero: 0')
total = 0
while 1:
    n = float(input(':'))
    if n == 0 : break
    total = total + n
print('Total: {}'.format(total))