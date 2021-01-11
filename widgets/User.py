from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import json
import sys

class User(QWidget):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.parentLayout = QHBoxLayout()
        self.changeTheme()

        self.parentLayout.setSpacing(0)
        self.parentLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.parentLayout)
        
        self.setFixedHeight(250)
        self.setFixedWidth(600)
        self.setWindowTitle("reavault")

    def changeTheme(self, isChange=False):
        res = None
        with open('configuration/conf.json', 'r') as f:
            res = json.loads(f.read())
        if isChange == True:
            if res['theme'] == 'light':
                res['theme'] = 'dark'
            else:
                res['theme'] = 'light'
        if res['theme'] == 'light':
            self.primaryBg      = "#F5F5F5"
            self.secondBg       = "#FFFFFF"
            self.primaryFg      = "#000000"
            self.secondFg       = "#C8C8C8"
            self.btnPrimaryBg   = "#AAAAAA"
            self.activeBg       = "#315BEF"
            self.alternativeBg  = "#2D56DC"
            self.complementBg   = "#242424"
            self.logoLocation   = "resources/reavaultLight.png"
            self.iconLocation   = "resources/darkToggle.png"
            self.registerIconDir = "resources/registerDark.png"
            self.infoIconDir    = "resources/infoDark.png"
        else:
            self.primaryBg      = "#242424"
            self.secondBg       = "#2E2E2E"
            self.primaryFg      = "#FFFFFF"
            self.secondFg       = "#323232"
            self.btnPrimaryBg   = "#505050"
            self.activeBg       = "#315BEF"       
            self.alternativeBg  = "#2D56DC"
            self.complementBg   = "#FFFFFF"
            self.logoLocation   = "resources/reavaultDark.png"
            self.iconLocation   = "resources/lightToggle.png"
            self.registerIconDir = "resources/registerLight.png"
            self.infoIconDir    = "resources/infoLight.png"
        with open('configuration/conf.json', 'w') as f:
            json.dump(res, f)

        ################################################
        self.setStyleSheet(f"background-color: {self.primaryBg};")
        for i in reversed(range(self.parentLayout.count())):
            self.parentLayout.removeItem(self.parentLayout.itemAt(i))
        self.leftSide()
        self.rightSide()
        self.uiTheme()
        ################################################

    def leftSide(self):
        leftWidget = QWidget()
        leftWidgetLayout = QVBoxLayout()

        logo = QLabel()
        logo.setPixmap(QtGui.QPixmap(self.logoLocation))
        logo.setFixedHeight(220)
        logo.setFixedWidth(220)
        logo.setScaledContents(True)

        info = QLabel("By Three Horseman")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(info.sizePolicy().hasHeightForWidth())
        info.setSizePolicy(sizePolicy)
        info.setAlignment(QtCore.Qt.AlignCenter)

        leftWidgetLayout.addWidget(logo)
        leftWidgetLayout.addWidget(info)

        leftWidget.setLayout(leftWidgetLayout)
        leftWidget.setStyleSheet(f"background-color: {self.primaryBg};\ncolor: {self.primaryFg};")

        self.parentLayout.addWidget(leftWidget)

    def rightSide(self):
        self.userWidget = QStackedWidget()
        self.loginWidget = QWidget()
        self.registerWidget = QWidget()

        self.loginUI()
        self.registerUI()

        self.userWidget.addWidget(self.loginWidget)
        self.userWidget.addWidget(self.registerWidget)

        self.userWidget.setStyleSheet(f"background-color: {self.secondBg};")

        self.parentLayout.addWidget(self.userWidget)

    def uiTheme(self):
        themeWidget = QWidget()
        layout = QVBoxLayout()
        btn = QPushButton()
        btn.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum))
        btn.setIcon(QtGui.QIcon(self.iconLocation))
        infoBtn = QPushButton()
        infoBtn.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum))
        infoBtn.setIcon(QtGui.QIcon(self.infoIconDir))
        vSpacer = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn.clicked.connect(lambda: self.changeTheme(True))
        btn.setStyleSheet(
            "QPushButton{\n"
            f"  background-color: {self.btnPrimaryBg};\n"
            f"  color: {self.primaryFg};"
            "   border-radius: 10px;\n"
            "   padding: 5px 5px 5px;\n"
            "   margin: 5px 5px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.activeBg};\n"
            "}"
        )
        infoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        infoBtn.clicked.connect(self.showCredit)
        infoBtn.setStyleSheet(
            "QPushButton{\n"
            f"  background-color: {self.btnPrimaryBg};\n"
            f"  color: {self.primaryFg};"
            "   border-radius: 10px;\n"
            "   padding: 5px 5px 5px;\n"
            "   margin: 5px 5px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.activeBg};\n"
            "}"
        )

        layout.addWidget(btn)
        layout.addItem(vSpacer)
        layout.addWidget(infoBtn)

        themeWidget.setStyleSheet(
            f"background-color: {self.secondBg};"
        )

        themeWidget.setLayout(layout)
        self.parentLayout.addWidget(themeWidget)

    def loginUI(self):
        parentLayout = QGridLayout()
        layout = QFormLayout()

        userField = QLineEdit()
        passwordField = QLineEdit()
        loginBtn = QPushButton("Login")
        dontHave = QLabel("Don't have one yet?")
        registerBtn = QPushButton("Sign Up")
        vInnerSpacer = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        userField.setStyleSheet(
            "QLineEdit {\n"
            f"  border: 2px solid {self.btnPrimaryBg};\n"
            "   border-radius: 4px;\n"
            "   padding: 2px;\n"
            "}\n"
            "QLineEdit::focus {\n"
            f"  border: 2px solid {self.activeBg};\n"
            "}"
        )
        passwordField.setStyleSheet(
            "QLineEdit {\n"
            f"  border: 2px solid {self.btnPrimaryBg};\n"
            "   border-radius: 4px;\n"
            "   padding: 2px;\n"
            "}\n"
            "QLineEdit::focus {\n"
            f"  border: 2px solid {self.activeBg};\n"
            "}"
        )
        loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        iconLogin = QtGui.QIcon()
        iconLogin.addPixmap(QtGui.QPixmap("resources/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginBtn.setIcon(iconLogin)
        loginBtn.setStyleSheet(
            "QPushButton{\n"
            f"  background-color: {self.activeBg};\n"
            "   color: #FFFFFF;"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.alternativeBg};\n"
            "}"
        )
        registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        iconRegister = QtGui.QIcon()
        iconRegister.addPixmap(QtGui.QPixmap(self.registerIconDir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        registerBtn.setIcon(iconRegister)
        registerBtn.setStyleSheet(
            "QPushButton{\n"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.btnPrimaryBg};\n"
            "}"
        )

        dontHave.setAlignment(QtCore.Qt.AlignCenter)
        loginBtn.clicked.connect(lambda: self.verifyUser(userField.text(), passwordField.text()))
        registerBtn.clicked.connect(lambda: self.userWidget.setCurrentIndex(1))

        hSpacer = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        vSpacer = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        layout.addRow(QLabel("Username\t"), userField)
        layout.addRow(QLabel("Password\t"), passwordField)
        layout.addWidget(loginBtn)
        layout.addItem(vInnerSpacer)
        layout.addWidget(line)
        layout.addWidget(dontHave)
        layout.addWidget(registerBtn)

        parentLayout.addItem(vSpacer, 0, 1)
        parentLayout.addItem(vSpacer, 1, 1)
        parentLayout.addLayout(layout, 2, 1)
        parentLayout.addItem(vSpacer, 3, 1)
        parentLayout.addItem(hSpacer, 2, 2)

        self.loginWidget.setLayout(parentLayout)

        ############################
        self.loginWidget.setStyleSheet(
            f"color: {self.complementBg};\n"
            f"background-color: {self.secondBg};"
        )

    def registerUI(self):
        parentLayout = QGridLayout()

        ############################
        layout = QFormLayout()
        userField = QLineEdit()
        passwordField = QLineEdit()
        repwdField = QLineEdit()
        registerBtn = QPushButton("Sign Up")
        backBtn = QPushButton("Back")
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        userField.setStyleSheet(
            "QLineEdit {\n"
            f"  border: 2px solid {self.btnPrimaryBg};\n"
            "   border-radius: 4px;\n"
            "   padding: 2px;\n"
            "}\n"
            "QLineEdit::focus {\n"
            f"  border: 2px solid {self.activeBg};\n"
            "}"
        )
        passwordField.setStyleSheet(
            "QLineEdit {\n"
            f"  border: 2px solid {self.btnPrimaryBg};\n"
            "   border-radius: 4px;\n"
            "   padding: 2px;\n"
            "}\n"
            "QLineEdit::focus {\n"
            f"  border: 2px solid {self.activeBg};\n"
            "}"
        )
        repwdField.setStyleSheet(
            "QLineEdit {\n"
            f"  border: 2px solid {self.btnPrimaryBg};\n"
            "   border-radius: 4px;\n"
            "   padding: 2px;\n"
            "}\n"
            "QLineEdit::focus {\n"
            f"  border: 2px solid {self.activeBg};\n"
            "}"
        )
        registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        iconRegister = QtGui.QIcon()
        iconRegister.addPixmap(QtGui.QPixmap("resources/registerLight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        registerBtn.setIcon(iconRegister)
        registerBtn.setStyleSheet(
            "QPushButton{\n"
            f"  background-color: {self.activeBg};\n"
            "   color: #FFFFFF;"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.alternativeBg};\n"
            "}"
        )
        backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        iconBack = QtGui.QIcon()
        iconBack.addPixmap(QtGui.QPixmap("resources/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        backBtn.setIcon(iconBack)
        backBtn.setStyleSheet(
            "QPushButton{\n"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.btnPrimaryBg};\n"
            "}"
        )

        backBtn.clicked.connect(lambda: self.userWidget.setCurrentIndex(0))
        registerBtn.clicked.connect(lambda: self.verifyUser(userField.text(), passwordField.text(), repwdField.text()))

        layout.addRow(QLabel("Username "), userField)
        layout.addRow(QLabel("Password "), passwordField)
        layout.addRow(QLabel("Retype Password "), repwdField)
        layout.addWidget(registerBtn)
        layout.addWidget(line)
        layout.addWidget(backBtn)
        ############################

        hSpacer = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        vSpacer = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        parentLayout.addItem(vSpacer, 0, 1)
        parentLayout.addItem(vSpacer, 2, 1)
        parentLayout.addLayout(layout, 1, 0)

        self.registerWidget.setLayout(parentLayout)

        ############################
        self.registerWidget.setStyleSheet(
            f"background-color: {self.secondBg};\n"
            f"color: {self.complementBg};"
        )

    def showCredit(self):
        self.child = []

        msg = QDialog()
        msg.setStyleSheet(f"background-color: {self.secondBg};\ncolor: {self.complementBg};")
        msg.setFixedHeight(400)
        msg.setFixedWidth(300)

        icon = QLabel()
        icon.setPixmap(QtGui.QPixmap(self.logoLocation))
        icon.setFixedHeight(220)
        icon.setFixedWidth(220)
        icon.setScaledContents(True)

        title = QLabel("Reavault")
        title.setStyleSheet("font-size: 24px;\nfont-style: bold;\ntext-align: center;")

        desc = QLabel("https://github.com/afifvdin/reavault\nReleased under GNU/GPL Version 3")
        desc.setStyleSheet("text-align: center;")

        changelog = QLabel(
            "Changelog v0.0.1:\n"
            "+ CRUD Feature"
        )

        layout = QGridLayout()
        layout.addWidget(icon, 0, 1, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(changelog, 1, 1, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(title, 2, 1, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(desc, 3, 1, 1, 1, QtCore.Qt.AlignCenter)

        msg.setLayout(layout)
        msg.setWindowTitle("About - reavault")
        self.child.append(msg)
        msg.show()


    def setNextPoint(self, Storage):
        self.Storage = Storage

    def databaseFunction(self, x):
        self.db = x
        self.db.interactDB()
    
    def raiseError(self, information):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText(information)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def verifyUser(self, uname, pwd, repwd=None):
        if uname.isspace() == True or uname == '' or pwd.isspace() == True or pwd == '' or (repwd != None and repwd != pwd):
            self.raiseError("Username or Password not correct!")
            return
        if repwd == None:
            res = self.db.fetchData(f"SELECT * FROM Users WHERE username = '{uname}' and password = '{pwd}';")
            if len(res) > 0:
                self.Storage.changeTheme()
                self.Storage.show()
                self.close()
            else:
                self.raiseError("Username or Password Not Found!")
            return
        req = self.db.insertData(f"INSERT INTO Users VALUES(null, '{uname}', '{pwd}');")
        self.userWidget.setCurrentIndex(0)
        return
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = User()
    win.show()
    sys.exit(app.exec_())