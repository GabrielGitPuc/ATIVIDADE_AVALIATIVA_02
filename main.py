import funcoes
import os
opcao = 0

pedidos = {}
entregador = {}
funcoes.limpar_menu()

while opcao == 0:
    print("="*30)
    print("FluxoNorte")
    print("="*30)
    print('''           
[1] Cadastro entregador
[2] Cadastro pedido
[3] Atualizar Pedidos 
[4] Informações 
[5] Relatórios Operacionais
[6] Finalizar Sistema ''')
    
    opc = funcoes.ler_opcao([1,2,3,4,5,6])
    match opc:
        case 1:
            funcoes.limpar_menu()
            id_entregador = funcoes.ID_entregador()
            print(id_entregador)

            veiculo = input("Digite o tipo de veiculo(Caminhão/van): ")

            entregador[id_entregador] = {
            'nome_entregador': input("Digite o nome do Entregador: "),
            'veiculo': veiculo,
            'limite': funcoes.limite_veiculo(veiculo),
            'pedidos_atuais': 0,
            'disponibilidade': input("Digite a disponibilidade do entregador (Disponivel/indisponivel): ")
            }
            
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
                atualizar = funcoes.ler_opcao([1,2,3,4,5])
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
                                if funcoes.verificar_limite(id_entregador, entregador):
                                    pedidos[id_pedidos]['id_entregador'] = id_entregador
                                    entregador[id_entregador]['pedidos_atuais'] += 1 
                                    print(f'Entregador {id_entregador} associado ao pedido {id_pedidos}')
                                else:
                                    print(f'Entregador {id_entregador} já atingiu o limite!')
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
                                entregador[id_entregador]['pedidos_atuais'] -= 1
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
                informações = funcoes.ler_opcao([1,2,3,4,5,6])

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
                        for id_e, dados in pedidos.items():
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
                                print("-"*30)
                        
                    case 4:
                        funcoes.limpar_menu()
                        print("="*30)
                        print("Entregadores Disponiveis:")
                        print("="*30)
                        disponiveis = 0
                        for id_e, dados in entregador.items():
                            if dados['disponibilidade'].lower() == 'sim':
                                disponiveis += 1
                                print(f"ID: {id_e}")
                                print(f" Nome: {dados['nome_entregador']}")
                                print(f" Veiculo: {dados['veiculo']}")
                                print("="*30)

                        if disponiveis == 0:
                            print("nenhum entregador disponivel")

                    case 5:
                        funcoes.limpar_menu()
                        print("="*30)
                        print("Entregas por entregador")
                        print("="*30)
                        pedidos_totalentregador = 0
                        id_entregador = int(input("Digite o ID do entregador que deseja consultar: "))
                        for id_e, dados in entregador.items():
                            if id_pedidos['status'] == 'Entregue':
                                pedidos_totalentregador +=1
                                print(f'ID: {id_e}')
                                print(f" Nome: {dados['nome_entregador']}")
                                print(f'Total de entregas: {pedidos_totalentregador}')
                            else:
                                (f'O entregador não há entregas concluídas')

                    case 6:
                        info = 0
        case 5:
            funcoes.limpar_menu()
            rel_op = 1
            while rel_op == 1:
                print('''      
[1] Total de pedidos 
[2] Quantidade de pedidos por status 
[3] Pedidos com Alta Prioridade
[4] Entregador com o maior número de entrega
[5] Voltar
''')   
                relatorios = int(input("Escolha uma opção: "))
                match relatorios:
                    case 1:
                        print("="*30)    
                        total = len(pedidos)
                        print(f"Total de pedidos cadastrados: {total}")
                        if total == 0:
                            print("Nenhum pedido cadastrado ainda.")
                        print("="*30)

                    case 2:
                        funcoes.limpar_menu()
                        print("="*30)
                        print("Pedidos por Status")
                        
                        contagem = {}
                        
                        for id_p, dados in pedidos.items():
                            status = dados['status'].lower()
                            if status in contagem:
                                contagem[status] += 1
                            else:
                                contagem[status] = 1
                        
                        if len(contagem) == 0:
                            print("Nenhum pedido cadastrado.")
                        else:
                            for status, quantidade in contagem.items():
                                print(f"{status}: {quantidade} pedido(s)")
                        
                        print("="*30)
                    
                    case 3:
                        print('='*30)
                        print('PRIORIDADE - ALTA')
                        print('='*30)
                        priori_alta = 0
                        for pedi_al in pedidos:
                            if id_pedidos['prioridade'] == 'Alta':
                                priori_alta +=1
                                print(f"Número de pedidos com prioridade alta: {priori_alta}")
                        print('='*30)
                        for id_pedidos, dados in pedidos.items():
                            if id_pedidos['prioridade'] == 'Alta':
                                print(f"  Cliente:    {dados['nome']}\n")
                                print(f"  Prioridade: {dados['prioridade']}\n")
                                print(f"  Descrição:  {dados['desc_pedido']}\n")
                                print(f"  Status:     {dados['status']}\n")
                    
                    case 4:
                        print('='*30)
                        print('Entregador com mais pedidos')
                        print('='*30)
                        
                        
                        contagem = {}
                        
                        for id_p, dados in pedidos.items():
                            
                            if dados.get('status', '').lower() == 'entregue' and dados.get('id_entregador'):
                                id_ent = dados['id_entregador']
                                if id_ent in contagem:
                                    contagem[id_ent] += 1
                                else:
                                    contagem[id_ent] = 1
                        
                        if contagem:
                            id_maior = max(contagem, key=contagem.get)
                            nome = entregador[id_maior]['nome_entregador']
                            total = contagem[id_maior]
                            
                            print(f"ID:     {id_maior}")
                            print(f"Nome:   {nome}")
                            print(f"Total de entregas: {total}")
                        else:
                            print("Nenhuma entrega concluída ainda.")
                        
                        print('='*30)
                    
                    case 5:
                        rel_op = 0

        case 6:
            funcoes.limpar_menu()
            fechamento = input("Deseja encerrar o sistema? (sim/não):  ")
            fechamento.lower()
            if fechamento == 'sim':
                print('Sistema finalizado!')
            else:
                print('Sua tentativa falhou, tente novamente')
                continue
            continue


print(pedidos)
