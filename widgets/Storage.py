from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import json
import sys

class Storage(QMainWindow):
    def __init__(self, db, *args, **kwargs):
        super(Storage, self).__init__(*args, **kwargs)
        self.key = ''
        self.db = db
        self.centralWidget = QWidget()
        self.centralLayout = QHBoxLayout()
        self.centralLayout.setSpacing(0)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)
        self.state = {"id" : 0, "isUpdate" : False}
        self.setMinimumHeight(500)
        self.setMinimumWidth(1000)

        self.setWindowTitle("reavault")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
    def setKey(self, key):
        self.key = key

    def changeTheme(self, isChange=False):
        res = None

        # Open File
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
            self.themeIconDir   = "resources/darkToggle.png"
            self.editIconDir    = "resources/editDark.png"
            self.rightArrowDir  = "resources/rightLight.png"
        else:
            self.primaryBg      = "#242424"
            self.secondBg       = "#2E2E2E"
            self.primaryFg      = "#FFFFFF"
            self.secondFg       = "#323232"
            self.btnPrimaryBg   = "#505050"
            self.activeBg       = "#315BEF"       
            self.alternativeBg  = "#2D56DC"
            self.complementBg   = "#FFFFFF"
            self.themeIconDir   = "resources/lightToggle.png"
            self.editIconDir    = "resources/edit.png"
            self.rightArrowDir  = "resources/rightDark.png"

        # Save File
        with open('configuration/conf.json', 'w') as f:
            json.dump(res, f)

        ################################################

        self.setStyleSheet(f"background-color: {self.primaryBg};")

        # Reloading
        for i in reversed(range(self.centralLayout.count())):
            try:
                self.centralLayout.removeItem(self.centralLayout.itemAt(i))
            except:
                self.centralLayout.itemAt(i).widget().setParent(None)

        self.leftWidget = QWidget()
        self.midWidget = QWidget()
        self.rightWidget = QWidget()

        self.leftUI()
        self.midUIMain()
        self.rightUI()

        self.centralLayout.addWidget(self.leftWidget)
        self.centralLayout.addWidget(self.midWidget)
        self.centralLayout.addWidget(self.rightWidget)

    def leftUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        #######################################################
        scrollArea = QScrollArea()
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(scrollArea.sizePolicy().hasHeightForWidth());
        scrollArea.setSizePolicy(sizePolicy);
        scrollArea.setFrameShape(QFrame.NoFrame);
        scrollArea.setLineWidth(0);
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
        scrollArea.setWidgetResizable(True)
        
        #######################################################
        scrollWidget = QWidget()
        scrollWidget.setSizePolicy(sizePolicy)
        self.scrollLayout = QVBoxLayout()
        self.scrollLayout.setSpacing(0)
        self.scrollLayout.setContentsMargins(0, 0, 0, 0)

        self.leftRedoButton()

        #######################################################
        scrollWidget.setLayout(self.scrollLayout)
        scrollArea.setWidget(scrollWidget)

        #######################################################
        hLine = QFrame()
        hLine.setFrameShape(QFrame.HLine)
        hLine.setFrameShadow(QFrame.Sunken)
        hLine.setStyleSheet(f"margin-top: 3px;\nmargin-right: 5px;\nmargin-left:5px;\nbackground-color: {self.complementBg};\n")
        
        #######################################################
        createBtn = QPushButton()
        createBtn.clicked.connect(self.rightUIAfter)
        createBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        iconCreate = QtGui.QIcon()
        iconCreate.addPixmap(QtGui.QPixmap("resources/create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        createBtn.setIcon(iconCreate)
        createBtn.setStyleSheet(
            "QPushButton{\n"
            f"  background-color: {self.activeBg};\n"
            "   color: #FFFFFF;"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   margin: 5px 5px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.alternativeBg};\n"
            "}"
        )

        ########################################################
        layout.addWidget(scrollArea)
        layout.addWidget(hLine)
        layout.addWidget(createBtn)

        self.leftWidget.setStyleSheet(f"background-color: {self.primaryBg};")
        self.leftWidget.setLayout(layout)

    def leftUIAfter(self):
        # Reloading
        for i in reversed(range(self.scrollLayout.count())):
            try:
                self.scrollLayout.itemAt(i).widget().setParent(None)
            except:
                self.scrollLayout.removeItem(self.scrollLayout.itemAt(i))
        self.leftRedoButton()

    def leftRedoButton(self):
        # Retrieve Data
        getData = self.db.fetchData("SELECT * FROM Vaults;", self.key)
        for item in getData:
            btn = QPushButton(str(item[1]))
            btn.setStyleSheet(
                "QPushButton{\n"
                "   border: None;\n"
                f"  color: {self.primaryFg};\n"
                "   padding: 2px 100px 2px 20px;\n"
                "   text-align: left;\n"
                f"  background-image: url('{self.rightArrowDir}');\n"
                "   background-repeat: no-repeat;\n"
                "   background-position: right;\n"
                "}\n"
                "QPushButton::hover{\n"
                f"  background-color: {self.activeBg};\n"
                "   background-image: url('resources/rightDark.png');\n"
                "   color: white;\n"
                "}\n"
            )
            btn.adjustSize()
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.clicked.connect(lambda checked, itemId=item[0], button=btn: self.spawnView(itemId, button))
            self.scrollLayout.addWidget(btn)
        vSpacer = QSpacerItem(10, 10, QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        hSpacer = QSpacerItem(300, 10, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.scrollLayout.addItem(hSpacer)
        self.scrollLayout.addItem(vSpacer)

    def midUI(self):
        hSpacer1 = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        label = QLabel("CREATE NEW OR \nSELECT ONE TO VIEW")
        label.setAlignment(QtCore.Qt.AlignCenter)
        hSpacer2 = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        themeToggle = QPushButton()
        themeToggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        themeToggle.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        themeToggle.clicked.connect(lambda: self.changeTheme(True))
        iconTheme = QtGui.QIcon()
        iconTheme.addPixmap(QtGui.QPixmap(self.themeIconDir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        themeToggle.setIcon(iconTheme)
        themeToggle.setStyleSheet(
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
        
        self.contentLayout.addItem(hSpacer1, 0, 0)
        self.contentLayout.addWidget(themeToggle, 0, 2, QtCore.Qt.AlignRight)
        self.contentLayout.addWidget(label, 1, 1)
        self.contentLayout.addItem(hSpacer1, 2, 2)

    def midUIMain(self):
        self.contentLayout = QGridLayout()
        self.contentLayout.setSpacing(0)
        self.contentLayout.setContentsMargins(20, 20, 20, 0)

        self.midUI()
        
        self.midWidget.setStyleSheet(f"background-color: {self.secondBg};\ncolor: {self.primaryFg};")
        self.midWidget.setLayout(self.contentLayout)

    def spawnView(self, itemId=None, button=None):
        # Reloading
        for i in reversed(range(self.contentLayout.count())):
            try:
                self.contentLayout.itemAt(i).widget().setParent(None)
            except:
                self.contentLayout.removeItem(self.contentLayout.itemAt(i))

        # Styling Selected Item
        for i in reversed(range(self.scrollLayout.count())):
            try:
                self.scrollLayout.itemAt(i).widget().setStyleSheet(
                    "QPushButton{\n"
                    "   border: None;\n"
                    f"  color: {self.primaryFg};\n"
                    "   padding: 2px 100px 2px 20px;\n"
                    "   text-align: left;\n"
                    f"  background-image: url('{self.rightArrowDir}');\n"
                    "   background-repeat: no-repeat;\n"
                    "   background-position: right;\n"
                    "}\n"
                    "QPushButton::hover{\n"
                    f"  background-color: {self.activeBg};\n"
                    "   background-image: url('resources/rightDark.png');\n"
                    "   color: white;\n"
                    "}\n"
                )
            except:
                None

        # When No Item Selected
        if itemId == None:
            self.midUI()
            return

        self.state["id"] = itemId
        
        if button != None:
            button.setStyleSheet(
                "QPushButton{\n"
                "   border: None;\n"
                f"  background-color: {self.activeBg};\n"
                f"  background-image: url('resources/rightDark');\n"
                "   background-repeat: no-repeat;\n"
                "   background-position: right;\n"
                "   padding: 2px 100px 2px 20px;\n"
                "   text-align: left;\n"
                "   color: white;\n"
                "}\n"
            )

        ########################################################        

        getData = self.db.fetchData(f"SELECT * FROM Vaults WHERE id = {itemId};", self.key)

        userLabel = QLabel("Username")
        pwdLabel = QLabel("Password")
        userValue = QLabel(str(getData[0][2]))
        pwdValue = QLabel(str(getData[0][3]))

        userValue.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        pwdValue.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        userValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        pwdValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

        userLabel.setStyleSheet("font-size: 20px;\nfont-style: bold;\npadding: 10px;")
        userValue.setStyleSheet("font-size: 20px;\nfont-style: regular;\npadding: 10px;")
        pwdLabel.setStyleSheet("font-size: 20px;\nfont-style: bold;\npadding: 10px;")
        pwdValue.setStyleSheet("font-size: 20px;\nfont-style: regular;\npadding: 10px;")

        hSpacer = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        vSpacer = QSpacerItem(10, 10, QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)

        hLine = QFrame()
        hLine.setFrameShape(QFrame.HLine)
        hLine.setFrameShadow(QFrame.Sunken)
        hLine.setStyleSheet(f"margin-top: 3px;\nmargin-right: 5px;\nmargin-left:5px;\nbackground-color: {self.complementBg};\n")
        
        deleteBtn = QPushButton()   #Delete
        iconDelete = QtGui.QIcon()
        iconDelete.addPixmap(QtGui.QPixmap("resources/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        deleteBtn.setIcon(iconDelete)
        
        editBtn = QPushButton() #Edit
        iconEdit = QtGui.QIcon()
        iconEdit.addPixmap(QtGui.QPixmap(self.editIconDir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        editBtn.setIcon(iconEdit)

        editBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        editBtn.setStyleSheet(
            "QPushButton{\n"
            f"  background-color: {self.btnPrimaryBg};\n"
            f"  color: {self.primaryFg};"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   margin: 5px 5px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.activeBg};\n"
            "}"
        )

        deleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        deleteBtn.setStyleSheet(
            "QPushButton{\n"
            "   color: red;"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   margin: 5px 5px 5px;\n"
            "   text-align: center;\n"
            "}\n"
        )

        editBtn.clicked.connect(lambda: self.rightUIAfter(True))
        deleteBtn.clicked.connect(self.onDelete)

        for i in range(3):
            hL = QFrame()
            hL.setFrameShape(QFrame.HLine)
            hL.setFrameShadow(QFrame.Sunken)
            hL.setStyleSheet(f"margin-bottom: 3px;\nmargin-right: 5px;\nmargin-left:5px;\nbackground-color: {self.complementBg};\n")
            self.contentLayout.addWidget(hL, i*2, 0, 1, 6)
        
        vL1 = QFrame()
        vL1.setFrameShape(QFrame.VLine)
        vL1.setFrameShadow(QFrame.Sunken)
        vL1.setStyleSheet(f"margin-right: 3px;\nbackground-color: {self.complementBg};\n")
        vL2 = QFrame()
        vL2.setFrameShape(QFrame.VLine)
        vL2.setFrameShadow(QFrame.Sunken)
        vL2.setStyleSheet(f"margin-right: 3px;\nbackground-color: {self.complementBg};\n")

        themeToggle = QPushButton()
        themeToggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        themeToggle.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        themeToggle.clicked.connect(lambda: self.changeTheme(True))
        iconTheme = QtGui.QIcon()
        iconTheme.addPixmap(QtGui.QPixmap(self.themeIconDir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        themeToggle.setIcon(iconTheme)
        themeToggle.setStyleSheet(
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

        self.contentLayout.addWidget(vL1, 1, 1)
        self.contentLayout.addWidget(vL2, 3, 1)

        self.contentLayout.addWidget(userLabel, 1, 0)
        self.contentLayout.addWidget(userValue, 1, 2, 1, 4)
        self.contentLayout.addWidget(pwdLabel, 3, 0)
        self.contentLayout.addWidget(pwdValue, 3, 2, 1, 4)
        self.contentLayout.addItem(vSpacer, 5, 1)
        self.contentLayout.addItem(hSpacer, 5, 2)
        self.contentLayout.addWidget(hLine, 6, 0, 1, 6)
        self.contentLayout.addWidget(themeToggle, 7, 0)
        self.contentLayout.addWidget(deleteBtn, 7, 4)
        self.contentLayout.addWidget(editBtn, 7, 5)

        self.rightUIBefore()

    def credit(self):
        None

    def rightUI(self):
        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(20, 10, 20, 0)
        
        titleFieldLabel = QLabel("Title")
        titleFieldLabel.setStyleSheet("padding: 10px 0px 10px;")
        
        userFieldLabel = QLabel("Username")
        userFieldLabel.setStyleSheet("padding: 10px 0px 10px;")
        
        pwdFieldLabel = QLabel("Password")
        pwdFieldLabel.setStyleSheet("padding: 10px 0px 10px;")

        self.titleField = QLineEdit()
        self.userField = QLineEdit()
        self.pwdField = QLineEdit()

        self.titleField.setMaxLength(20)
        self.userField.setMaxLength(32)
        self.pwdField.setMaxLength(32)

        self.titleField.setStyleSheet(
            "QLineEdit {\n"
            f"  border: 2px solid {self.btnPrimaryBg};\n"
            "   border-radius: 4px;\n"
            "   padding: 2px;\n"
            "}\n"
            "QLineEdit::focus {\n"
            f"  border: 2px solid {self.activeBg};\n"
            "}"
        )
        self.userField.setStyleSheet(
            "QLineEdit {\n"
            f"  border: 2px solid {self.btnPrimaryBg};\n"
            "   border-radius: 4px;\n"
            "   padding: 2px;\n"
            "}\n"
            "QLineEdit::focus {\n"
            f"  border: 2px solid {self.activeBg};\n"
            "}"
        )
        self.pwdField.setStyleSheet(
            "QLineEdit {\n"
            f"  border: 2px solid {self.btnPrimaryBg};\n"
            "   border-radius: 4px;\n"
            "   padding: 2px;\n"
            "}\n"
            "QLineEdit::focus {\n"
            f"  border: 2px solid {self.activeBg};\n"
            "}"
        )

        vSpacer = QSpacerItem(10, 10, QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        hSpacer = QSpacerItem(250, 10, QSizePolicy.Fixed, QSizePolicy.Maximum)

        hLine = QFrame()
        hLine.setFrameShape(QFrame.HLine)
        hLine.setFrameShadow(QFrame.Sunken)
        hLine.setStyleSheet(f"margin-top: 3px;\nmargin-right: 5px;\nmargin-left:5px;\nbackground-color: {self.primaryBg};\n")

        cancelBtn = QPushButton()
        iconCancel = QtGui.QIcon()
        iconCancel.addPixmap(QtGui.QPixmap("resources/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cancelBtn.setIcon(iconCancel)
        submitBtn = QPushButton("Save")
        iconSubmit = QtGui.QIcon()
        iconSubmit.addPixmap(QtGui.QPixmap("resources/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        submitBtn.setIcon(iconSubmit)

        cancelBtn.setStyleSheet(
            "QPushButton{\n"
            f"  color: {self.primaryFg};\n"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   margin: 5px 5px 5px;\n"
            "   text-align: center;\n"
            "}"
        )
        cancelBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        submitBtn.setStyleSheet(
            "QPushButton{\n"
            f"  background-color: {self.activeBg};\n"
            "   color: #FFFFFF;\n"
            "   border-radius: 10px;\n"
            "   padding: 5px 15px 5px;\n"
            "   margin: 5px 5px 5px;\n"
            "   text-align: center;\n"
            "}\n"
            "QPushButton::hover{\n"
            f"  background-color: {self.alternativeBg};\n"
            "}"
        )
        submitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        cancelBtn.clicked.connect(self.rightUIBefore)
        submitBtn.clicked.connect(self.transaction)

        layout.addWidget(titleFieldLabel, 0, 0)
        layout.addWidget(self.titleField, 0, 1)
        layout.addWidget(userFieldLabel, 1, 0)
        layout.addWidget(pwdFieldLabel, 2, 0)
        layout.addWidget(self.userField, 1, 1)
        layout.addWidget(self.pwdField, 2, 1)
        layout.addItem(vSpacer, 3, 0)
        layout.addItem(hSpacer, 4, 0, 1, 2)
        layout.addWidget(hLine, 5, 0, 1, 2)
        layout.addWidget(cancelBtn, 6, 0)
        layout.addWidget(submitBtn, 6, 1)

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(self.rightWidget.sizePolicy().hasHeightForWidth());
        self.rightWidget.setSizePolicy(sizePolicy);

        self.rightWidget.setLayout(layout)
        self.rightWidget.setStyleSheet(
            f"background-color: {self.complementBg};\n"
            f"color: {self.primaryBg};"
        )
        self.rightUIBefore()

    def rightUIBefore(self):
        self.state["isUpdate"] = False
        self.titleField.clear()
        self.userField.clear()
        self.pwdField.clear()
        self.rightWidget.hide()

    def rightUIAfter(self, isUpdate=False):
        self.rightWidget.show()
        if isUpdate == True:
            itemId = self.state["id"]
            self.state["isUpdate"] = True
            getData = self.db.fetchData(f"SELECT * FROM Vaults WHERE id = {itemId};", self.key)

            self.titleField.setText(str(getData[0][1]))
            self.userField.setText(str(getData[0][2]))
            self.pwdField.setText(str(getData[0][3]))
        else:
            self.state["isUpdate"] = False
            self.titleField.clear()
            self.userField.clear()
            self.pwdField.clear()

    def transaction(self):
        if self.titleField.text().isspace() == True or self.titleField.text() == '' or self.userField.text().isspace() == True or self.userField.text() == '' or self.pwdField.text().isspace() == True or self.pwdField.text() == '':
            self.raiseError()
            return
        if self.state["isUpdate"] == True:
            self.db.insertData("UPDATE Vaults SET "
                f"title = '{self.titleField.text()}', "
                f"username = '{self.userField.text()}', "
                f"password = '{self.pwdField.text()}' "
                f"WHERE id = {self.state['id']};" ,self.key
            )
        else:
            self.db.insertData(f"INSERT INTO Vaults VALUES(null, '{self.titleField.text()}', '{self.userField.text()}', '{self.pwdField.text()}');", self.key)
        self.leftUIAfter()
        self.rightUIBefore()
        self.spawnView()

    def onDelete(self):
        self.db.insertData(f"DELETE FROM Vaults WHERE id = {self.state['id']};", self.key)
        self.leftUIAfter()
        self.rightUIBefore()
        self.spawnView()