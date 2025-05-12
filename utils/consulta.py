import requests

def consultar_cnpj(cnpj):
    print(f"[DEBUG] Iniciando consulta para CNPJ: {cnpj}")

    url = f"https://minhareceita.org/{cnpj}"
    try:
        response = requests.get(url, timeout=10)
        print(f"[DEBUG] Status da resposta: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            resultado = {
                'CNPJ': cnpj,
                'Razão Social': data.get('razao_social', ''),
                'CNAE': data.get('cnae_fiscal', ''),
                'Simples Nacional': 'Sim' if data.get('opcao_pelo_simples') else 'Não',
                'Decreto': 'Sim' if data.get('opcao_pelo_mei') else 'Não'
            }
            print(f"[DEBUG] Consulta bem-sucedida: {resultado}")
            return resultado
        else:
            erro = {'CNPJ': cnpj, 'Erro': f"Erro {response.status_code}"}
            print(f"[DEBUG] Erro na resposta da API: {erro}")
            return erro

    except Exception as e:
        erro = {'CNPJ': cnpj, 'Erro': f"Erro de conexão: {str(e)}"}
        print(f"[DEBUG][ERRO] Exceção durante a consulta: {erro}")
        return erro
