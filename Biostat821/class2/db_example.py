import sqlite3


def main():
    """Do things."""
    connection = sqlite3.connect("test_database.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE Users")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Users(name VARCHAR PRIMARY KEY, dob INTEGER, pw BLOB)"
    )
    cursor.executemany(
        "INSERT INTO Users Values(?, ?, ?)",
        [
            ("Max", 1970, "helloworld"),
            ("Jeremy", 1902, 3.14),
            ("Will", 2012, None),
        ],
    )
    connection.commit()
    c = cursor.execute("SELECT name, pw FROM Users WHERE dob>1971")
    data = c.fetchall()
    print(c)
    print(data)


if __name__ == "__main__":
    main()
