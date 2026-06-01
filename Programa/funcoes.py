import random
import string
import os


def RO():
    numeros_aleatorios = ''.join(map(str, random.sample(range(1, 9), k=4)))
    return f'{numeros_aleatorios}'


def ID_pedido():
    letra_aleatoria = ''.join(random.sample(string.ascii_uppercase, k=1))
    numeros_aleatorios = ''.join(map(str, random.sample(range(1, 9), k=4)))
    return f'{letra_aleatoria}{numeros_aleatorios}'


def ID_entregador():
    numeros_aleatorios = ''.join(map(str, random.sample(range(1, 9), k=4)))
    return f'{numeros_aleatorios}'


def limite_veiculo(veiculo):
    v = veiculo.lower()
    if v == 'van':
        return 10
    elif v == 'carro':
        return 5
    elif v == 'moto':
        return 3
    else:
        return 0


def limpar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')


def ler_opcao(opcoes_validas):
    opcao_valida = 0
    while opcao_valida == 0:
        try:
            opc = int(input("Digite uma das opções: "))
            if opc in opcoes_validas:
                opcao_valida = 1
                return opc
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números.")


def selecionar_status():
    status_opcoes = {
        '1': 'Pendente',
        '2': 'Em Rota',
        '3': 'Entregue',
        '4': 'Cancelado'
    }
    print("Status disponíveis:")
    for chave, valor in status_opcoes.items():
        print(f"  [{chave}] {valor}")

    escolha_valida = 0
    while escolha_valida == 0:
        escolha = input("Escolha o status: ")
        if escolha in status_opcoes:
            escolha_valida = 1
            return status_opcoes[escolha]
        else:
            print("Opção inválida, tente novamente.")


def contar_pedidos_entregador(pedidos, id_entregador):
    total = 0
    for dados in pedidos.values():
        if dados.get('id_entregador') == id_entregador and dados.get('status', '').lower() != 'cancelado':
            total += 1
    return total


def contar_pedidos_entregador(pedidos, id_entregador):
    total = 0
    for dados in pedidos.values():
        entregador_correto = dados.get('id_entregador') == id_entregador
        nao_cancelado = dados.get('status', '').lower() != 'cancelado'
        if entregador_correto and nao_cancelado:
            total += 1
    return total


def ordenar_pedidos_por_prioridade(pedidos):
    lista = []
    for id_p, dados in pedidos.items():
        lista.append((id_p, dados))

    alta = []
    normal = []
    for item in lista:
        if item[1]['prioridade'].lower() == 'alta':
            alta.append(item)
        else:
            normal.append(item)

    return alta + normal
