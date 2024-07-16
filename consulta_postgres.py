import psycopg2

class Column:
    def __init__(self, name, is_nullable, the_type):
        self.name = name
        self.is_nullable = is_nullable
        self.the_type = the_type
    
    def __repr__(self):
        return f"{self.name}|{self.the_type}|{self.is_nullable}"

def obter_informacoes_tabela(postgres):
    # Configurações de conexão
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='localhost', 
        port='15432'  
    )

    # Criar um cursor
    cur = conn.cursor()

    # Executar a consulta
    cur.execute("""
        SELECT column_name, is_nullable, data_type
        FROM information_schema.columns
        WHERE table_name = 'nome_da_tabela';
    """)

    informacoes = cur.fetchall()
    # Fechar o cursor e a conexão
    cur.close()
    conn.close()
    
    return {col: Column(col, is_nullable, the_type) for col, is_nullable, the_type in informacoes}
    
    
