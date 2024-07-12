import pandas as pd
from consulta_postgres import obter_informacoes_tabela  # Importando a função

def tratar_valor(val, definition):
    if pd.isna(val) and definition.is_nullable == "YES":
        return "NULL"

    tipo = definition.the_type
    if tipo in ["character varying", "text"]:
        return tratar_texto(val)
    elif tipo == "integer":
        return tratar_inteiro(val)
    elif tipo == "boolean":
        return tratar_booleano(val)
    else:
        return str(val)

def tratar_texto(val):
    if pd.isna(val):
        return "'NULL'"
    return f"'{val}'"

def tratar_inteiro(val):
    if pd.isna(val):
        return "0"
    return str(int(val))

def tratar_booleano(val):
    return "TRUE" if val else "FALSE"

def csv_para_sql(caminho_csv, nome_tabela):
    # Lê o arquivo CSV e carrega os dados em um DataFrame do pandas
    data = pd.read_csv(caminho_csv)
    
    # Obter informações da tabela
    definitions = obter_informacoes_tabela(nome_tabela)
    
    # Cria a estrutura do comando SQL
    sql_insert = f"INSERT INTO {nome_tabela} ({', '.join(data.columns)}) VALUES\n"
    
    # Iterar sobre cada linha do DataFrame e criar os valores para o comando SQL
    valores = []
    for _, row in data.iterrows():
        valor = [tratar_valor(row[col], definitions[col]) for col in data.columns]
        valores.append(f"({', '.join(valor)})")
    
    sql_insert += ",\n".join(valores) + ";"
    
    return sql_insert

# Exemplo de uso
if __name__ == "__main__":
    caminho_csv = 'caminho_para_tabela
    nome_tabela = 'nome_tabela'
    comando_sql = csv_para_sql(caminho_csv, nome_tabela)
    print(comando_sql)
