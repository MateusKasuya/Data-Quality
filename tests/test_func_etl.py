import pandas as pd
from pandera import DataFrameSchema, Column, Check

from app.etl import transformar



def test_calculo_valor_total_estoque():
    # Preparação
    df = pd.DataFrame({
        'id_produto' : [1,2],
        'nome' : ['carrinho', 'notebook'],     
        'quantidade': [20, 25],
        'preco': [20.0, 100.0],
        'categoria': ['brinquedos', 'eletrônicos'],
        'email' : ['mateusvbkasuya@gmail.com', 'mateuskasuya@hotmail.com']
    })
    expected = pd.Series([400.0, 2500.0], name='valor_total_estoque')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['valor_total_estoque'], expected)

def test_normalizacao_categoria():
    # Preparação
    df = pd.DataFrame({
        'id_produto' : [1,2],
        'nome' : ['carrinho', 'notebook'],  
        'quantidade': [114, 28],
        'preco': [20.0, 30.0],
        'categoria': ['brinquedos', 'eletrônicos'],
        'email' : ['mateusvbkasuya@gmail.com', 'mateuskasuya@hotmail.com']
    })
    expected = pd.Series(['BRINQUEDOS', 'ELETRÔNICOS'], name='categoria_normalizada')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['categoria_normalizada'], expected)

def test_determinacao_disponibilidade():
    # Preparação
    df = pd.DataFrame({
        'id_produto' : [1,2],
        'nome' : ['carrinho', 'notebook'],
        'quantidade': [100, 25],
        'preco': [20.0, 30.0],
        'categoria': ['brinquedos', 'eletrônicos'],
        'email' : ['mateusvbkasuya@gmail.com', 'mateuskasuya@hotmail.com']
    })
    expected = pd.Series([True, True], name='disponibilidade')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['disponibilidade'], expected)

# Para rodar os testes, execute `poetry run task test` no terminal.