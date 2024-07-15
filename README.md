# CSV para SQL Inserção

Este projeto tem como objetivo converter dados de um arquivo CSV para comandos SQL de inserção em uma tabela do PostgreSQL. Ele obtém informações sobre a estrutura da tabela a partir do banco de dados e usa essas informações para formatar os valores corretamente.

## Estrutura do Projeto

```sh
.
├── consulta_postgres.py
├── csv_para_sql.py
├── README.md
└── requirements.txt
```


- `consulta_postgres.py`: Contém a função `obter_informacoes_tabela` para obter informações sobre a tabela do PostgreSQL.
- `csv_para_sql.py`: Contém a função `csv_para_sql` que converte os dados do CSV em comandos SQL de inserção.
- `README.md`: Este arquivo.
- `requirements.txt`: Lista de dependências do projeto.

## Pré-requisitos

- Python 3.6 ou superior
- PostgreSQL
- Pandas
- Psycopg2

## Instalação

1. Clone o repositório para sua máquina local;

2. Instale as dependências listadas no `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

## Configuração

### Banco de Dados PostgreSQL

Certifique-se de ter um banco de dados PostgreSQL em execução e configure as credenciais de acesso no script `consulta_postgres.py`. 

Substitua dbname, user, password, host e port pelos valores apropriados para seu ambiente.

## Uso

### Executando o Script

1. Prepare o arquivo CSV que deseja converter para comandos SQL de inserção;

2. Modifique csv_para_sql.py para apontar para o caminho correto do CSV e o nome da tabela no arquivo script.py:
    caminho_csv = 'caminho_da_tabela'
    nome_tabela = 'nome_da_tabela'
    comando_sql = csv_para_sql(caminho_csv, nome_tabela)
    print(comando_sql)

3. NO arquivo consulta_postgres, mude somente o nome da tabela:
    ```sh
    cur.execute("""
        SELECT column_name, is_nullable, data_type
        FROM information_schema.columns
        WHERE table_name = 'nome_da_tabela';
    """)

3. Execute o script:

```sh
    python csv_para_sql.py
```

O script irá ler o arquivo CSV, obter as informações da tabela no banco de dados, e gerar comandos SQL de inserção que serão impressos no console.