'''
Without data validation, this code defines a simple Product class with attributes for id, name, description, price, and quantity.models.py
'''

class Product:
    id: int
    name: str
    description: str
    price: float
    quantity: int
    
    def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity