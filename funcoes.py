import random
import string
import os

def ID_pedido():
    letra_aleatoria = ''.join(random.sample(string.ascii_uppercase, k=1))
    numeros_aleatorios = ''.join(map(str, random.sample(range(1,9), k=4)))
    return f'{letra_aleatoria}{numeros_aleatorios}'





def ID_entregador():
    numeros_aleatorios = ''.join(map(str, random.sample(range(1, 9), k=4)))
    return f'ID:{numeros_aleatorios}'

def limite_veiculo(veiculo):
    if veiculo.lower() == 'caminhão':
        tamanho = input("Digite o tamanho do caminhão (2 Eixos/3 Eixos/Cavalo Trucado/BiTrem): ").lower()
        if tamanho == '2 Eixos':
            return 5
        elif tamanho == '3 Eixos':
            return 10
        elif tamanho == 'Cavalo Trucado':
            return 20
        elif tamanho == 'BiTrem':
            return 35
    else:  # Van
        return 3

def limpar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')


def ler_opcao(opcoes_validas):

    while True:

        try:

            opc = int(input("Digite uma das opções: "))

            if opc in opcoes_validas:

                return opc 

            else:

                print("Opção inválida.")

        except ValueError:

            print("Digite apenas números.")
