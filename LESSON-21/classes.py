from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() >= count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name] = count
            print("Товар добавлен")
        else:
            if self.get_free_space() != 0:
                print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров")
            else:
                print(f"Товар не может быть добавлен, так как место закончилось")

    def remove(self, name, count):
        for key in self.items.keys():
            if name == key:
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Слишком мало {name}")
            else:
                print(f"{name.title()} - нет на складе")

    def get_item(self):
        return self.items

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 20
        self._limit = limit

    @property
    def get_item_limit(self):
        return self._limit

    def add(self, name, count):
        if self.get_unique_items_count() <= self._limit:
            super().add(name, count)
        else:
            print(f"Товар не может быть добавлен")


class Request:
    def __init__(self, user_str):
        data = self.get_data(user_str)

        self.from_ = data[4]
        self.to = data[6]
        self.amount = int(data[1])
        self.product = data[2]

    def get_data(self, user_str):
        return user_str.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'