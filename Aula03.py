# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# if a > b and a > c:
#     print('o maior numero é {}' .format(a))
# elif b > a and b > c:
#     print('o maior numero é {}' .format(b))
# else:
#     print('o maior numero é {}' .format(c))
# print('final do programa')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um numero par')
# else:
#     print('Nenhum numero par foi digitado')

# a = int(input('Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <=10:
#     print('media: {}' .format(media))
# else:
# #     print('foi encotrada uma nota errada')
# a = int(input('Entre com o numero: '))
# for num in range(a):
#
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#        nova_lista = []
#        nova_lista.append(num)
#        print(nova_lista)

# a = int(input('Entre com o numero: '))
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('O numero {} é primo' .format(a))
# else:
#     print('O número {} não é primo'. format(a))
a = 0
while a < 9:
    a += 1
    print(a)
