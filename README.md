# Integração de APIs de Software com Metabase na AWS

Este projeto de faculdade demonstra um pipeline de dados completo: extração de dados via APIs de software, armazenamento em um banco de dados relacional na nuvem (AWS RDS) e visualização de indicadores em um dashboard profissional usando Metabase.

## 📋 Arquitetura do Projeto

A solução foi desenhada utilizando os seguintes componentes:

1.  **Extração (Python):** Script responsável por consumir as APIs, realizar o tratamento inicial dos dados (ETL) e enviá-los para a nuvem.
2.  **Armazenamento (AWS RDS):** Instância gerenciada de PostgreSQL na AWS onde os dados das APIs são centralizados.
3.  **Visualização (Metabase):** Plataforma de Business Intelligence hospedada em uma instância AWS EC2 para consulta e criação de gráficos.
4.  **Infraestrutura (Docker):** Utilização de containers para garantir que o Metabase rode de forma isolada e segura.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:** Pandas, SQLAlchemy, Requests
* **Cloud:** Amazon Web Services (RDS para banco de dados e EC2 para o servidor)
* **Containerização:** Docker & Docker Compose
* **BI:** Metabase

## 📂 Estrutura de Arquivos

* `main.py`: Script Python que realiza a coleta dos dados da API.
* `docker-compose.yml`: Arquivo de configuração para subir o Metabase na AWS.
* `requirements.txt`: Lista de dependências Python necessárias.
* `.gitignore`: Arquivo para garantir a segurança das credenciais de acesso.

## 🚀 Como Executar o Projeto

### 1. Configuração do Banco (AWS RDS)
* Crie uma instância PostgreSQL no AWS RDS.
* Certifique-se de que o Security Group permite acesso na porta 5432.

### 2. Execução do Script de Extração
Instale as dependências e rode o script principal:
```bash
pip install -r requirements.txt
python main.py
