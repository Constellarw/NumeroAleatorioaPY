import random

numero_aleatorio = random.randint(1,100)
numero = 0

tentativas = 10

while   tentativas > 0 and numero != numero_aleatorio:
    numero = int(input('Tente Advinhar o numero: '))
    if numero > numero_aleatorio:
        print('Numero escolhido e maior que o aleatorio')
        tentativas -= 1
        print('Voce ainda tem: ',tentativas,'Tentativas') 
        
    elif numero < numero_aleatorio:
        print('Numero escolhido e menor que o aleatorio')
        tentativas -= 1
        print('Voce ainda tem: ',tentativas,'Tentativas')
        
    elif numero == numero_aleatorio:
        print('Parabens voce adivinhou o numero aleatorio', numero_aleatorio)
    if tentativas == 0:
        print('Voce perdeu :(')

