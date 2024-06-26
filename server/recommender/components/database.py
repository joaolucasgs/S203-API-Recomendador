import sqlite3

class Database:
    def __init__(self):
        self.db_path = "../server/db.sqlite3"  # O caminho arquivo sqlite deve ser relativo ao terminal venv

    def query(self, query):
        connect = sqlite3.connect(self.db_path)
        try:
            cur = connect.cursor()
            result = cur.execute(query)
            return result.fetchall()
        except Exception as e:
            return print(e)
        finally:
            connect.close()
