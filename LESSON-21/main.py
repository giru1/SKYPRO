from abc import ABC, abstractmethod

class Storage(ABC):
    def __init__(self, capacity):
        self.items = {}
        self.capacity = capacity

    def add(self, title, count):
        """
        (<название>, <количество>)  - увеличивает запас items
        :param title:
        :param count:
        :return:
        """
        self.items[title] = count


    def remove(self, title, count):
        """
        (<название>, <количество>) - уменьшает запас items
        :param title:
        :param count:
        :return:
        """
        try:
            del self.items[title]
        except Exception:
            print('Key not found')

    def get_free_space(self):
        """
        вернуть количество свободных мест
        :return:
        """
        return

    def get_items(self):
        """
        возвращает сожержание склада в словаре {товар: количество}
        :return:
        """
        return self.items

    def get_unique_items_count(self):
        """
        возвращает количество уникальных товаров.
        :return:
        """
        return


class Store:



if __name__ == '__main__':
    print(1)
