import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from chatUI import Ui_MainWindow

import chatUI
import Threaded_client

class AppWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()

		self.client = Threaded_client()


app = QApplication(sys.argv)
MainWindow = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)

MainWindow.show()
sys.exit(app.exec_())