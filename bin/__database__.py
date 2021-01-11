from pysqlcipher3 import dbapi2 as sqlite3
def interactDB():
    conn = sqlite3.connect("bin/database.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username varchar(255),
                password varchar(255)
            );
        ''')
        conn.commit()
        cursor.execute('''
            CREATE TABLE Vaults (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title varchar(255),
                username varchar(255),
                password varchar(255)
            );
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        conn.close()

        #INSERT DATA
def insertData(query):
    conn = sqlite3.connect("bin/database.db")
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

        #FETCH DATA
def fetchData(query):
    conn = sqlite3.connect("bin/database.db")
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()