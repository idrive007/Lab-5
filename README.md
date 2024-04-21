# Звіт з лабораторної роботи №5. Розбіжні модифікації.
> Виконала студентка групи ІКМ-М223в **Павленко Дарина**
### Мета: Рефакторінг коду з проблемою «Розбіжні модифікації».
### Завдання 1: Наданий код
    
    class Product:
        def __init__(self, name, price, type):
            self.name = name
            self.price = price
            self.type = type

    def search_product(self, query):
        # Пошук товару за запитом
        pass

    def display_product(self):
        # Відображення інформації про товар
        pass

    def order_product(self, quantity):
        # Замовлення товару
        pass

### Рішення

Проблема "Розбіжності модифікації" виникає, коли один клас змінюється у різних напрямках через різні причини. Це призводить до складності в підтримці та розширенні програмного коду. Щоб зменшити цю залежність і здійснити рефакторинг коду, в цьому випадку, можна використати підходи, такі як відокремлення класу, та відокремлення суперкласу. 

     class Product:
        def __init__(self, name, price, type):
            self.name = name
            self.price = price
            self.type = type

    class ProductSearch:
        def search_product(self, product_list, query):
            # Пошук товару за запитом в переданому списку товарів
            pass

    class ProductDisplay:
        def display_product(self, product):
            # Відображення інформації про товар
            pass

    class ProductOrder:
        def order_product(self, product, quantity):
            # Замовлення товару
            pass

Таким чином, клас Product залишився, але його методи були розділені в окремі класи, які відповідають за конкретні аспекти товару: пошук, відображення та замовлення. Це дозволяє кожному з цих класів змінюватися незалежно від інших, зменшуючи ризик розбіжних модифікацій.
