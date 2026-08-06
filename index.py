import requests

def buscar_taxas():

    url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print("Registros encontrados com sucesso!")

            dados = resposta.json()
            for registro in dados["data"][:5]:
                    print("Data:", registro["record_date"])
                    print("Taxa de câmbio:", registro["exchange_rate"])
                    print("---------------------------")
        elif resposta.status_code == 400:
             print("Requisição inválida. Verifique os parâmetros da solicitação.")
        elif resposta.status_code == 401:
                    print("Acesso não autorizado.")
        elif resposta.status_code == 403:
            print("Acesso proibido. Você não tem permissão para acessar este recurso.")
        elif resposta.status_code == 404:
                    print("Recurso não encontrado.")
        elif resposta.status_code == 500:
                    print("Erro interno do servidor. Tente novamente mais tarde.")
        elif resposta.status_code == 503:
                    print("Serviço indisponível. O servidor está temporariamente indisponível.")
        elif resposta.status_code == 429:
                    print("Limite de taxa excedido. Aguarde antes de fazer novas solicitações.")
        else:
            print(f"Erro: {resposta.status_code}")

    except requests.RequestException as erro:
        print(f"Erro de conexão: {erro}")

buscar_taxas()
