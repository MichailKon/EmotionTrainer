import os
import random
import sys

import cv2
import numpy as np
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from keras.models import load_model

import MainAppInterface as MainAI
import RecognitionAppInterface as RecognitionAI
import UITrainer as UserRecognizesAI
from constants import *

language = 'ru'
ind = 0


class EmotionRecognitionApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # All variables
        super().__init__(parent)
        self.ui = RecognitionAI.Ui_Form()
        self.ui.setupUi(self)
        self.is_opened_main = None
        self.faces = []
        self.frame = None
        self.cam = None
        self.model = load_model(MODEL_PATH)
        self.faceCascade = cv2.CascadeClassifier(CASCADE_PATH)
        # Connecting buttons
        self.ui.Start_recognition.clicked.connect(self.open_window_with_recognition)
        self.ui.ToMainWindow.clicked.connect(self.open_main)
        self.ui.user_answered.clicked.connect(self.recognize_emotion)
        # Making form
        self.ui.Result.setText('')
        self.ui.UserInput.setReadOnly(True)
        self.ui.Result.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.user_answered.setEnabled(False)

    def translating(self):
        self.ui.Start_recognition.setText(WORDS[language][self.ui.Start_recognition.text()])
        self.ui.ToMainWindow.setText(WORDS[language][self.ui.ToMainWindow.text()])

    def open_window_with_recognition(self):
        # After this user can't writing anything in that place
        self.ui.Start_recognition.setEnabled(False)
        self.ui.Result.setText('')
        self.ui.user_answered.setEnabled(False)
        self.ui.UserInput.setReadOnly(True)

        # Recognizing emotion
        self.cam = cv2.VideoCapture(0)
        while self.cam.isOpened():
            ret, frame = self.cam.read()
            if cv2.waitKey(1) == ord(' '):
                break
            faces = self.faceCascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            num = 1
            self.faces = faces
            self.frame = frame
            frame1 = frame.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame1, str(num), (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                num += 1
            cv2.imshow('Video', frame1)
            rgb_image = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            res_picture = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
            self.ui.Image.setPixmap(QtGui.QPixmap(res_picture))
        self.cam.release()
        # Making interface available
        self.ui.Result.setText(WORDS[language]['Введите номер вашего лица'])
        self.ui.UserInput.setReadOnly(False)
        self.ui.user_answered.setEnabled(True)
        cv2.destroyWindow('Video')
        self.ui.Start_recognition.setEnabled(True)

    def recognize_emotion(self):
        number = int(self.ui.UserInput.text())
        number -= 1
        if not (0 <= number < len(self.faces)):
            self.ui.Result.setText(WORDS[language]['Такого лица нет!'])
            return None
        # Magic with picture
        face = self.faces[number]
        face = self.frame[face[1]:(face[1] + face[3]), face[0]:(face[0] + face[2])]
        face = np.array((Image.fromarray(face).convert('1')).resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS))
        face = face.reshape((1, IMG_SIZE, IMG_SIZE, 1))
        predictions = self.model.predict(face).reshape(CNT_CLASSES).tolist()
        predictions = [(CLASSES[language][i], predictions[i]) for i in range(CNT_CLASSES) if predictions[i] >= 0.1]
        predictions = [i[0] for i in sorted(predictions, reverse=True)]
        self.ui.Result.setText(",".join(predictions))

    def open_main(self):
        if self.cam:
            self.cam.release()
        if not self.is_opened_main:
            self.is_opened_main = MainWindowApp()
        self.is_opened_main.translating()
        self.is_opened_main.show()
        self.hide()


def swap_language():
    global language, ind
    language, ind = LANGUAGES[not ind], not ind
    if ERA is not None:
        ERA.translating()


class MainWindowApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # All variables
        super().__init__(parent)
        self.ui = MainAI.Ui_Form()
        self.ui.setupUi(self)
        self.is_opened_recognition = None
        self.is_opened_recognizes = None
        # Connecting buttons
        self.ui.ToSecondTrainer.clicked.connect(self.open_recognition)
        self.ui.Language.clicked.connect(swap_language)
        self.ui.ToFirstTrainer.clicked.connect(self.open_rezognizes)
        self.ui.Language.setIcon(QtGui.QIcon(r'Eng.png'))
        self.ui.Language.setIconSize(QtCore.QSize(45, 45))

    def translating(self):
        if self.is_opened_recognition:
            self.is_opened_recognition.translating()
        if self.is_opened_recognizes:
            self.is_opened_recognizes.translating()
        self.ui.ToSecondTrainer.setText(WORDS[language][self.ui.ToSecondTrainer.text()])
        self.ui.ToFirstTrainer.setText(WORDS[language][self.ui.ToFirstTrainer.text()])

    def open_recognition(self):
        if not self.is_opened_recognition:
            self.is_opened_recognition = EmotionRecognitionApp()
        self.is_opened_recognition.translating()
        self.is_opened_recognition.show()
        self.hide()

    def open_rezognizes(self):
        if not self.is_opened_recognizes:
            self.is_opened_recognizes = UserRecognizesApp()
            self.is_opened_recognizes.next_image()
        self.is_opened_recognizes.translating()
        self.is_opened_recognizes.show()
        self.hide()


class UserRecognizesApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # All variables
        super().__init__(parent)
        self.now_emotion = None
        self.ui = UserRecognizesAI.Ui_Dialog()
        self.ui.setupUi(self)
        self.is_opened_main = None
        # Connecting buttons
        self.ui.SetNextFace.clicked.connect(self.next_image)
        self.ui.ToMainWindow.clicked.connect(self.to_main_window)

    def translating(self):
        self.ui.ToMainWindow = WORDS[language][self.ui.ToMainWindow.text()]
        self.ui.Emotion.clear()
        self.ui.Emotion.addItems(CLASSES[language])

    def next_image(self):
        if self.ui.Emotion.currentText() != '':
            answer = self.ui.Emotion.currentIndex()
            user_choice = CLASSES['en'][answer]
        if self.ui.Image.pixmap() is not None:
            self.ui.IsUserRight.setText("Right" if user_choice == self.now_emotion else "Wrong")
        self.now_emotion = random.choice(CLASSES['en'])
        cnt_photos = len(os.listdir(os.path.join(os.getcwd(), 'Emotions', self.now_emotion)))
        num_emotion = str(random.randint(1, cnt_photos))
        path_to_image = os.path.join(os.getcwd(), 'Emotions', self.now_emotion, self.now_emotion + num_emotion + '.jpg')
        image = QtGui.QPixmap(path_to_image)
        image = image.scaled(QtCore.QSize(400, 350))
        self.ui.Image.setPixmap(image)

    def to_main_window(self):
        if not self.is_opened_main:
            self.is_opened_main = MainWindowApp()
        self.is_opened_main.translating()
        self.is_opened_main.show()
        self.hide()


if __name__ == "__main__":
    app1 = QtWidgets.QApplication(sys.argv)
    ERA = MainWindowApp()
    ERA.show()
    sys.exit(app1.exec())
