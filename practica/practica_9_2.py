'''
Created on 11 jun 2022
ADIVINA EL NUMERO
@author: txema
'''

secreto = 50
valor = 0
while valor != secreto:
    valor = int(input('introduce un múmero: '))

    if valor > secreto:
        print('Muy alto')
        continue
    
    if valor < secreto:
        print('Muy bajo')
        continue
    
print('acertaste')