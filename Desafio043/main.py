# Bibliotecas usadas
import time
import random
from datetime import datetime
import math

# Estética
print('{:=^40}'.format('Desafio 43'))
print('{:80}'.format(40 * '='))

# Interação inicial
input('')  # Pausa inicial
nome = input('Olaaaa!!!!! Eu me chamo ASCE, como é seu nome? ').strip().upper()

# Correção no nome
if nome in ['LUIS', 'LUÍS']:
    print('É bom te ver de novo carinha')
elif nome in ['KAROL', 'ANE']:
    print('Fala guria!')
else:
    print('É um prazer te conhecer!!!!')

# Listas de frases
frases_feliz = [
    'Se você está bem, eu estou bem!',
    'Que sua felicidade contagie a todos como me contagiou ;D',
    'Eu estou feliz por você estar feliz.',
    'Que bom que você está bem!'
]

frases_triste = [
    "Não desista, você é capaz de tudo!",
    "Cada desafio é uma oportunidade para crescer.",
    "Acredite em você, pois você tem muito potencial!",
    "Continue lutando, o sucesso está perto!"
]

# Pergunta sobre estado emocional
emocao = input('Você está bem? [Sim/Não] ').strip().upper()

while emocao not in ['SIM', 'NÃO']:
    emocao = input('Eu sou meio binário, vai ter que escolher entre SIM e NÃO :D ').strip().upper()

if emocao == 'SIM':
    print(random.choice(frases_feliz))
else:
    print(random.choice(frases_triste))

time.sleep(2)
# Loop principal do programa
while True:
    # Pergunta se quer ver a classificação dos triângulos
    duvida = input('\nAprendi uma nova utilidade. Agora consigo calcular o seu IMC. Quer ver? [Sim/Não] ').strip().upper()

    # Validação da resposta
    while duvida not in ['SIM', 'NÃO', 'QUERO']:
        duvida = input('Eu sou meio binário, vai ter que escolher entre SIM e NÃO :D ').strip().upper()

    if duvida in ['NÃO']:
        print('Ok, outro dia então...')
        break
    kg = float(input('Qual é o seu peso? '))
    m = float(input('Qual é a sua altura? '))
    imc = kg / (m**2)
    if imc <= 18.5:
        print('Você está abaixo do peso ideal')
    elif 18.5 < imc <= 24.9:
        print('Você está com o peso ideal')
    elif 25.0 <= imc <= 29.9:
        print('Você está com sobre peso')
    elif 30.0 <= imc <= 34.9:
        print('Você está com obesidade de 1º grau')
    elif 35.0 <= imc <= 39.9:
        print('Você está com obesidade de 2º grau')
    else:
        print('Você está com obesidade de 3º grau')

    # Pergunta se deseja repetir
    replay = input('\nGostaria de tentar de novo? [Sim/Não]: ').strip().upper()

    while replay not in ['SIM', 'NÃO']:
        replay = input('Por favor, escolha entre Sim ou Não: ').strip().upper()

    if replay == 'NÃO':
        print('\nEspero ter sido útil a você! Até a próxima :D')
        print('{:=^80}'.format(''))
        break

    print('\nReiniciando o código...\n')
    time.sleep(2)