import pandas as pd
from pathlib import Path
import re
import os

# --- CONFIGURAÇÃO ---
diretorio_principal = r"C:\Users\samur\OneDrive\Documentos\VSCODE\python\Python\trabalho"

# !! MUDANÇA AQUI !! O script agora salvará em uma pasta na sua Área de Trabalho.
pasta_saida = Path.home() / "Desktop" / "Relatorios_das_Provas"

coluna_polo_padronizada = 'polo_final'
coluna_nome_padronizada = 'nome_final'
modulos = ['ING1', 'ING2', 'ING3', 'ESP1', 'ESP2', 'ESP3']
# --------------------

# --- INÍCIO DO SCRIPT ---
# O resto do script continua exatamente igual...

lista_de_dados = []
caminho_base = Path(diretorio_principal)

print("--- Passo 1 de 4: Lendo e combinando todos os arquivos... ---")
arquivos_para_ler = [f for f in caminho_base.iterdir() if f.is_file() and f.suffix == '.xlsx']

if not arquivos_para_ler:
    print(f"❌ ERRO: Nenhum arquivo .xlsx foi encontrado no diretório: {diretorio_principal}")
else:
    # (O restante do código é idêntico ao anterior)
    for caminho_arquivo in arquivos_para_ler:
        try:
            nome_do_modulo = caminho_arquivo.stem.split(' ')[0]
            if nome_do_modulo in modulos:
                df = pd.read_excel(caminho_arquivo)
                nome_polo_encontrado = None
                if 'polo' in df.columns: nome_polo_encontrado = 'polo'
                elif 'Polo' in df.columns: nome_polo_encontrado = 'Polo'
                nome_aluno_encontrado = None
                if 'nome' in df.columns: nome_aluno_encontrado = 'nome'
                elif 'Nome' in df.columns: nome_aluno_encontrado = 'Nome'
                if nome_polo_encontrado and nome_aluno_encontrado:
                    df.rename(columns={
                        nome_polo_encontrado: coluna_polo_padronizada,
                        nome_aluno_encontrado: coluna_nome_padronizada
                    }, inplace=True)
                    df['Origem_Modulo'] = nome_do_modulo
                    lista_de_dados.append(df)
                    print(f"   - Arquivo '{caminho_arquivo.name}' lido e padronizado com sucesso.")
                else:
                    if not nome_polo_encontrado: print(f"   - ⚠️ Aviso: Coluna de polo não encontrada no arquivo '{caminho_arquivo.name}'. Pulando...")
                    if not nome_aluno_encontrado: print(f"   - ⚠️ Aviso: Coluna de nome não encontrada no arquivo '{caminho_arquivo.name}'. Pulando...")
        except Exception as e:
            print(f"   - ❌ Erro ao ler o arquivo '{caminho_arquivo.name}': {e}. Pulando...")

    dados_completos = pd.concat(lista_de_dados, ignore_index=True)
    print("\n✅ Todos os arquivos foram lidos e combinados!")
    print("\n--- Passo 2 de 4: Identificando os Polos... ---")
    polos_unicos = [polo for polo in dados_completos[coluna_polo_padronizada].unique() if pd.notna(polo)]
    print(f"Polos encontrados: {len(polos_unicos)}")
    
    # Cria a pasta de resultados na Área de Trabalho
    pasta_saida.mkdir(exist_ok=True)
    print(f"Os arquivos de saída serão salvos em: {pasta_saida}")
    
    print("\n--- Passo 3 de 4: Gerando os relatórios sequenciais... ---")
    for polo in polos_unicos:
        nome_arquivo_limpo = re.sub(r'[\\/*?:"<>|]', "", str(polo))
        caminho_saida_final = pasta_saida / f"{nome_arquivo_limpo}.xlsx"
        print(f"   -> Criando relatório para o Polo: {polo}...")
        dados_do_polo = dados_completos[dados_completos[coluna_polo_padronizada] == polo]
        with pd.ExcelWriter(caminho_saida_final, engine='openpyxl') as writer:
            linha_inicial = 0
            for modulo in modulos:
                dados_para_modulo = dados_do_polo[dados_do_polo['Origem_Modulo'] == modulo]
                if not dados_para_modulo.empty:
                    df_titulo = pd.DataFrame([f"Módulo: {modulo}"])
                    df_titulo.to_excel(writer, sheet_name='Relatorio Unico', startrow=linha_inicial, index=False, header=False)
                    linha_inicial += 2
                    dados_para_modulo_ordenados = dados_para_modulo.sort_values(by=coluna_nome_padronizada)
                    colunas_para_remover = ['Origem_Modulo', coluna_polo_padronizada]
                    dados_finais = dados_para_modulo_ordenados.drop(columns=colunas_para_remover)
                    dados_finais.to_excel(writer, sheet_name='Relatorio Unico', startrow=linha_inicial, index=False)
                    linha_inicial += len(dados_finais.index) + 2
        print(f"      ✅ Relatório '{caminho_saida_final.name}' criado.")
    print("\n--- Passo 4 de 4: Processo concluído! ---")