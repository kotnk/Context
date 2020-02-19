import datetime
from random import randrange


class manager:

    def __init__(self):
        self.start = datetime.datetime.now()
        print(f'Процесс запущен ({self.start})')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        print(f'Разгадано!\nВремя окончания: {self.end}\nПроцесс занял {self.end - self.start}')


def guesser():
    secret = randrange(100, 10000000)
    print(f'Загадано число: {secret}')
    guess = int()
    while guess != secret:
        guess = randrange(100, 10000000)


if __name__ == '__main__':
    with manager():
        guesser()
