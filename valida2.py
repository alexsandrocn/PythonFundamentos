valida_numero = {
    'par': lambda a: 'par' if a % 2 == 0 else False,
    'impar': lambda b: 'impar' b % 2 != 0 else False

}
resultado = valida_numero['par'](10)
print(resultado)
