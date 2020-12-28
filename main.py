import sys
from PyQt5.QtWidgets import *
from bin.__database__ import *
import json

########## CHECKING THEME

try:
    with open('configuration/configuration.json', 'r') as f:
        a = json.loads(f.read())
        if a['application.theme'] == 'lighto':
            from layouts.light import light, login, signup
        else:
            from layouts.dark import mainApp, login, signup
except:
    from layouts.dark import mainApp, login, signup
        

######### BUILDING CLASS

class Reavault:
    def __init__(self):
        self.setup()

    def setup(self):
        self.conn = connectDB()
        intializeTable(self.conn)

    def userStatus(self):
        c = fetchData(self.conn, "SELECT * FROM user;")        
        return len(c)

    def createUser(self, data):
        # query = f"PRAGMA key='{data['password']}';"
        # print(changeData(self.conn, "Securing", query))

        query = f"INSERT INTO user VALUES(null, '{data['username']}', '{data['password']}');"
        changeData(self.conn, "Create", query)
        
        query = (
            "INSERT INTO login (login_uid, user_login, user_password)" 
            f"SELECT user.uid, user.username, user.password FROM user WHERE user.uid = 1;"
            )
        changeData(self.conn, "Create", query)

        query = (
            "INSERT INTO recovery "
            "(recovery_uid, ques_a, ques_b, ques_c, ans_a, ans_b, ans_c) "
            f"SELECT user.uid, '{data['ques']['a']}', '{data['ques']['b']}', '{data['ques']['c']}', "
            f"'{data['ans']['a']}', '{data['ans']['b']}', '{data['ans']['c']}' FROM user WHERE user.uid = 1;"
        )
        changeData(self.conn, "Create", query)
        self.conn.commit()

    def loginUser(self, data):
        query = f"SELECT * FROM user;"
        res = fetchData(self.conn, query)
        for i in res:
            if i[1] != data[0] or i[2] != data[1]:
                return False
        return True

    def getAllData(self):
        query = f"SELECT * FROM password_vault;"
        res = fetchData(self.conn, query)
        return res

    def getAttribute(self, query):
        res = fetchData(self.conn, query)
        return res

    def insertData(self, query):
        changeData(self.conn, "Create", query)


########## EXAMPLE IF NO USER FOUND

reavault = Reavault()
# if reavault.userStatus() == 0:
if True:
    app = QApplication(sys.argv)

    storageParent = QWidget()
    storage = mainApp.Ui_storageDark()
    storage.setBridge(reavault)
    storage.setupUi(storageParent)

    Login = QWidget()
    Loginui = login.Ui_LoginRecovery()
    Loginui.setupUi(Login)
    Loginui.setter(Login, storageParent)
    Loginui.setBridge(reavault)

    SignUp = QWidget()
    SignUpui = signup.Ui_Form()
    SignUpui.setupUi(SignUp)
    SignUpui.setter(SignUp, Login)
    SignUpui.setBridge(reavault)

    SignUp.show()

    sys.exit(app.exec_())

# [(), (2, '222')]