import funcoes
opcao = 0
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
            print(funcoes.ID_pedido())
            nome = input("Digite o nome do Cliente: ")
            Endereco = input("Digite o Endereço: ")
            Prioridade = input("Digite a Prioridade: ")
            Desc_Pedido = input("Digite a descrição do pedido: ")
            Status = input("Digite o Status:  ")
            Id_Entregador = input("Digite o id do entregador: ")

        case 2:
            print(funcoes.ID_entregador())
            nome_entregador = input("Digite o nome do Entregador: ")
            veiculo = input("Digite o tipo de veiculo: ")
            id_pedidos = input("Digite o id do pedido: ")
            disponibilidade = input("Digite a disponibilidade do entregador: ")