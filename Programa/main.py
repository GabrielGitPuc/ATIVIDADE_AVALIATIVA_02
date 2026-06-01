import funcoes
import os

inicio = 0

operador = {}
pedidos = {}
entregador = {}

funcoes.limpar_menu()

while inicio == 0:
    print("=" * 30)
    print("FluxoNorte")
    print("=" * 30)
    print('''
[1] Sistema - Login
[2] Sistema - Cadastro ''')

    comeco = funcoes.ler_opcao([1, 2])

    match comeco:
        case 1:
            funcoes.limpar_menu()
            print("=" * 30)
            print("Login - Operador")
            print("=" * 30)
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

                    opc = funcoes.ler_opcao([1, 2, 3, 4, 5, 6])

                    match opc:

                        case 1:
                            funcoes.limpar_menu()
                            print("=" * 30)
                            print("Cadastro de Entregador")
                            print("=" * 30)

                            nome_ent = input("Digite o nome do Entregador: ")

                            if funcoes.nome_entregador_existe(entregador, nome_ent):
                                print("❌ Entregador já cadastrado com esse nome!")
                            else:
                                id_entregador = funcoes.ID_entregador()

                                print("Tipos de veículo disponíveis: carro / van / moto")
                                veiculo = input("Digite o tipo de veículo: ").lower()

                                opcoes_veiculo_validas = 0
                                while opcoes_veiculo_validas == 0:
                                    if veiculo in ['carro', 'van', 'moto']:
                                        opcoes_veiculo_validas = 1
                                    else:
                                        print("Veículo inválido. Digite: carro, van ou moto")
                                        veiculo = input("Digite o tipo de veículo: ").lower()

                                print("Disponibilidade: sim / nao")
                                disponibilidade = input("Está disponível? ").lower()
                                disp_valida = 0
                                while disp_valida == 0:
                                    if disponibilidade in ['sim', 'nao']:
                                        disp_valida = 1
                                    else:
                                        print("Digite apenas 'sim' ou 'nao'.")
                                        disponibilidade = input("Está disponível? ").lower()

                                entregador[id_entregador] = {
                                    'nome_entregador': nome_ent,
                                    'veiculo': veiculo,
                                    'limite': funcoes.limite_veiculo(veiculo),
                                    'disponibilidade': disponibilidade
                                }
                                print(f"✅ Entregador ID:{id_entregador} cadastrado com sucesso!")
                                print(f"   Limite de pedidos simultâneos: {funcoes.limite_veiculo(veiculo)}")

                        case 2:
                            funcoes.limpar_menu()
                            print("=" * 30)
                            print("Cadastro de Pedido")
                            print("=" * 30)

                            id_pedidos = funcoes.ID_pedido()
                            print(f"ID do Pedido: {id_pedidos}")

                            print("Prioridade disponível: Alta / Normal")
                            prioridade = input("Digite a Prioridade: ").capitalize()
                            prior_valida = 0
                            while prior_valida == 0:
                                if prioridade in ['Alta', 'Normal']:
                                    prior_valida = 1
                                else:
                                    print("Prioridade inválida. Digite: Alta ou Normal")
                                    prioridade = input("Digite a Prioridade: ").capitalize()

                            pedidos[id_pedidos] = {
                                'nome': input("Digite o nome do Cliente: "),
                                'endereco': input("Digite o Endereço: "),
                                'prioridade': prioridade,
                                'desc_pedido': input("Digite a descrição do pedido: "),
                                'status': funcoes.selecionar_status(),
                                'id_entregador': None
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
                                atualizar = funcoes.ler_opcao([1, 2, 3, 4, 5])

                                match atualizar:
                                    case 1:
                                        funcoes.limpar_menu()
                                        id_pedidos = input("Digite o ID do pedido que deseja alterar: ")
                                        if id_pedidos in pedidos:
                                            status_atual = pedidos[id_pedidos]['status'].lower()
                                            if status_atual == 'cancelado':
                                                print("⚠️  Este pedido está cancelado.")
                                                reativar = input("Deseja reativá-lo? (sim/nao): ").lower()
                                                reativar_valido = 0
                                                while reativar_valido == 0:
                                                    if reativar in ['sim', 'nao']:
                                                        reativar_valido = 1
                                                    else:
                                                        print("Digite apenas 'sim' ou 'nao'.")
                                                        reativar = input("Deseja reativá-lo? (sim/nao): ").lower()
                                                if reativar == 'sim':
                                                    pedidos[id_pedidos]['status'] = funcoes.selecionar_status()
                                                    print("✅ Pedido reativado e status atualizado com sucesso!")
                                                else:
                                                    print("Operação cancelada.")
                                            else:
                                                pedidos[id_pedidos]['status'] = funcoes.selecionar_status()
                                                print("✅ Status atualizado com sucesso!")
                                        else:
                                            print("Pedido não encontrado.")

                                    case 2:
                                        funcoes.limpar_menu()
                                        id_pedidos = input("Digite o ID do pedido que deseja cancelar: ")
                                        if id_pedidos in pedidos:
                                            if pedidos[id_pedidos]['status'].lower() == 'cancelado':
                                                print("Este pedido já está cancelado.")
                                            else:
                                                pedidos[id_pedidos]['status'] = 'Cancelado'
                                                pedidos[id_pedidos]['id_entregador'] = None
                                                print("✅ Pedido cancelado com sucesso!")
                                        else:
                                            print("Pedido não encontrado.")

                                    case 3:
                                        funcoes.limpar_menu()
                                        id_pedidos = input("Digite o ID do pedido: ")
                                        if id_pedidos in pedidos:
                                            if pedidos[id_pedidos]['status'].lower() == 'cancelado':
                                                print("❌ Não é possível associar entregador a um pedido cancelado.")
                                            else:
                                                id_entregador = input("Digite o ID do entregador: ")
                                                if id_entregador in entregador:
                                                    pedidos_atuais = funcoes.contar_pedidos_entregador(pedidos, id_entregador)
                                                    limite = entregador[id_entregador]['limite']
                                                    if pedidos_atuais >= limite:
                                                        print(f"❌ Limite atingido! Entregador possui {pedidos_atuais} pedido(s) (limite: {limite}).")
                                                    else:
                                                        pedidos[id_pedidos]['id_entregador'] = id_entregador
                                                        print(f"✅ Entregador {id_entregador} associado ao pedido {id_pedidos}.")
                                                        print(f"   Pedidos atuais do entregador: {pedidos_atuais + 1}/{limite}")
                                                else:
                                                    print("Entregador não encontrado.")
                                        else:
                                            print("Pedido não encontrado.")

                                    case 4:
                                        funcoes.limpar_menu()
                                        id_pedidos = input("Digite o ID do pedido que deseja remover a associação: ")
                                        if id_pedidos in pedidos:
                                            associado = pedidos[id_pedidos].get('id_entregador')
                                            if associado:
                                                pedidos[id_pedidos]['id_entregador'] = None
                                                print(f"✅ Entregador {associado} desassociado do pedido {id_pedidos}.")
                                            else:
                                                print("Este pedido não possui entregador associado.")
                                        else:
                                            print("Pedido não encontrado.")

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
[6] Voltar ''')
                                informacoes = funcoes.ler_opcao([1, 2, 3, 4, 5, 6])

                                match informacoes:
                                    case 1:
                                        funcoes.limpar_menu()
                                        print("=" * 30)
                                        print("Pedidos Pendentes")
                                        print("(Alta prioridade primeiro)")
                                        print("=" * 30)
                                        encontrou = 0
                                        pedidos_ordenados = funcoes.ordenar_pedidos_por_prioridade(pedidos)
                                        for id_p, dados in pedidos_ordenados:
                                            if dados['status'].lower() == 'pendente':
                                                encontrou = 1
                                                print(f"ID: {id_p}")
                                                print(f"  Cliente:    {dados['nome']}")
                                                print(f"  Prioridade: {dados['prioridade']}")
                                                print(f"  Descrição:  {dados['desc_pedido']}")
                                                print(f"  Status:     {dados['status']}")
                                                print("-" * 30)
                                        if encontrou == 0:
                                            print("Nenhum pedido pendente.")

                                    case 2:
                                        funcoes.limpar_menu()
                                        print("=" * 30)
                                        print("Pedidos Entregues")
                                        print("=" * 30)
                                        encontrou = 0
                                        for id_e, dados in pedidos.items():
                                            if dados['status'].lower() == 'entregue':
                                                encontrou = 1
                                                print(f"ID: {id_e}")
                                                print(f"  Cliente:    {dados['nome']}")
                                                print(f"  Status:     {dados['status']}")
                                                print(f"  Prioridade: {dados['prioridade']}")
                                                print(f"  Descrição:  {dados['desc_pedido']}")
                                                print("-" * 30)
                                        if encontrou == 0:
                                            print("Nenhum pedido entregue ainda.")

                                    case 3:
                                        funcoes.limpar_menu()
                                        print("=" * 30)
                                        id_pedidos = input("Digite o ID do pedido que deseja buscar: ")
                                        if id_pedidos in pedidos:
                                            dados = pedidos[id_pedidos]
                                            print(f"  ID:           {id_pedidos}")
                                            print(f"  Cliente:      {dados['nome']}")
                                            print(f"  Endereço:     {dados['endereco']}")
                                            print(f"  Status:       {dados['status']}")
                                            print(f"  Prioridade:   {dados['prioridade']}")
                                            print(f"  Descrição:    {dados['desc_pedido']}")
                                            print(f"  Entregador:   {dados.get('id_entregador') or 'Não associado'}")
                                            print("-" * 30)
                                        else:
                                            print("Pedido não encontrado.")

                                    case 4:
                                        funcoes.limpar_menu()
                                        print("=" * 30)
                                        print("Entregadores Disponíveis:")
                                        print("=" * 30)
                                        disponiveis = 0
                                        for id_e, dados in entregador.items():
                                            if dados['disponibilidade'].lower() == 'sim':
                                                disponiveis += 1
                                                pedidos_atuais = funcoes.contar_pedidos_entregador(pedidos, id_e)
                                                print(f"ID: {id_e}")
                                                print(f"  Nome:     {dados['nome_entregador']}")
                                                print(f"  Veículo:  {dados['veiculo']}")
                                                print(f"  Pedidos:  {pedidos_atuais}/{dados['limite']}")
                                                print("=" * 30)
                                        if disponiveis == 0:
                                            print("Nenhum entregador disponível.")

                                    case 5:
                                        funcoes.limpar_menu()
                                        print("=" * 30)
                                        print("Entregas por Entregador")
                                        print("=" * 30)
                                        id_entregador = input("Digite o ID do entregador que deseja consultar: ")
                                        if id_entregador in entregador:
                                            pedidos_totalentregador = 0
                                            for id_p, dados_p in pedidos.items():
                                                if (dados_p.get('id_entregador') == id_entregador
                                                        and dados_p['status'].lower() == 'entregue'):
                                                    pedidos_totalentregador += 1
                                                    print(f"  Pedido ID: {id_p}")
                                                    print(f"  Cliente:   {dados_p['nome']}")
                                                    print("-" * 30)
                                            nome = entregador[id_entregador]['nome_entregador']
                                            print(f"Entregador: {nome}")
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
[4] Entregador com o maior número de entregas
[5] Voltar ''')
                                relatorios = funcoes.ler_opcao([1, 2, 3, 4, 5])

                                match relatorios:
                                    case 1:
                                        print("=" * 30)
                                        total = len(pedidos)
                                        if total == 0:
                                            print("Nenhum pedido cadastrado ainda.")
                                        else:
                                            print(f"Total de pedidos cadastrados: {total}")
                                        print("=" * 30)

                                    case 2:
                                        funcoes.limpar_menu()
                                        print("=" * 30)
                                        print("Pedidos por Status")
                                        print("=" * 30)
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
                                                print(f"  {status.capitalize()}: {quantidade} pedido(s)")
                                        print("=" * 30)

                                    case 3:
                                        funcoes.limpar_menu()
                                        print("=" * 30)
                                        print("PRIORIDADE - ALTA")
                                        print("=" * 30)
                                        priori_alta = 0
                                        pedidos_ordenados = funcoes.ordenar_pedidos_por_prioridade(pedidos)
                                        for id_p, dados in pedidos_ordenados:
                                            if dados['prioridade'].lower() == 'alta':
                                                priori_alta += 1
                                                print(f"  Pedido ID:  {id_p}")
                                                print(f"  Cliente:    {dados['nome']}")
                                                print(f"  Prioridade: {dados['prioridade']}")
                                                print(f"  Descrição:  {dados['desc_pedido']}")
                                                print(f"  Status:     {dados['status']}")
                                                print("-" * 30)
                                        if priori_alta == 0:
                                            print("Nenhum pedido com prioridade alta.")
                                        else:
                                            print(f"Total com prioridade alta: {priori_alta}")
                                        print("=" * 30)

                                    case 4:
                                        print("=" * 30)
                                        print("Entregador com mais entregas")
                                        print("=" * 30)
                                        contagem = {}
                                        for id_p, dados in pedidos.items():
                                            if (dados.get('status', '').lower() == 'entregue'
                                                    and dados.get('id_entregador')):
                                                id_ent = dados['id_entregador']
                                                if id_ent in contagem:
                                                    contagem[id_ent] += 1
                                                else:
                                                    contagem[id_ent] = 1
                                        if contagem:
                                            id_maior = max(contagem, key=contagem.get)
                                            nome = entregador[id_maior]['nome_entregador']
                                            total = contagem[id_maior]
                                            print(f"  ID:                {id_maior}")
                                            print(f"  Nome:              {nome}")
                                            print(f"  Total de entregas: {total}")
                                        else:
                                            print("Nenhuma entrega concluída ainda.")
                                        print("=" * 30)

                                    case 5:
                                        funcoes.limpar_menu()
                                        rel_op = 0

                        case 6:
                            funcoes.limpar_menu()
                            operario = input("Digite seu código de operário: ")
                            fechamento = input("Deseja encerrar o sistema? (sim/nao): ").lower()
                            if operario in operador and fechamento == 'sim':
                                print("Sistema finalizado!")
                                inicio = 2
                            else:
                                print("Sua tentativa falhou, tente novamente.")

            else:
                print("Usuário não cadastrado. Tente novamente com as credenciais corretas.")

        case 2:
            funcoes.limpar_menu()
            print("=" * 30)
            print("Cadastro - OPERADOR")
            print("=" * 30)
            Registro_Operador = funcoes.RO()
            operador[Registro_Operador] = {
                'nome': input("Digite seu nome: ").lower()
            }
            print("Obrigado! Agora segue seu Registro de Operador, faça o login utilizando nome e registro.")
            print(f"Registro de Operador: {Registro_Operador}")
            inicio = 0
