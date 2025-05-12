import pandas as pd
import unicodedata

def normalizar_texto(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

def ler_cnpjs(caminho_arquivo):
    print(f"[DEBUG] Lendo planilha: {caminho_arquivo}")

    try:
        df = pd.read_excel(caminho_arquivo)
        print(f"[DEBUG] Colunas encontradas: {df.columns.tolist()}")

        coluna_cnpj = None
        for col in df.columns:
            if "cnpj" in normalizar_texto(col):
                coluna_cnpj = col
                break
        if not coluna_cnpj:
            raise ValueError("Coluna contendo 'CNPJ' não foi encontrada.")

        coluna_codigo = None
        for col in df.columns:
            if "codigo" in normalizar_texto(col):
                coluna_codigo = col
                break
        if not coluna_codigo:
            raise ValueError("Coluna contendo 'Código' não foi encontrada.")

        print(f"[DEBUG] Coluna identificada como CNPJ: '{coluna_cnpj}'")
        print(f"[DEBUG] Coluna identificada como Código: '{coluna_codigo}'")

        # Limpa e normaliza os dados
        df[coluna_cnpj] = df[coluna_cnpj].astype(str).str.replace(r'\D', '', regex=True).str.zfill(14)
        df[coluna_codigo] = df[coluna_codigo].astype(str)

        df_filtrado = df[[coluna_codigo, coluna_cnpj]].dropna()
        df_filtrado.columns = ['Código', 'CNPJ']  # Renomeia colunas para padrão fixo

        lista = df_filtrado.to_dict(orient="records")
        print(f"[DEBUG] Total de pares Código+CNPJ extraídos: {len(lista)}")
        return lista

    except Exception as e:
        print(f"[DEBUG][ERRO] Erro ao ler planilha: {str(e)}")
        raise e
