from math import hypot
ca = float(input('Entre com o valor do cateto adjacente:'))
co = float(input('Entre com o valor do cateto oposto:'))
hip = hypot(ca, co)
print('A hipotenusa é {:.3f}'.format(hip))
