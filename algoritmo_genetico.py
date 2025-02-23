from time import sleep
import numpy as np


x = np.array([float(i) for i in input('Digite as 4 estatísticas de desempenho (ex: posse de bola, chutes a gol, passes certos, e defesas) separadas por espaços: ').split()])
w = np.array([float(i) for i in input('Digite os 4 pesos das estatísticas respectivamente (ex: importância de posse de bola, chutes, passes, e defesas) separadas por espaço: ').split()])
b = float(input('Digite o viés (ex: fatores externos como torcida ou clima): '))

print('Calculando a probabilidade de vitória do time...')
print('Um momento, estamos realizando o cálculo...')
sleep(2)


z = np.dot(x, w) + b


if z >= 0:
    y = 1  
else:
    y = 0  
    
print(f"Resultado do cálculo: {z:.2f}")
print("Chance de vitória do time:", y)
