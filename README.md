# Análise de Dados Imobiliários

Este projeto realiza uma análise de dados de imóveis disponíveis para aluguel, utilizando Python e Pandas para processamento e manipulação dos dados.

## Descrição

O projeto analisa um conjunto de dados de imóveis, incluindo informações como:
- Tipo de imóvel
- Localização (Bairro)
- Características (Quartos, Vagas, Suítes)
- Valores (Aluguel, Condomínio, IPTU)
- Área do imóvel

## Funcionalidades

O projeto inclui as seguintes funcionalidades:

1. **Análise de Dados Básica**
   - Leitura e visualização dos dados
   - Estatísticas descritivas
   - Filtragem de imóveis por características

2. **Cálculos Financeiros**
   - Cálculo do valor mensal total (Aluguel + Condomínio)
   - Cálculo do valor anual total (Valor mensal * 12 + IPTU)

3. **Processamento de Dados**
   - Criação de descrições detalhadas dos imóveis
   - Classificação binária de imóveis com suíte
   - Exportação dos dados processados

## Arquivos do Projeto

- `first.py`: Análise inicial dos dados e filtragem de apartamentos
- `second.py`: Processamento adicional dos dados e criação de novas colunas
- `dados_completos.csv`: Arquivo CSV com todos os dados processados
- `dados_apartamentos.csv`: Arquivo CSV contendo apenas dados de apartamentos

## Requisitos

- Python 3.x
- Pandas
- Matplotlib (para visualizações)

## Como Usar

1. Clone o repositório
2. Instale as dependências necessárias
3. Execute os scripts Python na seguinte ordem:
   ```bash
   python first.py
   python second.py
   ```

## Estrutura dos Dados

O conjunto de dados inclui as seguintes colunas:
- Tipo: Tipo do imóvel
- Bairro: Localização
- Quartos: Número de quartos
- Vagas: Número de vagas de garagem
- Suites: Número de suítes
- Area: Área do imóvel em m²
- Valor: Valor do aluguel
- Condominio: Valor do condomínio
- IPTU: Valor do IPTU
- Valor_por_mes: Soma do aluguel e condomínio
- Valor_por_ano: Custo anual total
- Descricao: Descrição detalhada do imóvel
- Possui_suite: Indicação se o imóvel possui suíte

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de pull requests ou reportando issues.

## Licença

Este projeto está sob a licença MIT. 