import random

class Checker():
    def __init__(self):
        self._secret = []

    def get_secret_number(self):
        self._secret = random.randint(1000,9999)
        print(self._secret)