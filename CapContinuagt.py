import math
from math import e

print('=-'* 15, 'CAPITALIZAÇÃO CONTÍNUA', '=-'*15)
print(' F = P · e^δn')
print('Opções:')
print('[1]CALCULAR VALOR FUTURO (F)\n[2]CALCULAR VALOR PRESENTE (P)\n[3]CALCULAR A TAXA (δ)\n[4]NÚMERO DE PERÍODOS (n)')
escolha = int(input('SELECIONE UMA OPÇÃO: '))
while True:
    if escolha != 1 and escolha !=2 and escolha != 3 and escolha != 4:
        print('Comando inválido, tente novamente')
        escolha = int(input('SELECIONE UMA OPÇÃO '))
    else:
        break
if escolha == 1:
    print('Calcular o valor futuro -> F: ')
    p = float(input('valor presente -> P = '))
    taxa = float(input('Taxa -> δ (em decimais) = '))
    n = float(input('Períodos -> n = '))
    f = p * (e ** (taxa * n))
    print(f'O valor futuro -> F = {f}')
if escolha == 2:
    print('Calcular o valor presente -> P: ')
    f = float(input('Valor futuro -> F: '))
    taxa = float(input(f'Taxa -> δ (em decimais) = '))
    n = float(input(f'Períodos -> n = '))
    p = f / (e ** (taxa * n))
    print(f'O valor presente -> P = {p}')
if escolha == 3:
    print('Calcular a taxa -> δ ')
    p = float(input('valor presente -> P = '))
    f = float(input('Valor futuro -> F: '))
    n = float(input(f'Períodos -> n = '))
    taxa = ((math.log(f / p)) / n)
    print(f'taxa = {taxa} = {taxa * 100:.3f}%')
if escolha == 4:
    print(f'Número de períodos -> n: ')
    p = float(input(f'p = '))
    f = 2 * p
    taxa = float(input(f'delta = '))
    n = ((math.log(f / p)) / taxa)
    print(f'Períodos -> n = {n}')


