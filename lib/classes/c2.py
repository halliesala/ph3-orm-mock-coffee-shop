from lib import CONN, CURSOR

class C2:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"C2(id={self.id}, name={self.name})"

    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS c2s (
        id INTEGER PRIMARY KEY,
        name TEXT
        )
        """

        CURSOR.execute(sql)
