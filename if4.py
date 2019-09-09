# usandi IF
ana = 30
bia = 30

total = ana + bia
media = total / 2
print('total:', total)
print
print('media:', media)
diferenciana = media - ana
diferencibia = media - bia
if ana < media:
       print('Ana deve pagar: R$ ', diferenciana)
      
elif bia < media:
       print('Bia deve pagar: R$ ', diferencibia)
else:
       print('Elas gastaram mesma quantia')
