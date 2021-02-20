from Aula07_televisao import Televisao
from Aula07_calculadora1 import Calculadora
from aula08_contador_letras import contador_letras

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora()
print(calculadora.soma(5, 10))
lista = ['Elefante', 'Cachorro', 'gato']
total_letras = contador_letras(lista)
print('Total de letras por palavras: {}'.format(total_letras))


