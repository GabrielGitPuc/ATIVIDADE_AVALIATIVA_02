import random
import string
import os

def ID_pedido():
    letra_aleatoria = ''.join(random.sample(string.ascii_uppercase, k=1))
    numeros_aleatorios = ''.join(map(str, random.sample(range(1,9), k=4)))
    return f'{letra_aleatoria}{numeros_aleatorios}'





def ID_entregador():
    numeros_aleatorios = ''.join(map(str, random.sample(range(1, 9), k=4)))
    return f'{numeros_aleatorios}'





def limpar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
