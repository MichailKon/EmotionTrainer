import os
import random
import sys
import datetime as dt

import cv2
import numpy as np
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from keras.models import load_model
import pygame

from Interface import MainAppInterface as MainAI
from Interface import RecognitionAppInterface as RecognitionAI
from Interface import UITrainer as UserRecognizesAI
from Interface import AfterFirstInterface as AfterFirstAI
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
        face = np.array((Image.fromarray(face).convert('L')).resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)) / 255
        face = face.reshape((1, IMG_SIZE, IMG_SIZE, 1))
        predictions = self.model.predict(face).reshape(CNT_CLASSES - 1).tolist()
        predictions = [(CLASSES[language][i], predictions[i]) for i in range(CNT_CLASSES - 1) if predictions[i] >= 0.1]
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
        self.ui.Language.clicked.connect(self.swap_language)
        self.ui.ToFirstTrainer.clicked.connect(self.open_rezognizes)
        self.ui.Language.setIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'Icons', 'Eng.png')))
        self.ui.Language.setIconSize(QtCore.QSize(45, 45))

    def swap_language(self):
        global language, ind
        if language == 'en':
            self.ui.Language.setIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'Icons', 'Eng.png')))
        else:
            self.ui.Language.setIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'Icons', 'Rus.png')))
        language, ind = LANGUAGES[not ind], not ind
        self.translating()

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
        self.shown_images = 0
        self.true_images = -1
        self.last_answer = None
        self.statistics = []
        self.is_opened_statistics = None
        self.music_filename = None
        self.mixer = pygame.mixer
        # Connecting buttons
        self.ui.SetNextFace.clicked.connect(self.next_image)
        self.ui.ToMainWindow.clicked.connect(self.to_main_window)
        for i in CLASSES['en']:
            exec('self.ui.{}.clicked.connect(self.{}_clicked)'.format(i, i.lower()))
        # Making window
        self.ui.Progress.setMinimum(0)
        self.ui.Progress.setMaximum(100)
        self.ui.Progress.setValue(0)

    def translating(self):
        self.ui.ToMainWindow.setText(WORDS[language][self.ui.ToMainWindow.text()])
        for i in CLASSES['en']:
            exec("self.ui.{}.setText(CLASSES[language][CLASSES['en'].index(i)])".format(i))
        self.ui.SetNextFace.setText(WORDS[language][self.ui.SetNextFace.text()])
        self.ui.Emotion.setTitle(WORDS[language][self.ui.Emotion.title()])

    def next_image(self):
        self.shown_images += 1
        user_answer = self.get_selected_button()
        if len(self.statistics) >= 1:
            self.statistics[-1].append(user_answer)
            self.statistics[-1].append(round((dt.datetime.now() - self.last_answer).total_seconds(), 1))
        if self.shown_images > 10:
            self.to_statistics()
            return
        self.statistics.append([])
        self.true_images += user_answer == self.now_emotion
        self.now_emotion = random.choice(CLASSES['en'])

        try:
            self.mixer.init()
            self.mixer.music.load(os.path.join(os.getcwd(), 'Music', self.now_emotion + ".mp3"))
            self.mixer.music.play()
        except pygame.error:
            print(self.now_emotion)

        cnt_photos = len(os.listdir(os.path.join(os.getcwd(), 'Emotions', self.now_emotion)))
        num_emotion = str(random.randint(1, cnt_photos))
        path_to_image = os.path.join(os.getcwd(), 'Emotions', self.now_emotion, self.now_emotion + num_emotion + '.jpg')
        image = QtGui.QPixmap(path_to_image)
        temp = QtGui.QTransform().rotate(90)
        image = image.scaled(QtCore.QSize(672, 504)).transformed(temp)
        self.ui.Image.setPixmap(image)
        self.ui.Progress.setValue(self.ui.Progress.value() + 10)
        self.statistics[-1].append(path_to_image)
        self.statistics[-1].append(self.now_emotion)
        self.last_answer = dt.datetime.now()

    def to_main_window(self):
        self.mixer.music.stop()
        if not self.is_opened_main:
            self.is_opened_main = MainWindowApp()
        self.is_opened_main.translating()
        self.is_opened_main.show()
        self.hide()

    def to_statistics(self):
        self.mixer.music.stop()
        if not self.is_opened_statistics:
            self.is_opened_statistics = AfterFirstApp(statistics=self.statistics)
        self.is_opened_statistics.translating()
        self.hide()
        self.is_opened_statistics.show()

    def get_selected_button(self):
        for i in CLASSES['en']:
            command = 'self.ui.{}.isChecked() == 1'
            if eval(command.format(i)):
                return i

    def make_one_choice(self, emotion=None):
        for i in CLASSES['en']:
            exec('self.ui.{}.setChecked(False)'.format(i))
        if emotion:
            exec('self.ui.{}.setChecked(True)'.format(emotion))

    def angry_clicked(self):
        self.make_one_choice('Angry')

    def disgust_clicked(self):
        self.make_one_choice('Disgust')

    def fear_clicked(self):
        self.make_one_choice('Fear')

    def happy_clicked(self):
        self.make_one_choice('Happy')

    def sad_clicked(self):
        self.make_one_choice('Sad')

    def surprised_clicked(self):
        self.make_one_choice('Surprised')

    def neutral_clicked(self):
        self.make_one_choice('Neutral')

    def scorn_clicked(self):
        self.make_one_choice('Scorn')


