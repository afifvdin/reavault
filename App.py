# Import Own Files
from widgets.Storage import *
from widgets.User import *
import bin.__database__ as db
#
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
user = User()
user.databaseFunction(db)
storage = Storage(db)
user.setNextPoint(storage)

user.show()
sys.exit(app.exec_())