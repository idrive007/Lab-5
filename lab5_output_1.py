#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

