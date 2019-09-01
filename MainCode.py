import re
import sys

import cv2
import numpy as np
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from keras.models import load_model

import MainInterface as MainI
import RecognitionAppInterface as RecognitionAI
from constants import *


class EmotionRecognitionApp(QtWidgets.QWidget):
    model = load_model(MODEL_PATH)
    faceCascade = cv2.CascadeClassifier(CASCADE_PATH)

    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui = RecognitionAI.Ui_Form()
        self.ui.setupUi(self)
        self.is_opened_main = None
        self.faces = []
        self.frame = None
        self.cam = None

        self.ui.Start_recognition.clicked.connect(self.bp)
        self.ui.ToMainWindow.clicked.connect(self.open_main)
        self.ui.user_answered.clicked.connect(self.recognize_emotion)

        self.ui.Result.setText('')
        self.ui.user_input.setReadOnly(True)
        self.ui.Result.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.user_input.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.user_answered.setEnabled(False)

    def bp(self):
        # After this user can't writing anything in that place
        self.ui.Result.setText('')
        self.ui.user_answered.setEnabled(False)
        self.ui.user_input.setReadOnly(True)
        self.ui.user_input.setText('')
        # Recognizing emotion
        self.cam = cv2.VideoCapture(0)
        good = [ord(i) for i in ['q', 'Q', ' ', 'й', 'Й']]
        while self.cam and self.cam.isOpened():
            ret, frame = self.cam.read()
            if not self.cam or any([cv2.waitKey(1) == i for i in good]):
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
        self.cam = None
        self.ui.Result.setText('Введите номер вашего лица')
        self.ui.user_input.setReadOnly(False)
        self.ui.user_answered.setEnabled(True)
        cv2.destroyWindow('Video')

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

    def open_main(self):
        self.close()
        self.cam = None
        if not self.is_opened_main:
            self.is_opened_main = MainWindowApp(self)
        self.is_opened_main.show()


class MainWindowApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui = MainI.Ui_Form()
        self.ui.setupUi(self)

        self.is_opened_recognition = None

        self.ui.pushButton.clicked.connect(self.open_recognition)

    def open_recognition(self):
        self.close()
        if not self.is_opened_recognition:
            self.is_opened_recognition = EmotionRecognitionApp(self)
        self.is_opened_recognition.show()


if __name__ == "__main__":
    app1 = QtWidgets.QApplication(sys.argv)
    ERA = MainWindowApp()
    ERA.show()
    sys.exit(app1.exec())
