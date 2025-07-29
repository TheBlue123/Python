import pandas as pd
from pathlib import Path

# --- CONFIGURAÇÃO ---
# Todos os dados já estão corretos para o novo arquivo.

# 1. Caminho do arquivo de entrada (ATUALIZADO).
caminho_entrada = r"C:\Users\samur\OneDrive\Documentos\VSCODE\python\Python\trabalho\ESP3 - PROVA 3 (2) (1).xlsx"

# 2. Nome da coluna para ordenar (continua sendo 'polo').
nome_da_coluna_para_ordenar = "Polo"


# 3. Nome do arquivo de saída (ATUALIZADO).
arquivo_saida = "PROVA 3 ESP3 .xlsx"

# --- FIM DA CONFIGURAÇÃO ---

try:
    print(f"--- Processando: {caminho_entrada} ---")
    
    # Lê o arquivo Excel (.xlsx)
    df = pd.read_excel(caminho_entrada)

    # Ordena pela coluna "polo"
    print(f"Ordenando pela coluna '{nome_da_coluna_para_ordenar}'...")
    df_ordenado = df.sort_values(by=nome_da_coluna_para_ordenar, ascending=True)
    
    # Define o caminho de saída completo
    caminho_saida_final = Path(caminho_entrada).parent / arquivo_saida

    # Salva o resultado em um novo arquivo Excel
    df_ordenado.to_excel(caminho_saida_final, index=False)

    print(f"✅ Sucesso! A planilha foi ordenada e salva como '{arquivo_saida}'")
    print(f"   Local: {caminho_saida_final}")

except FileNotFoundError:
    print(f"❌ Erro: Arquivo não encontrado. Verifique se o caminho está 100% correto:\n{caminho_entrada}")
except KeyError:
    print(f"❌ Erro: A coluna '{nome_da_coluna_para_ordenar}' não foi encontrada. Verifique se o nome na planilha mudou.")
except Exception as e:
    print(f"❌ Ocorreu um erro inesperado: {e}")