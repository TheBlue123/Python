import requests
import json

# 1. Mensagem para confirmar que o script iniciou
print("Iniciando a busca pela cotação do dólar...")

url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

try:
    # 2. Faz a requisição para a API
    resposta = requests.get(url, timeout=10) # Adicionado um timeout de 10 segundos

    # 3. Verifica se a requisição foi bem-sucedida (código 200)
    resposta.raise_for_status() 

    # 4. Transforma a resposta JSON em dicionário
    dados = resposta.json()
    print("Dados recebidos da API:", dados) # Imprime os dados para vermos a estrutura

    # 5. Acessa o valor atual do dólar com segurança
    cotacao_dolar = dados['USDBRL']['bid']

    # 6. Imprime o resultado final
    print(f'✅ Cotação do dólar agora: R$ {cotacao_dolar}')

except requests.exceptions.RequestException as e:
    print(f"❌ Erro de conexão ou na requisição: {e}")
except KeyError:
    print("❌ Erro: A estrutura do JSON recebido mudou. Não foi possível encontrar a chave 'USDBRL' ou 'bid'.")
except Exception as e:
    print(f"❌ Ocorreu um erro inesperado: {e}")

finally:
    print("Script finalizado.")