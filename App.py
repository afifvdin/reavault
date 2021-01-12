# Import Own Files
from widgets.Storage import *
from widgets.User import *
import bin.__database__ as db
#
from PyQt5.QtWidgets import QApplication
import sys, platform

app = QApplication(sys.argv)
if platform.system() == "Windows":
    app.setFont(QtGui.QFont("Arial", 11, 500))

user = User()
user.databaseFunction(db)
storage = Storage(db)
user.setNextPoint(storage)

user.show()
sys.exit(app.exec_())