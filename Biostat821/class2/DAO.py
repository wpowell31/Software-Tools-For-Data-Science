"""Create Dao data access object."""
import sqlite3


class DinosaurDao:
    def __init__(self, filename: str):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "DROP TABLE IF EXISTS dinos"
        )
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS dinos(name VARCHAR PRIMARY KEY, species VARCHAR)"
        )

    def add(self, name: str, species: str):
        self.cursor.execute(
            "INSERT INTO dinos VALUES(?, ?)", (name, species)
        )

    def get(self, name: str):
        c = self.cursor.execute("SELECT * FROM dinos WHERE name=?", (name,))
        dino = c.fetchall()
        return dino

    def list(self):
        c = self.cursor.execute("SELECT * FROM dinos")
        data = c.fetchall()
        return data

test = DinosaurDao("test.db")
test.add("Will", "T-Rex")
print(test.list())