# -*- coding: utf-8 -*-

## --- Funções Auxiliares (As "Ferramentas") ---

def calcular_media(lista_de_notas):
    """Recebe uma lista de notas e retorna a média."""
    # SEU CÓDIGO AQUI: Se a lista estiver vazia, retorne 0.0.
    # Senão, calcule e retorne a média (soma / quantidade).
    if not lista_de_notas:
        return 0.0
    return sum(lista_de_notas)/len(lista_de_notas)

def verificar_aprovacao(media):
    """Recebe uma média e retorna 'Aprovado' ou 'Reprovado'."""
    # SEU CÓDIGO AQUI: Use um 'if' para verificar se a média é >= 7.0.
    media = float(media)
    if media >= 7.0:
        print("Aluno aprovado! ")
    else:
        print("Aluno reprovado! ")

## --- Funções Principais (As "Operações do Menu") ---

def criar_sala(linhas, colunas):
    sala = []  # Começa com a matriz vazia
    
    # Laço de fora para criar cada linha
    for i in range(linhas):
        nova_linha = []  # Cria uma lista vazia para representar a nova linha
        
        # Laço de dentro para adicionar cada carteira (dicionário) à nova linha
        for j in range(colunas):
            carteira_padrao = {"status": "livre", "aluno": {"id": None, "nome": None, "notas": []}}
            nova_linha.append(carteira_padrao)
            
        # Adiciona a linha, já preenchida com as carteiras, à matriz principal
        sala.append(nova_linha)
        
    return sala

def exibir_mapa(sala):
    """Exibe o mapa da sala mostrando [L] para livre e [O] para ocupado."""
    print("\n--- Mapa da Sala ---")
    # SEU CÓDIGO AQUI: Percorra a matriz com laços aninhados.
    # Para cada carteira, verifique o seu 'status' e imprima '[ L ]' ou '[ O ]'.
    # Use 'print(..., end="")' para não pular de linha.
    for linhas in sala:
        linha = ''
        for colunas in linhas:
            if colunas['status'] == 'livre':
                linha += '[ L ] '
            else:
                linha += '[ O ] '
        print(linha)
                
    pass

def alocar_aluno(sala, proximo_id):
    print("\n--- Alocar Novo Aluno ---")
    
    try:
        # 1. Pede a linha e a coluna ao utilizador
        # (Para o utilizador, as linhas/colunas começam em 1)
        linha_usr = int(input("Digite a fila desejada: "))
        coluna_usr = int(input("Digite a carteira desejada: "))

        # 2. Converte para os índices da matriz (que começam em 0)
        linha_idx = linha_usr - 1
        coluna_idx = coluna_usr - 1

        # 3. Valida se os índices estão dentro dos limites da sala
        if 0 <= linha_idx < len(sala) and 0 <= coluna_idx < len(sala[0]):
            
            # 4. Acede DIRETAMENTE à carteira (dicionário)
            carteira = sala[linha_idx][coluna_idx]
            
            # 5. Verifica o status DESSA carteira
            if carteira['status'] == 'livre':
                nome_aluno = input("Digite o nome do novo aluno: ")
                
                # 6. Modifica o dicionário da carteira encontrada
                carteira['status'] = 'ocupado'
                carteira['aluno']['id'] = proximo_id
                carteira['aluno']['nome'] = nome_aluno
                # A lista de 'notas' já está lá, vazia
                
                print(f"Aluno '{nome_aluno}' alocado no lugar [{linha_usr}][{coluna_usr}] com sucesso!")
                
                # Retorna o próximo ID para ser usado
                return proximo_id + 1
            else:
                # Se a carteira específica já estava ocupada
                print("Erro: Este lugar já está ocupado!")
        else:
            # Se o utilizador digitou um número fora do mapa
            print("Erro: Posição inválida. Fora dos limites da sala.")

    except ValueError:
        print("Erro: Por favor, digite apenas números.")

    # Se algo deu errado (lugar ocupado, erro de input, etc.), 
    # retorna o 'proximo_id' sem o alterar.
    return proximo_id
    

def lancar_notas_aluno(sala):
    """Encontra um aluno por ID e lança notas para ele."""
    print("\n--- Lançar Notas ---")
    # SEU CÓDIGO AQUI:
    # 1. Peça o ID do aluno.
    # 2. Percorra a matriz inteira para encontrar o aluno com esse ID.
    # 3. Se encontrar, peça as notas e adicione-as à lista de 'notas' do aluno.
    # 4. Se não encontrar, mostre uma mensagem de erro.
    id_aluno = int(input("Digite o ID do aluno: "))
    aluno_encontrado = None
    
    for linha in sala:
        for carteira in linha:
            if carteira['status'] == 'ocupado' and carteira['aluno']['id'] == id_aluno:
                aluno_encontrado = carteira['aluno']
                break
        if aluno_encontrado:
            break


    if aluno_encontrado:
        while True:
            nota_str = input(f"Digite a nota do aluno {aluno_encontrado['nome']}: ")
            if nota_str.lower() == 'fim':
                break
            try:
                nota = float(nota_str)
                aluno_encontrado['notas'].append(nota)
                print(f"A nota {nota} foi adicionada! ")
            except ValueError:
                print("Digite um numero valido! ")
    else:
        print("O aluno com este ID nao foi encontrado!")

