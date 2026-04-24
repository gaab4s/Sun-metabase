import requests
import pandas as pd
from sqlalchemy import create_engine
import os

# Configurações do Banco de Dados AWS RDS
# Dica: Substitua pelos seus dados ou use variáveis de ambiente
DB_USER = 'user'
DB_PASS = 'senha'
DB_HOST = 'banco.us-east-1.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'postgres'

def extrair_dados():
    print("Buscando dados da API...")
    # Nesse campo será adicionada a api.
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    response = requests.get(url)
    return response.json()

def carregar_dados(dados):
    print("Carregando dados no RDS da AWS...")
    df = pd.DataFrame(dados)
    
    # Criando a conexão com o PostgreSQL
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    
    # Salva no banco (substitui a tabela se já existir)
    df.to_sql('dashboard_apis', engine, if_exists='replace', index=False)
    print("Sucesso!")

if __name__ == "__main__":
    dados = extrair_dados()
    carregar_dados(dados)
