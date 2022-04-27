from classes import Shop, Store, Request

if __name__ == '__main__':
    shop = Shop()
    shop.add('вафли', 5)
    shop.add('огурцы', 5)
    shop.add('помидоры', 5)
    shop.add('чай', 5)
    store = Store()
    store.add('огурцы', 5)

    user_input = input("Введите запрос: \n")
    user_list = user_input.split(' ')
    try:
        user_list[1] = int(user_list[1])
    except ValueError:
        print("Ошибка! Введите число")

    if "доставить" not in user_list[0].lower() and "забрать" not in user_list[0].lower():
        print("Ошибка! Введите 'забрать/доставить'")
    elif ("магазин" and "склад") not in user_list[4].lower():
        print("Ошибка! Введите место назначения(магазин/склад)")
    else:
        r = Request(user_input)
        print(r)
        if "магазин" in r.from_:
            print("Доставка возможна только со склада")
        elif "склад" in r.from_:
            if r.product in store.get_item():
                if r.amount <= store.get_item()[r.product]:
                    print("Нужное количество есть на складе")
                    print("Курьер везет со склад в магазин")
                    if sum(shop.get_item().values()) + int(r.amount) < shop.capacity:
                        print(f"Курьер доставил {r.amount} {r.product} в магазин")
                        store.remove(r.product, r.amount)
                        shop.add(r.product, r.amount)
                    else:
                        print("В магазине недостаточно места")
                else:
                    print("На складе нехватает товара, попробуйте заказать меньше")
            else:
                print("Такого товара нет на складе")

        print("На складе хранится:")
        for key, value in store.items.items():
            print(key, value)

        print("В магазине хранится:")
        for key, value in shop.items.items():
            print(key, value)