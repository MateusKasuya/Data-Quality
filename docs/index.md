# Documentação Data Quality

## Fluxo

Para desenvolver o desafio de negócio, vamos montar a seguinte ETL:
```mermaid
graph TD;
    A[Configura Variáveis] --> B[Ler o Banco SQL];
    B --> V[Validação do Schema de Entrada];
    V -->|Falha| X[Alerta de Erro];
    V -->|Sucesso| C[Transformar os KPIs];
    C --> Y[Validação do Schema de Saída];
    Y -->|Falha| Z[Alerta de Erro];
    Y -->|Sucesso| D[Salvar no DuckDB];
```

# Contrato de Dados

::: app.schema.ProdutoSchema

# Transformacoes

## Configurar Variáveis
::: app.etl.load_settings

## Ler o Banco SQL
::: app.etl.extrair_do_sql

## Transformar os KPIs
::: app.etl.transformar

## Salvar no Duckdb
::: app.etl.load_to_duckdb
