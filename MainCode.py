import re
import sys

import cv2
import numpy as np
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from keras.models import load_model

from constants import *
from inter import Ui_Form


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.faceCascade = cv2.CascadeClassifier(CASCADE_PATH)
        self.ui = Ui_Form()
        self.model = load_model(MODEL_PATH)
        self.ui.setupUi(self)

        self.ui.Start_recognition.clicked.connect(self.bp)
        self.ui.Result.setText('')
        self.ui.user_input.setReadOnly(True)
        self.ui.user_answered.clicked.connect(self.recognize_emotion)
        self.faces = []
        self.frame = None
        self.ui.Result.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.user_input.setAlignment(QtCore.Qt.AlignCenter)

    def bp(self):
        cam = cv2.VideoCapture(0)
        good = [ord(i) for i in ['q', 'Q', ' ', 'й', 'Й']]
        while cam.isOpened():
            ret, frame = cam.read()
            if any([cv2.waitKey(1) == i for i in good]):
                cv2.destroyAllWindows()
                break
            faces = self.faceCascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
            num = 1
            self.faces = faces
            self.frame = frame
            frame1 = frame.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(frame1, (x, y), (x + w, x + h), (0, 0, 255), 2)
                cv2.putText(frame1, str(num), (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                num += 1
            cv2.imshow('Video', frame1)
            rgbImage = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            self.ui.Image.setPixmap(QtGui.QPixmap(convertToQtFormat))
        cam.release()
        del cam
        self.ui.Result.setText('Введите номер вашего лица')
        self.ui.user_input.setReadOnly(False)

    def recognize_emotion(self):
        pattern = r"\d+"
        if not re.fullmatch(pattern, self.ui.user_input.text().strip()):
            self.ui.Result.setText('Ваш текст либо пустой,\n либо содержит не только цифры!')
            return None
        number = int(self.ui.user_input.text())
        number -= 1
        if not (0 <= number < len(self.faces)):
            self.ui.Result.setText('Такого лица нет!')
            return None
        face = self.faces[number]
        face = self.frame[face[1]:(face[1] + face[3]), face[0]:(face[0] + face[2])]
        face = np.array((Image.fromarray(face).convert('1')).resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS))
        face = face.reshape((1, IMG_SIZE, IMG_SIZE, 1))
        predictions = self.model.predict(face).reshape(CNT_CLASSES).tolist()
        predictions = [(CLASSES[i], predictions[i]) for i in range(CNT_CLASSES) if predictions[i] >= 0.1]
        predictions = sorted(predictions, reverse=True)
        predictions = [i[0] for i in predictions]
        self.ui.Result.setText(",".join(predictions))


if __name__ == "__main__":
    app1 = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app1.exec())
