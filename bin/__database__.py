from sqlcipher3 import dbapi2 as sqlite3
def interactDB(key):
    conn = sqlite3.connect("bin/database.db")
    cursor = conn.cursor()
    try:
        cursor.execute(f"PRAGMA key='{key}';")
        conn.commit()
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
def insertData(query, key):
    conn = sqlite3.connect("bin/database.db")
    c = conn.cursor()
    c.execute(f"PRAGMA key='{key}';")
    conn.commit()
    c.execute(query)
    conn.commit()
    conn.close()

        #FETCH DATA
def fetchData(query, key):
    try:
        conn = sqlite3.connect("bin/database.db")
        c = conn.cursor()
        c.execute(f"PRAGMA key='{key}';")
        conn.commit()
        c.execute(query)
        return c.fetchall()
    except:
        return []

def insertUser(query, key):
    try:
        conn = sqlite3.connect("bin/database.db")
        c = conn.cursor()
        c.execute(f"PRAGMA key='{key}';")
        conn.commit()
        c.execute(query)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)