import funcoes
opcao = 0

pedidos = {}
entregador = {}
while opcao == 0:
    print("="*30)
    print("FluxoNorte")
    print("="*30)
    print('''   
          
        [1] Cadastro pedido
        [2] Cadastro entregador
        [3] Atualizar Pedidos 
        [4] Informações 
        [5] Relatórios
        [6] Finalizar Sistema ''')
    
    opc = int(input(":"))
    match opc:
        case 1:
            id_pedidos = funcoes.ID_pedido()
            print(id_pedidos)

            pedidos[id_pedidos]{
            'nome': input("Digite o nome do Cliente: "),
            'endereco':  input("Digite o Endereço: "),
            'prioridade':  input("Digite a Prioridade (Alta/Normal): "),
            'desc_Pedido':  input("Digite a descrição do pedido: "),
            'status':  input("Digite o Status:  "),
            'id_Entregador':  input("Digite o id do entregador: ")
            }

        case 2:
            id_
            print(funcoes.ID_entregador())
            nome_entregador = input("Digite o nome do Entregador: ")
            veiculo = input("Digite o tipo de veiculo: ")
            id_pedidos = input("Digite o id do pedido: ")
            disponibilidade = input("Digite a disponibilidade do entregador: ")
