import sqlite3


class DatabaseManager:
    def __init__(self, main):
        self.conn = sqlite3.connect(main.db)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        create_table = """Create Table IF NOT EXISTS pm_schdule(
                            id INTEGER Primary Key,
                            model TEXT,
                            status Text
                        );"""
        self.cursor.execute(create_table)

    def load_data(self):
        query = "SELECT * from pm_schdule"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close(self):
        self.cursor.close()

    


