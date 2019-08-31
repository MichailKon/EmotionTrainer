from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import sys
from inter import Ui_Form
import cv2


class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)

    def run(self):
                cam = cv2.VideoCapture(0)
                while cam.isOpened():
                    ret, frame = cam.read()
                    if cv2.waitKey(1) & 0xFF == ord(' ') or not ret:
                        break
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    convertToQRFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                    convertToQRFormat = QPixmap.fromImage(convertToQRFormat)
                    p = convertToQRFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)


class App(QWidget):
    def __init__(self):
        super().__init__()
        # some inits
        self.title = 'Image'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        # not some inits
        self.initUI()

    def initUI(self, image=None):
        self.setWindowTitle('Image')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(640, 480)

        label = QLabel(self)
        label.move(0, 0)
        label.resize(640, 480)
        th = Thread(self)
        th.changePixmap.connect(label.setPixmap)
        th.start()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec_())
