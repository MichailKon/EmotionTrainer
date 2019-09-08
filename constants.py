CASCADE_PATH = r'face_detector.xml'
IMG_SIZE = 48
MODEL_PATH = r'model'
CLASSES = {'en': ('Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprised', 'Neutral'),
           'ru': ('Злость', 'Отвращение', 'Страх', 'Счастье', 'Печаль', 'Удивление', 'Нейтральность')}
CNT_CLASSES = 7
LANGUAGES = ('ru', 'en')
WORDS = dict()
WORDS['en'], WORDS['ru'] = dict(), dict()

WORDS['en']['Second trainer'] = WORDS['en']['Второй тренажер'] = 'Second trainer'
WORDS['ru']['Second trainer'] = WORDS['ru']['Второй тренажер'] = 'Второй тренажер'
WORDS['en']['First trainer'] = WORDS['en']['Первый тренажер'] = 'First trainer'
WORDS['ru']['First trainer'] = WORDS['ru']['Первый тренажер'] = 'Первый тренажер'
WORDS['en']['Начать распознавание'] = WORDS['en']['Start recognition'] = 'Start recognition'
WORDS['ru']['Начать распознавание'] = WORDS['ru']['Start recognition'] = 'Начать распознавание'
WORDS['en']['Back'] = WORDS['en']['Назад'] = 'Back'
WORDS['ru']['Back'] = WORDS['ru']['Назад'] = 'Назад'
WORDS['en']['Your text is empty, \n or contains not only digits!'] = \
    WORDS['en']['Ваш текст либо пустой,\n либо содержит не только цифры!'] = \
    'Your text is empty, \n or contains not only digits!'
WORDS['ru']['Ваш текст либо пустой,\n либо содержит не только цифры!'] = \
    WORDS['ru']['Your text is empty, \n or contains not only digits!'] = \
    'Ваш текст либо пустой,\n либо содержит не только цифры!'
WORDS['en']['There is no such face!'] = WORDS['en']['Такого лица нет!'] = 'There is no such face!'
WORDS['ru']['Такого лица нет!'] = WORDS['ru']['There is no such face!'] = 'Такого лица нет!'
WORDS['en']['Enter number of your face'] = WORDS['en']['Введите номер вашего лица'] = 'Enter number\nof your face'
WORDS['ru']['Введите номер вашего лица'] = WORDS['ru']['Enter number of your face'] = 'Введите номер\n вашего лица'
WORDS['en']['Right'] = WORDS['en']['Правильно'] = 'Right'
WORDS['ru']['Right'] = WORDS['ru']['Правильно'] = 'Правильно'
WORDS['en']['Wrong'] = WORDS['en']['Неправильно'] = 'Неправильно'
WORDS['ru']['Wrong'] = WORDS['ru']['Неправильно'] = 'Неправильно'