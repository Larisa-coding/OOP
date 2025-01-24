class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

# Создание объектов классов Store
store1 = Store("Магазин №1", "ул. Ленина, 1")
store2 = Store("Магазин №2", "ул. Пушкина, 2")
store3 = Store("Магазин №3", "ул. Горького, 3")

# Добавление товаров
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("milk", 1.0)
store2.add_item("bread", 0.8)

store3.add_item("eggs", 1.2)
store3.add_item("cheese", 2.5)

# Тестирование методов на первом магазине
print("\nТестирование методов на 'Магазин №1':")
store1.add_item("pears", 0.6)
print(f"Цена на 'bananas': {store1.get_price('bananas')}")
store1.update_price("bananas", 0.85)
print(f"Новая цена на 'bananas': {store1.get_price('bananas')}")
store1.remove_item("apples")
print(f"Цена на 'apples': {store1.get_price('apples')}")