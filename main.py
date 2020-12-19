from bin.__database__ import *
from bin.__user__ import *
import json

# Let's Start this Application

# Start Up.....
conn = connectDB()
intializeTable(conn)

# Creating User if not Exist
profile = createUser(len(fetchData(conn, "SELECT * FROM user;")))
if profile != None:
    print(changeData(
        conn, 
        "Create", 
        f"INSERT INTO user VALUES(null, '{profile['username']}', '{profile['password']}');"
    ))
    print(changeData(
        conn,
        "Create",
        f"INSERT INTO login (login_uid, user_login, user_password) SELECT user.uid, user.username, user.password FROM user WHERE uid = 1 LIMIT 1;"
    ))
    print(changeData(
        conn,
        "Create",
        f"INSERT INTO recovery (recovery_uid, ques_a, ques_b, ques_c, ans_a, ans_b, ans_c) SELECT user.uid, '{profile['ques']['a']}', '{profile['ques']['b']}', '{profile['ques']['c']}', '{profile['ans']['a']}', '{profile['ans']['b']}', '{profile['ans']['c']}' FROM user WHERE uid = 1 LIMIT 1;"
    ))