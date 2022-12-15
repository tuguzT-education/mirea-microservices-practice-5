import sys
from PyQt5.QtWidgets import QApplication, QWidget

application = QApplication(sys.argv)

window = QWidget()
window.resize(320, 240)
window.setWindowTitle('Hello, World!')
window.show()

sys.exit(application.exec_())
