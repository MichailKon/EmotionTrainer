CASCADE_PATH = r'face_detector.xml'
IMG_SIZE = 48
MODEL_PATH = r'model'
CLASSES = {'en': ('Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprised', 'Neutral', 'Scorn'),
           'ru': ('Злость', 'Отвращение', 'Страх', 'Счастье', 'Печаль', 'Удивление', 'Нейтральность', 'Презрение')}
TABLE_NAMES = {'en': ('Image', 'True answer', 'Your answer', 'Time'),
               'ru': ('Фото', 'Правильный ответ', 'Ваш ответ', 'Время')}
CNT_CLASSES = 8
LANGUAGES = ('ru', 'en')
WORDS = dict()
WORDS['en'], WORDS['ru'] = dict(), dict()

WORDS['en']['Show emotion'] = WORDS['en']['Покажи эмоцию'] = 'Show emotion'
WORDS['ru']['Show emotion'] = WORDS['ru']['Покажи эмоцию'] = 'Покажи эмоцию'
WORDS['en']['Guess the emotion'] = WORDS['en']['Угадай эмоцию'] = 'Guess the emotion'
WORDS['ru']['Guess the emotion'] = WORDS['ru']['Угадай эмоцию'] = 'Угадай эмоцию'
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
WORDS['en']['Choose an emotion'] = WORDS['en']['Выберите эмоцию'] = 'Choose an emotion'
WORDS['ru']['Choose an emotion'] = WORDS['ru']['Выберите эмоцию'] = 'Выберите эмоцию'
WORDS['en']['Check'] = WORDS['en']['Проверить'] = 'Check'
WORDS['ru']['Check'] = WORDS['ru']['Проверить'] = 'Проверить'
WORDS['en']['Show a photo'] = WORDS['en']['Показать фото'] = 'Show a photo'
WORDS['ru']['Show a photo'] = WORDS['ru']['Показать фото'] = 'Показать фото'