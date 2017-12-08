"""Farmer's market basket app"""
PRODUCTS = {
    'CH1': {
        'code': 'CH1',
        'name': 'Chai',
        'price': 3.11
    },
    'AP1': {
        'code': 'AP1',
        'name': 'Apples',
        'price': 6
    },
    'CF1': {
        'code': 'CF1',
        'name': 'Coffee',
        'price': 11.23
    },
    'MK1': {
        'code': 'MK1',
        'name': 'Milk',
        'price': 4.75
    },
    'OM1': {
        'code': 'OM1',
        'name': 'Oatmeal',
        'price': 3.69
    }
}

class Basket(object):
    """Basket class"""
    def __init__(self):
        self.items = []
    def add(self, item):
        """Add item to basket list"""
        try:
            self.items.append(PRODUCTS[item])
        except KeyError:
            print "Not a valid item for sale!"
    def remove(self, item):
        """Remove item from basket list"""
        item_index = self.find(item)
        if item_index is not None:
            del self.items[item_index]
        else:
            print "Item was not found in basket."
    def show(self):
        """Returns inventory display of basket"""
        pass
    def value(self):
        """Return the value of all items"""
        pass
    def find(self, code):
        """Looks for item with matching code in basket"""
        for index, item in enumerate(self.items):
            if item['code'] == code:
                print index
                return index
        return None

def main():
    """Terminal runner"""
    print 'Welcome to the farmer\'s market. Enter items for purchase and see our deals.' #pylint: disable=line-too-long
    print '+--------------|--------------|---------+\n| Product Code |     Name     |  Price  |\n+--------------|--------------|---------+\n|     CH1      |   Chai       |  $3.11  |\n|     AP1      |   Apples     |  $6.00  |\n|     CF1      |   Coffee     | $11.23  |\n|     MK1      |   Milk       |  $4.75  |\n|     OM1      |   Oatmeal    |  $3.69  |\n+--------------|--------------|---------+' #pylint: disable=line-too-long
    print 'Commands: add, remove, inv, exit'
    running = True
    user_basket = Basket()
    while running:
        user_input = raw_input('Please enter a command: ')
        if user_input == 'exit':
            running = False
            print 'Exiting... Thank you and have a nice day.'
        elif user_input == 'inv':
            user_basket.show()
        elif user_input == 'add':
            user_add_input = raw_input('Add an item: ')
            user_basket.add(user_add_input)
            print user_basket.items
        elif user_input == 'remove':
            user_remove_input = raw_input('Remove an item: ')
            user_basket.remove(user_remove_input)
            print user_basket.items
        else:
            print 'Not a valid command. Try again.'

if __name__ == '__main__':
    main()
