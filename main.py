import funcoes
opcao = 0

pedidos = {}
entregador = {}
while opcao == 0:
    print("="*30)
    print("FluxoNorte")
    print("="*30)
    print('''           
[1] Cadastro entregador
[2] Cadastro pedido
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
            'desc_pedido':  input("Digite a descrição do pedido: "),
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
                        funcoes.limpar_menu()
                        id_pedidos = input("Digite o id do pedido que deseja cancelar: ")
                        if id_pedidos in pedidos:
                            pedidos [id_pedidos] ['status'] = 'Cancelado' 
                        else: 
                          print("Pedido não Encontrado") 
                    case 3:
                        funcoes.limpar_menu()
                        id_pedidos = input("Digite o ID do entregador que deseja associar do pedido: ")
                        if id_pedidos in pedidos:
                            id_entregador = input("Digite o ID do entregador: ")
                            if id_entregador in entregador:
                                pedidos [id_pedidos] ['id_entregador'] = id_entregador
                                print(f'Entregador {id_entregador} associado ao pedido {id_pedidos}')
                            else:
                                print('Entregador não entregador')
                        else: 
                            print('Pedido não encontrado')
                    case 4:
                        funcoes.limpar_menu()
                        id_pedidos = input("Digite o ID do entregador que deseja desassociar do pedido: ")
                        if id_pedidos in pedidos:
                            id_entregador = input("Digite o ID do entregador: ")
                            if id_entregador in entregador:
                                pedidos [id_pedidos] ['id_entregador'] = None
                                print(f'Entregador {id_entregador} desassociado ao pedido {id_pedidos}')
                            else:
                                print('Entregador não entregador')
                        else: 
                            print('Pedido não encontrado')



                    case 5:
                        att = 0
        case 4:
            funcoes.limpar_menu()
            info = 1
            while info == 1:
                print('''      
[1] Pedidos Pendentes 
[2] Pedidos Entregues 
[3] Buscar Pedido por ID
[4] Entregador Disponível
[5] Todas as Entregas realizadas por um entregador
[6] Voltar
''')        
                informações = int(input("Digite uma opção: "))

                match informações:
                    case 1:
                        funcoes.limpar_menu()
                        print("="*30)
                        print("Pedidos Pendentes")
                        print("="*30)
                        for id_p, dados in pedidos.items():
                            if dados['status'].lower() == 'pendente':
                                print(f"ID: {id_p}")
                                print(f"  Cliente:    {dados['nome']}")
                                print(f"  Status:     {dados['status']}")
                                print(f"  Prioridade: {dados['prioridade']})")
                                print(f"  Descrição:  {dados['desc_pedido']}")
                                print(f"  Status:     {dados['pendente']})")
                                print("-"*30)

                    case 2:
                        funcoes.limpar_menu()
                        print("="*30)
                        print('Pedidos Entregues')
                        print("="*30)
                        for id_e, dados in id_pedidos.items():
                            if dados['status'].lower() == 'Entregue':
                                print(f'ID: {id_e}')
                                print(f"  Cliente:    {dados['nome']}")
                                print(f"  Status:     {dados['status']}")
                                print(f"  Prioridade: {dados['prioridade']}")
                                print(f"  Descrição:  {dados['desc_pedido']}")
                                print(f"  Status:     {dados['pendente']})")
                                print("-"*30)

                    case 3:
                        funcoes.limpar_menu()
                        print("="*30)
                        id_pedidos = input("Digite o ID do pedido que deseja busca")
                        for id_e, dados in id_pedidos.items():
                            if dados['status'].lower() == 'Entregue':
                                print(f'ID: {id_e}')
                                print(f"  Cliente:    {dados['nome']}")
                                print(f"  Status:     {dados['status']}")
                                print(f"  Prioridade: {dados['prioridade']}")
                                print(f"  Descrição:  {dados['desc_pedido']}")
                                print(f"  Status:     {dados['pendente']})")
                                print("-"*30)
                        
                    case 4:
                        funcoes.limpar_menu()
                    case 5:
                        funcoes.limpar_menu()
                    case 6:
                        funcoes.limpar_menu()
                
                
        

        case 6:
            opcao = 1
            opc = 0

            
    print(pedidos)