def gerar_relatorio_geral(sala):
    """Exibe um relatório com a média e situação de cada aluno."""
    print("\n--- Relatório Geral da Turma ---")
    # SEU CÓDIGO AQUI:
    # 1. Percorra a matriz inteira.
    # 2. Para cada carteira com status 'ocupado':
    #    a. Pegue a lista de notas do aluno.
    #    b. Chame a sua função 'calcular_media()' com essa lista.
    #    c. Chame a sua função 'verificar_aprovacao()' com a média calculada.
    #    d. Imprima os resultados formatados (ID, Nome, Média, Situação).
    aluno_encontrado = False
    for linha in sala:
        for carteira in linha:
            if carteira['status'] == 'ocupado':
                aluno_encontrado = True
                aluno = carteira['aluno']
                notas_do_aluno = aluno['notas']
                media = calcular_media(notas_do_aluno)
                situacao = verificar_aprovacao(media)
                print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | Média: {media:.1f} | Situação: {situacao}")
            else:
                print("Livre")
            

def gerar_ranking_da_turma(sala):
    """Exibe os alunos ordenados pela maior média."""
    print("\n--- Ranking da Turma ---")
    # SEU CÓDIGO AQUI (Este é o mais desafiador):
    # 1. Crie uma lista temporária.
    # 2. Percorra a matriz e, para cada aluno, calcule a sua média.
    # 3. Adicione um par (tupla) ou dicionário (ex: {'nome': nome, 'media': media}) à lista temporária.
    # 4. Ordene a lista temporária pela média, da maior para a menor.
    # 5. Imprima o ranking.
     # 1. Crie uma lista temporária para guardar os dados do ranking
    lista_para_ranking = []

    # 2. Percorra a sala para encontrar cada aluno e calcular a sua média
    for linha in sala:
        for carteira in linha:
            if carteira['status'] == 'ocupado':
                aluno = carteira['aluno']
                
                # Reutilize a sua função 'calcular_media'
                media_do_aluno = calcular_media(aluno['notas'])
                
                # 3. Adicione um dicionário simples à lista de ranking
                lista_para_ranking.append({
                    'nome': aluno['nome'],
                    'media': media_do_aluno
                })

    # 4. Verifique se existe alguém para ordenar
    if not lista_para_ranking:
        print("Nenhum aluno na turma para gerar ranking.")
        return # Sai da função

    # 5. Use sorted() com a 'key' para ordenar pela média
    #    - key=lambda aluno: aluno['media'] diz: "Para cada dicionário 'aluno', use o valor da chave 'media' para ordenar."
    #    - reverse=True diz: "Ordene do maior para o menor."
    ranking_ordenado = sorted(lista_para_ranking, key=lambda aluno: aluno['media'], reverse=True)
    
    # 6. Imprima o ranking final
    for i, aluno_rank in enumerate(ranking_ordenado):
        # enumerate(lista) é uma forma de obter o índice (i) e o item ao mesmo tempo
        print(f"{i + 1}º Lugar: {aluno_rank['nome']} - Média: {aluno_rank['media']:.1f}")

                
                


## --- Programa Principal ---

if __name__ == "__main__":
    try:
        linhas = int(input("Digite o número de filas na sala: "))
        colunas = int(input("Digite o número de carteiras por fila: "))
    except ValueError:
        print("Entrada inválida. A usar tamanho padrão 3x3.")
        linhas, colunas = 3, 3

    # Cria a sala e o contador de ID
    sala_de_aula = criar_sala(linhas, colunas)
    proximo_id = 1
    
    # Laço principal do menu
    while True:
        print("\n--- Sistema de Gestão de Pautas da Turma ---")
        print("[1] - Alocar Aluno a um Lugar")
        print("[2] - Lançar Notas para um Aluno")
        print("[3] - Gerar Relatório Geral da Turma")
        print("[4] - Exibir Ranking da Turma")
        print("[5] - Exibir Mapa da Sala")
        print("[6] - Sair")
        print("---------------------------------------------")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")
            continue

        if opcao == 1:
            # A função deve retornar o novo ID para atualizarmos a nossa variável
            proximo_id = alocar_aluno(sala_de_aula, proximo_id)
        elif opcao == 2:
            lancar_notas_aluno(sala_de_aula)
        elif opcao == 3:
            gerar_relatorio_geral(sala_de_aula)
        elif opcao == 4:
            gerar_ranking_da_turma(sala_de_aula)
        elif opcao == 5:
            exibir_mapa(sala_de_aula)
        elif opcao == 6:
            print("A sair do sistema. Até à próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.") 