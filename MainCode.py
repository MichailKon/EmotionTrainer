from PySide2 import QtCore, QtGui, QtWidgets
import sys
from inter import Ui_Form


if __name__ == "__main__":
    # create app
    app = QtWidgets.QApplication(sys.argv)

    # create form
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    # logic
    def bp():
        ui.textEdit.setText("Произошел Тык")

    ui.pushButton.clicked.connect(bp)

    # launch
    sys.exit(app.exec_())