class AfterFirstApp(QtWidgets.QWidget):
    def __init__(self, parent=None, statistics=None):
        # All variables
        super().__init__(parent)
        self.ui = AfterFirstAI.Ui_Form()
        self.ui.setupUi(self)
        self.is_opened_main = None
        self.statistics = statistics
        # Connecting buttons
        self.ui.ToMainWindow.clicked.connect(self.to_main_window)
        self.ui.ToAfterFirst.clicked.connect(self.to_after_first)
        # Making form
        self.make_table()
        self.ui.ToAfterFirst.setVisible(False)
        self.ui.Image.setVisible(False)
        # self.sx = self.x()
        # self.sy = self.y()

    def translating(self):
        self.ui.ToMainWindow.setText(WORDS[language][self.ui.ToMainWindow.text()])
        self.ui.ToAfterFirst.setText(WORDS[language][self.ui.ToAfterFirst.text()])
        self.ui.Statistics.setHorizontalHeaderLabels(TABLE_NAMES[language])

    def make_table(self):
        self.ui.Statistics.setHorizontalHeaderLabels(TABLE_NAMES[language])
        self.ui.Statistics.setSortingEnabled(False)
        row = 0
        for i in self.statistics:
            column = 0
            for j in i:
                cellinfo = QtWidgets.QTableWidgetItem(str(j))
                if 1 <= column <= 2 and j is not None:
                    cellinfo = QtWidgets.QTableWidgetItem(CLASSES[language][CLASSES['en'].index(str(j))])
                btn = QtWidgets.QPushButton(text='{} {}'.format(WORDS[language]['Показать фото'], row + 1))
                btn.clicked.connect(self.show_photo)
                if column:
                    self.ui.Statistics.setItem(row, column, cellinfo)
                else:
                    self.ui.Statistics.setCellWidget(row, column, btn)
                column += 1
            row += 1

    def show_photo(self):
        num_photo = str(int(self.sender().text().split()[-1]) - 1)
        path_to_image = self.statistics[int(num_photo)][0]
        image = QtGui.QPixmap(path_to_image)
        temp = QtGui.QTransform().rotate(90)
        image = image.scaled(QtCore.QSize(672, 504)).transformed(temp)

        self.setGeometry(self.x(), self.y(), 700, 750)
        self.ui.Image.setVisible(True)
        self.ui.ToAfterFirst.setVisible(True)
        self.ui.Statistics.setVisible(False)
        self.ui.ToMainWindow.setVisible(False)
        self.ui.Image.setPixmap(image)

    def to_main_window(self):
        if not self.is_opened_main:
            self.is_opened_main = MainWindowApp()
            self.is_opened_main.translating()
        self.hide()
        self.is_opened_main.show()

    def to_after_first(self):
        self.setGeometry(self.x(), self.y(), 790, 520)
        self.ui.Image.setVisible(False)
        self.ui.ToAfterFirst.setVisible(False)
        self.ui.Statistics.setVisible(True)
        self.ui.ToMainWindow.setVisible(True)


if __name__ == "__main__":
    app1 = QtWidgets.QApplication(sys.argv)
    ERA = MainWindowApp()
    ERA.show()
    sys.exit(app1.exec())
