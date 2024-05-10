import sqlite3
import json

class Banco():
    
    def __init__(self):        
        self.connection = sqlite3.connect('chatbot.db')
        self.create_cursor()
        # Tire o comentário abaixo para inicializar o banco e inserir alguns dados de teste
        #self.create_and_populate_db()

    def create_cursor(self):        
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        self.connection.close()

    def create_and_populate_db(self):
        with open('chatbot.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        
        self.cursor.executescript(sql_script)
        self.connection.commit()

    def execute_query(self, sql):
        try:
            self.cursor.execute(sql)
            if self.cursor.description:  # Checa se o resultado tem descrição de colunas (típico de SELECT)
                columns = [column[0] for column in self.cursor.description]
                result = self.cursor.fetchall()
                if result:
                    # Convertendo resultados para uma lista de dicionários baseada nos nomes das colunas
                    result_list = [dict(zip(columns, row)) for row in result]
                    return json.dumps(result_list)  # Converte a lista de dicionários para JSON
                else:
                    return json.dumps({"error": "No data found."})
            else:
                # Para comandos INSERT, UPDATE, DELETE que não retornam linhas
                self.connection.commit()  # Confirma as alterações no banco
                return json.dumps({"success": "Query executed successfully.", "rows_affected": self.cursor.rowcount})
        except sqlite3.Error as e:
            return json.dumps({"error": str(e)})