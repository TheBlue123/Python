# -*- coding: utf-8 -*-

# --- FUNÇÕES A SEREM RESOLVIDAS ---

def calcular_media_temperaturas_sem_extremos(matriz_leituras):
    """
    Objetivo: Calcular a média de temperatura de CADA sensor, mas com uma regra:
    a maior e a menor leitura de cada sensor devem ser DESCARTADAS antes de calcular a média.
    A função deve retornar uma LISTA com a média de cada sensor.
    Exemplo de retorno: [22.5, 25.0, 19.8]
    """
    medias_finais = []
    
    # Crie seu código aqui...
    # Dica: Percorra a matriz de leituras linha por linha (cada linha é um sensor).
    # Para cada linha (lista de temperaturas):
    #   1. Encontre o maior e o menor valor.
    #   2. Crie uma nova lista temporária sem esses dois valores.
    #   3. Calcule a média da lista temporária.
    #   4. Adicione essa média à lista 'medias_finais'.

    for linhas in matriz_leituras:
        maior = max(linhas)
        menor = min(linhas)
        copialista = list(linhas)

        copialista.remove(maior)
        copialista.remove(menor)
        
        if copialista:
            media = sum(copialista)/len(copialista)
        else:
            media = 0
        medias_finais.append(media)

    
    return medias_finais

def encontrar_sensores_alerta(lista_humidade, lista_vento):
    """
    Objetivo: Identificar os sensores que estão em estado de alerta.
    Um sensor está em alerta se a sua HUMIDADE for MAIOR que 85 OU
    a sua VELOCIDADE DO VENTO for MAIOR que 60.
    A função deve retornar uma LISTA com os ÍNDICES dos sensores em alerta.
    Exemplo de retorno: [1, 3] (significa que o sensor 1 e o sensor 3 estão em alerta).
    """
    contador = 0
    indices_alerta = []
    
    # Crie seu código aqui...
    # Dica: Percorra as listas de humidade e vento usando um laço com 'range(len(...))'
    # para ter acesso ao índice 'i'.
    # Em cada iteração, verifique a condição de alerta usando 'or'.
    # Se a condição for verdadeira, adicione o ÍNDICE 'i' à lista 'indices_alerta'.
    for i in range(len(lista_humidade)):
        humidade = lista_humidade[i]
        vento = lista_vento[i]
        if humidade > 85 or vento > 60:
            contador += 1
            indices_alerta.append(i)
            
    
    
    
    return indices_alerta

def categorizar_temperaturas(matriz_leituras):
    """
    Objetivo: Contar quantas leituras de temperatura caem em cada categoria.
    As categorias são: "Frio" (abaixo de 20), "Ameno" (de 20 a 29) e "Quente" (30 ou mais).
    A função deve retornar um DICIONÁRIO com a contagem para cada categoria.
    Exemplo de retorno: {'Frio': 5, 'Ameno': 10, 'Quente': 3}
    """
    
    # Crie seu código aqui...
    # Dica: Crie um dicionário inicial: categorias = {"Frio": 0, "Ameno": 0, "Quente": 0}.
    # Use laços aninhados para percorrer CADA valor da matriz.
    # Para cada temperatura, use if/elif/else para descobrir a qual categoria ela pertence
    # e incremente o valor correspondente no dicionário.
    
    categorias = {"Frio": 0, "Ameno": 0, "Quente": 0}
    for linha in matriz_leituras: 
        for temperatura in linha:
         if temperatura < 20:
             categorias["Frio"] += 1
         elif 20 <= temperatura <= 29:
             categorias["Ameno"] += 1
         else:
             categorias["Quente"] +=1
    
    
    
    return categorias # Retorna um dicionário vazio por padrão


# --- DADOS E BLOCO DE TESTE (NÃO ALTERAR) ---

if __name__ == "__main__":
    
    # --- DADOS DOS SENSORES ---
    
    # 4 sensores (linhas), 6 leituras de temperatura cada (colunas)
    matriz_leituras = [
        [22, 25, 18, 30, 28, 19],  # Sensor 0
        [28, 29, 31, 35, 27, 26],  # Sensor 1
        [15, 18, 22, 25, 21, 17],  # Sensor 2
        [32, 33, 29, 28, 35, 30]   # Sensor 3
    ]
    
    # Lista com a humidade de cada um dos 4 sensores
    lista_humidade = [80, 92, 75, 88]
    
    # Lista com a velocidade do vento de cada um dos 4 sensores
    lista_vento = [45, 55, 65, 50]

    # --- VERIFICAÇÃO DOS RESULTADOS ---
    
    print("--- Análise de Dados dos Sensores ---")
    
    # Teste da Questão 1
    medias = calcular_media_temperaturas_sem_extremos(matriz_leituras)
    # O bloco de teste CORRIGIDO
    resultado_esperado_q1 = [23.5, 28.75, 19.5, 31.0] # <--- VALORES CORRIGIDOS AQUI
    print("\nQuestão 1: Média de Temperaturas (sem extremos)")
    if all(abs(a - b) < 0.01 for a, b in zip(medias, resultado_esperado_q1)):
        print("CERTA!    =D")
    else:
        print(f"ERRADA!   =( Resultado obtido: {medias}, esperado: {resultado_esperado_q1}")
    # Teste da Questão 2
    alertas = encontrar_sensores_alerta(lista_humidade, lista_vento)
    resultado_esperado_q2 = [1, 2, 3]
    print("\nQuestão 2: Sensores em Alerta")
    if resultado_esperado_q2 == alertas:
        print("CERTA!    =D")
    else:
        print(f"ERRADA!   =( Resultado obtido: {alertas}, esperado: {resultado_esperado_q2}")

    # Teste da Questão 3
    categorias = categorizar_temperaturas(matriz_leituras)
    resultado_esperado_q3 = {'Frio': 5, 'Ameno': 12, 'Quente': 7}
    print("\nQuestão 3: Contagem de Temperaturas por Categoria")
    if resultado_esperado_q3 == categorias:
        print("CERTA!    =D")
    else:
        print(f"ERRADA!   =( Resultado obtido: {categorias}, esperado: {resultado_esperado_q3}")