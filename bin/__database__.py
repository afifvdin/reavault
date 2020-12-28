from pysqlcipher3 import dbapi2 as sqlite3
# import json
def connectDB():
    # Connect Database Application With Location Given
    # Should return like conn = sqlite3.connect()
    return sqlite3.connect('bin/database.db')

def intializeTable(connection):
    # Intializing Table Which is exist or not
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE user (
                uid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username varchar(255),
                password varchar(255)
            );
        ''')
        cursor.execute('''
            CREATE TABLE login (
                login_uid INTEGER,
                user_login varchar(255),
                user_password varchar(255),
                FOREIGN KEY (login_uid) REFERENCES user(uid)
            );
        ''')
        cursor.execute('''
            CREATE TABLE recovery (
                recovery_uid INTEGER,
                ques_a varchar(255),
                ques_b varchar(255),
                ques_c varchar(255),
                ans_a varchar(255),
                ans_b varchar(255),
                ans_c varchar(255),
                FOREIGN KEY (recovery_uid) REFERENCES user(uid)
            );
        ''')
        cursor.execute('''
            CREATE TABLE categories (
                category_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                category_name varchar(255)
            );
        ''')
        cursor.execute('''
            CREATE TABLE tags (
                tag_id INTEGER NOT NULL,
                tag_name varchar(255)
            );
        ''')
        cursor.execute('''
            CREATE TABLE types (
                type_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                type_value INTEGER
            );
        ''')
        cursor.execute('''
            CREATE TABLE colors (
                color_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                color_code varchar(7)
            );
        ''')
        cursor.execute('''
            CREATE TABLE password_vault (
                vault_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title varchar(255),
                description varchar(255),
                target varchar(255),
                enc_username varchar(255),
                enc_password varchar(255),
                vault_category_id INTEGER,
                vault_tag_id INTEGER,
                vault_type_id INTEGER,
                vault_color_id INTEGER,
                FOREIGN KEY (vault_category_id) REFERENCES categories(category_id),
                FOREIGN KEY (vault_tag_id) REFERENCES tags(tag_id),
                FOREIGN KEY (vault_type_id) REFERENCES types(type_id),
                FOREIGN KEY (vault_color_id) REFERENCES colors(color_id)
            );
        ''')
        # connection.commit()
    except Exception as e:
        print(e)

def fetchData(connection, query="SELECT * FROM password_vault;"):
    # Fetching Data and return it to variable
    cursor = connection.cursor()
    cursor.execute(query)
    # connection.commit()
    return cursor.fetchall()

def changeData(connection, method, query):
    # Changing data Insert, Update, Delete
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        # connection.commit()
        return f"{method} Successfull"
    except Exception as e:
        return e
        return f"{method} Not Succesfull"