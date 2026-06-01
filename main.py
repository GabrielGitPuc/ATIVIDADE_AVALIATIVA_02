import funcoes
import os
inicio = 0

operador = {}
pedidos = {}
entregador = {}
funcoes.limpar_menu()
while inicio == 0:
    print("="*30)
    print("FluxoNorte")
    print("="*30)
    print('''
[1] Sistema - Login
[2] Sistema - Cadastro ''')
    
    comeco = funcoes.ler_opcao([1, 2])
    match comeco:
        case 1:
            funcoes.limpar_menu()
            print("="*30)
            print("Login - Operador")
            print("="*30)
            Nome = input("Digite seu nome: ")
            Registro = input("Digite seu número de registro: ")
           
            if Registro in operador and operador[Registro]['nome'].lower() == Nome.lower():
                print("Login realizado com sucesso")
                inicio = 1
                while inicio == 1:
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
                                'disponibilidade' : input("Digite se está disponível(sim/nao): ")
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
                                            id_pedidos = input("Digite o ID do pedido que deseja associar ao entregador: ")
                                            if id_pedidos in pedidos:
                                                id_entregador = input("Digite o ID do entregador: ")
                                                if id_entregador in entregador:
                                                    pedidos [id_pedidos] ['id_entregador'] = id_entregador
                                                    print(f'Entregador {id_entregador} associado ao pedido {id_pedidos}')
                                                    if id_pedidos in entregador[id_entregador] > funcoes.limite_veiculo:
                                                        print("Limite de pedidos excedido!") 
                                                else:
                                                    print('Entregador não encontrado')
                                            else: 
                                                print('Pedido não encontrado')
                                        case 4:
                                            funcoes.limpar_menu()
                                            id_pedidos = input("Digite o ID do pedido que deseja remover a associação: ")
                                            if id_pedidos in pedidos:
                                                associado = pedidos[id_pedidos].get('id_entregador')
                                                if associado:                                # ← verifica se há entregador associado
                                                    pedidos[id_pedidos]['id_entregador'] = None
                                                    print(f'Entregador {associado} desassociado do pedido {id_pedidos}.')
                                                else:
                                                    print('Este pedido não possui entregador associado.')
                                            else:
                                                print('Pedido não encontrado.')

                                        case 5:
                                            funcoes.limpar_menu()
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
                                                    print(f"  Prioridade: {dados['prioridade']}")
                                                    print(f"  Descrição:  {dados['desc_pedido']}")
                                                    print(f"  Status:     {dados['status']}")
                                                    print("-"*30)

                                        case 2:
                                            funcoes.limpar_menu()
                                            print("="*30)
                                            print('Pedidos Entregues')
                                            print("="*30)
                                            for id_e, dados in pedidos.items():
                                                if dados['status'].lower() == 'entregue':
                                                    print(f'ID: {id_e}')
                                                    print(f"  Cliente:    {dados['nome']}")
                                                    print(f"  Status:     {dados['status']}")
                                                    print(f"  Prioridade: {dados['prioridade']}")
                                                    print(f"  Descrição:  {dados['desc_pedido']}")
                                                    print("-"*30)

                                        case 3:
                                            funcoes.limpar_menu()
                                            print("="*30)
                                            id_pedidos = input("Digite o ID do pedido que deseja buscar: ")
                                            if id_pedidos in pedidos:
                                                dados = pedidos[id_pedidos]
                                                print(f"  ID:           {id_pedidos}")  
                                                print(f"  Cliente:    {dados['nome']}")
                                                print(f"  Status:     {dados['status']}")
                                                print(f"  Prioridade: {dados['prioridade']}")
                                                print(f"  Descrição:  {dados['desc_pedido']}")
                                                print("-"*30)
                                            else:
                                                print("Pedido não encontrado.")
                                            
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
                                            id_entregador = input("Digite o ID do entregador que deseja consultar: ")
                                            if id_entregador in entregador:                 # ← valida se entregador existe
                                                pedidos_totalentregador = 0
                                                for id_p, dados_p in pedidos.items():       # ← itera sobre pedidos
                                                    if (dados_p.get('id_entregador') == id_entregador
                                                            and dados_p['status'].lower() == 'entregue'):
                                                        pedidos_totalentregador += 1
                                                        print(f'  Pedido ID: {id_p}')
                                                        print(f"  Cliente:   {dados_p['nome']}")
                                                        print("-"*30)
                                                nome = entregador[id_entregador]['nome_entregador']
                                                print(f"Entregador: {nome}")
                                                print(f"Total de entregas concluídas: {pedidos_totalentregador}")
                                                if pedidos_totalentregador == 0:
                                                    print("Nenhuma entrega concluída ainda.")
                                                else:
                                                    print(f"Total de entregas concluídas: {pedidos_totalentregador}")
                                            else:
                                                print("Entregador não encontrado.")

                                        case 6:
                                            funcoes.limpar_menu()
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
                                    relatorios = funcoes.ler_opcao([1, 2, 3, 4, 5])
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
                                            funcoes.limpar_menu()
                                            print('='*30)
                                            print('PRIORIDADE - ALTA')
                                            print('='*30)
                                            priori_alta = 0
                                            for id_p, dados in pedidos.items():              # ← itera corretamente
                                                if dados['prioridade'].lower() == 'alta':    # ← acessa via dados
                                                    priori_alta += 1
                                                    print(f'  Pedido ID:  {id_p}')
                                                    print(f"  Cliente:    {dados['nome']}")
                                                    print(f"  Prioridade: {dados['prioridade']}")
                                                    print(f"  Descrição:  {dados['desc_pedido']}")
                                                    print(f"  Status:     {dados['status']}")
                                                    print("-"*30)
                                            if priori_alta == 0:
                                                print("Nenhum pedido com prioridade alta.")
                                            else:
                                                print(f"Total com prioridade alta: {priori_alta}")
                                            print('='*30)
                                        
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
                                            funcoes.limpar_menu()
                                            rel_op = 0

                            case 6:
                                funcoes.limpar_menu()
                                operario = input("Digite seu código de operário: ")
                                fechamento = input("Deseja encerrar o sistema? (sim/não):  ")
                                fechamento = fechamento.lower()
                                if operario in operador and fechamento == 'sim':
                                    print('Sistema finalizado!')
                                else:
                                    print('Sua tentativa falhou, tente novamente')
                                    continue
                                continue

            else:
                print('Usuário não cadastrado. Tente novamente com as credenciais corretas.')
                continue

        case 2:
            funcoes.limpar_menu()
            print('='*30)
            print('Cadastro - OPERADOR')
            print('='*30)
            Registro_Operador = funcoes.RO()
            operador[Registro_Operador] = {
            'nome': input("Digite seu nome: ").lower()
            }
            print('Obrigado! Agora segue seu Registro de Operador, faça o login utilzando nome e registro.')
            print(f'Registro de Operador: {Registro_Operador}')

            inicio = 0
