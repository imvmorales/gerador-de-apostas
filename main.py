# gerador de apostas de loteria
# 6 números de 1 a 60 (sem repetições)
import time

# função que gera uma lista ordenada com 6 números aleatórios entre 1 e 60
def aposta():
    import random
    l = []
    while len(l) < 6:
        n = random.randint(1, 60)
        if n not in l:
            l.append(n)
    return sorted(l)


# impressão do título do 'programa'
print('~' * 30)
titulo = 'GERADOR DE APOSTAS'
print(titulo.center(30))
print('~' * 30)

# interação com o usuário para saber quantas apostas ele quer
x = int(input('Quantas apostas deseja gerar? '))
print('-' * 30)

# impressão das apostas de forma ordenada, sem estarem dentro de listas
for k in range(1, x+1):
    print(f'{k}ª APOSTA: ', end='')
    for i in aposta():
        print(i, end=' ')
    print()
    if k != x:
        time.sleep(2)

print('-' * 30)
