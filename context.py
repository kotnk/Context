import datetime


class TryLoad:
    def __init__(self, path):
        self.path = path
        self.start_date = datetime.datetime.now()
        print(f'Запуск процесса начат {self.start_date}')

    def __enter__(self):
        self.file = open(self.path, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_date = datetime.datetime.now()
        print(f'Процесс завершен {self.end_date}')
        print(f'Управились за {self.end_date - self.start_date}')
        self.file.close()


def main():
    search = input('Что ищем? Введите значения через запятую.\n>').strip().split(',')
    print(search)
    found = 0
    with TryLoad('somefile.txt', ) as file:
        while True:
            for line in file:
                print(line)
                data = file.readline().strip()
                for items in search:
                    if items in data:
                        found += 1
            break
        print(f'Найдено {found} совпадений')


main()
