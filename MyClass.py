class MyClass:
    def __init__(self):
        self.first = []
        print('Making')

    def add(self, element):
        self.first.append(element)

    def get(self, ind):
        return self.first[ind]
