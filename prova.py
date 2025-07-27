# -*- coding: utf-8 -*-

# --- FUNÇÕES A SEREM RESOLVIDAS ---

def calcular_soma_trabalhos_especificos(matriz_notas):
    soma_total = 0.0  # Apenas uma variável de soma é necessária
    
    # Percorremos a matriz apenas UMA vez
    # O laço 'for linha in matriz_notas:' é uma forma mais direta de percorrer as linhas
    for linha in matriz_notas:
        # 'linha' aqui é uma lista como [8.0, 7.5, 9.0, 8.5]
        
        # Somamos o primeiro (índice 0) e o último (índice 3) elemento da linha
        soma_total = soma_total + linha[0] + linha[3]
    
    return soma_total

def contar_alunos_em_risco(lista_faltas):
    """
    (Similar a 'contarQuantosUnicos')
    Objetivo: Contar quantos alunos estão em risco por faltas.
    Um aluno é considerado em risco se tiver MAIS de 15 faltas.
    A função deve retornar o número de alunos em risco.
    """
    alunos_em_risco = 0
    
    # Crie seu código aqui...
    # Dica: Percorra a 'lista_faltas'. Para cada número de faltas,
    # verifique se ele é maior que 15. Se for, incremente o contador.
    
    for i in range(len(lista_faltas)):
        if lista_faltas[i] > 15:
            alunos_em_risco += 1


    return alunos_em_risco

def substituir_notas_extremas(lista_notas):
    """
    (Similar a 'removerExtremos')
    Objetivo: Encontrar a maior e a menor nota de participação.
    A função deve retornar uma NOVA lista onde todas as ocorrências
    da maior e da menor nota foram substituídas pelo valor 0.0.
    """
    
    # Crie seu código aqui...
    # Dica: O processo tem 2 fases.
    # 1. Encontre a maior e a menor nota usando as funções max() e min().
    # 2. Crie uma nova lista vazia. Percorra a lista original e, para cada nota,
    #    decida se adiciona a própria nota ou o valor 0.0 à nova lista.

    maior = max(lista_notas)
    menor = min(lista_notas)
    retorno = []
    for nota in lista_notas:
        if nota == maior or nota == menor:
            retorno.append(0.0)
        else:
            retorno.append(nota)
    
    return retorno # Retorna uma lista vazia por padrão


# --- DADOS E BLOCO DE TESTE (NÃO ALTERAR) ---

if __name__ == "__main__":
    
    # --- DADOS DA TURMA ---
    
    # Notas dos trabalhos de 5 alunos (5 linhas), 4 trabalhos (4 colunas)
    matriz_notas = [
        [8.0, 7.5, 9.0, 8.5],  # Aluno 0
        [6.0, 7.0, 7.0, 8.0],  # Aluno 1
        [10.0, 9.5, 9.8, 9.0], # Aluno 2
        [4.0, 5.0, 6.5, 5.5],  # Aluno 3
        [9.0, 8.5, 8.8, 9.2]   # Aluno 4
    ]
    
    # Lista com as faltas de cada um dos 5 alunos
    lista_faltas = [10, 20, 5, 18, 2]
    
    # Lista com as notas de participação de cada um dos 5 alunos
    lista_notas_participacao = [9.5, 7.0, 10.0, 5.0, 9.5]

    # --- VERIFICAÇÃO DOS RESULTADOS ---
    
    print("--- Análise de Desempenho da Turma ---")
    
    # Teste da Questão 1 (COM O VALOR CORRIGIDO)
    soma_trabalhos = calcular_soma_trabalhos_especificos(matriz_notas)
    print("\nQuestão 1: Soma dos Trabalhos 1 e 4")
    if 77.2 == soma_trabalhos: # <-- VALOR CORRIGIDO
        print("CERTA!    =D")
    else:
        print(f"ERRADA!   =( Resultado obtido: {soma_trabalhos}, esperado: 77.2")

    # Teste da Questão 2
    alunos_risco = contar_alunos_em_risco(lista_faltas)
    print("\nQuestão 2: Alunos em Risco por Faltas")
    if 2 == alunos_risco:
        print("CERTA!    =D")
    else:
        print(f"ERRADA!   =( Resultado obtido: {alunos_risco}, esperado: 2")

    # Teste da Questão 3
    notas_substituidas = substituir_notas_extremas(lista_notas_participacao)
    resultado_esperado = [9.5, 7.0, 0.0, 0.0, 9.5] # Substituiu 10.0 (maior) e 5.0 (menor)
    print("\nQuestão 3: Substituição de Notas Extremas")
    if resultado_esperado == notas_substituidas:
        print("CERTA!    =D")
    else:
        print(f"ERRADA!   =( Resultado obtido: {notas_substituidas}, esperado: {resultado_esperado}")