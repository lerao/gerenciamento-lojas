import sqlite3

class SQLiteConnection:
  def __init__(self, db_name):
    self.db_name = db_name
    self.connection = None

  def connect(self):
    try:
        self.connection = sqlite3.connect(self.db_name)
        print("Conexão com o banco de dados estabelecida.")
    except sqlite3.Error as error:
        print("Erro ao conectar ao banco de dados:", error)

  def close(self):
    if self.connection:
        self.connection.close()
        print("Conexão com o banco de dados fechada.")

  def execute_query(self, query, parameters=None):
    cursor = self.connection.cursor()
    try:
        if parameters:
          cursor.execute(query, parameters)
        else:
          cursor.execute(query)
        self.connection.commit()
        print("Query executada com sucesso.")
        return cursor.fetchall()
    except sqlite3.Error as error:
        print("Erro ao executar a query:", error)
        return None

  def create_database(self):
    query = '''
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    '''
    self.execute_query(query)
    print("Banco de dados e tabela criados com sucesso.")
