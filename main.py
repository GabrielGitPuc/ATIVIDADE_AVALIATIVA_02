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
            funcoes.limpar_menu()
            id_entregador = funcoes.ID_entregador()
            print(id_entregador)

            entregador[id_entregador] = {
            'nome_entregador': input("Digite o nome do Entregador: "),
            'veiculo': input("Digite o tipo de veiculo: "),
            'id_pedidos': input("Digite o id do pedido: "),
            'disponibilidade': input("Digite a disponibilidade do entregador: ")
            }
            print(f"✅ Entregador ID:{id_entregador} cadastrado com sucesso!")
            
        case 2:
            funcoes.limpar_menu()
            id_pedidos = funcoes.ID_pedido()
            print(f"ID:{id_pedidos}")

            pedidos[id_pedidos] = {
            'nome': input("Digite o nome do Cliente: "),
            'endereco':  input("Digite o Endereço: "),
            'prioridade':  input("Digite a Prioridade (Alta/Normal): "),
            'desc_Pedido':  input("Digite a descrição do pedido: "),
            'status':  input("Digite o Status:  "),
            'id_Entregador':  input("Digite o id do entregador: ")
            }
            print(f"✅ Pedido ID:{id_pedidos} cadastrado com sucesso!")

        case 3:
            funcoes.limpar_menu()
            att = 1
            while att == 1:
                print('''      
[1] Alterar o status do pedido
[2] Cancelar Pedido 
[3] Associar Entregadores a Pedidos
[4] Remover associação de Entregador 
[5] Voltar ''')
                atualizar = int(input(": "))
                match atualizar:
                    case 1:
                        funcoes.limpar_menu()
                        id_pedidos = input("Digite o id do pedido que deseja alterar: ")
                        if id_pedidos in pedidos:
                            pedidos [id_pedidos] ['status'] = input("Digite o novo status: ")
                        else: 
                          print("Pedido não Encontrado") 
                    
                    case 2:
                        id_pedidos = input("Digite o id do pedido que deseja alterar: ")
                        if id_pedidos in pedidos:
                            pedidos [id_pedidos] ['status'] 
                        else: 
                          print("Pedido não Encontrado") 
                    case 3:
                        pass

                    case 4:
                        pass

                    case 5:
                        att = 0
                
            
            
    

        case 6:
            opcao = 1
            opc = 0

        
print(pedidos)
