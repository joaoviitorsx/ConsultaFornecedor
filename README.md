# 🧾 Consulta de Fornecedores via CNPJ

Este projeto é uma aplicação desktop simples desenvolvida em **Python com Tkinter**, que realiza a leitura de uma planilha Excel contendo CNPJs de fornecedores e consulta automaticamente seus dados na API pública [minhareceita.org](https://minhareceita.org).

## 📌 Funcionalidades

- Leitura de planilhas `.xlsx` com colunas `Código` e `CNPJ`
- Identificação automática de colunas, mesmo com nomes como `CÓDIGO`, `cnpj fornecedor`, etc
- Consulta dos dados via API pública
- Geração de nova planilha com:
  - Código
  - CNPJ
  - Razão Social
  - Simples Nacional
  - Decreto
- Interface simples e amigável em Tkinter
- Barra de progresso durante a execução


