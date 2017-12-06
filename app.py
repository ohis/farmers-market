"""Farmer's market basket app"""
PRODUCTS = [
    {
        'code': 'CH1',
        'name': 'Chai',
        'price': 3.11
    },
    {
        'code': 'AP1',
        'name': 'Apples',
        'price': 6
    },
    {
        'code': 'CF1',
        'name': 'Coffee',
        'price': 11.23
    },
    {
        'code': 'MK1',
        'name': 'Milk',
        'price': 4.75
    },
    {
        'code': 'OM1',
        'name': 'Oatmeal',
        'price': 3.69
    }
]

class Basket(object):
    """Basket class"""
    def __init__(self):
        self.items = []
    def add(self, item):
        """Add item to basket list"""
        pass
    def show(self):
        """Returns inventory display of basket"""
        pass
    def value(self):
        """Return the value of all items"""
        pass
