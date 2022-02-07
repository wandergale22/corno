# c1
def var(var):
    print('Print valor')
    return var

variavel = var('Um valor')
if variavel:
    print(variavel)
else:
    print('Nenhum valor')
# c2
def divisao(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print('Nao é possivel divisao por 0(zero).')

div = divisao(8, 0)
if div:
    print(div)