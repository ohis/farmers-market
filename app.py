"""Farmer's market basket app"""
import copy

PRODUCTS = {
    'CH1': {
        'code': 'CH1',
        'name': 'Chai',
        'price': 311
    },
    'AP1': {
        'code': 'AP1',
        'name': 'Apples',
        'price': 600
    },
    'CF1': {
        'code': 'CF1',
        'name': 'Coffee',
        'price': 1123
    },
    'MK1': {
        'code': 'MK1',
        'name': 'Milk',
        'price': 475
    },
    'OM1': {
        'code': 'OM1',
        'name': 'Oatmeal',
        'price': 369
    }
}

class Basket(object):
    """Basket class"""
    def __init__(self):
        self.items = []
        # Deal toggles that are limited to one
        self.chmk = False
        self.apom = False
        # Running tally of items added
        self.item_counter = {
            'CH1': 0,
            'AP1': 0,
            'CF1': 0,
            'MK1': 0,
            'OM1': 0
        }
    def add(self, item):
        """Add item to basket list"""
        try:
            new_item = copy.deepcopy(PRODUCTS[item])
            self.items.append(new_item)
            self.item_counter[new_item['code']] += 1
            self.discount()
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
        inv_display = 'Item\t\t\t\tPrice\n----\t\t\t\t-----\n'
        for item in self.items:
            item_price = float(item['price']) / 100
            inv_display += str(item['code']) + '\t\t\t\t' + '{0:.2f}'.format(item_price) + '\n'
            if 'promotion' in item:
                item_discount = float(item['discount']) / 100
                inv_display += '\t\t' + str(item['promotion']) + '\t       ' + '{0:.2f}'.format(item_discount) + '\n' #pylint: disable=line-too-long
        inv_value = float(self.value()) / 100
        inv_display += '-------------------------------------\n\t\t\t\t' + '{0:.2f}'.format(inv_value) #pylint: disable=line-too-long
        return inv_display
    def discount(self): #pylint: disable=too-many-branches
        """Apply discounts to items in basket"""
        if self.item_counter['AP1'] >= 3:
            for item in self.items:
                if item['code'] == 'AP1':
                    item['promotion'] = 'APPL'
                    item['discount'] = -150
        if self.item_counter['CF1'] >= 2:
            cf1_count = self.item_counter['CF1']
            discount_counter = ((cf1_count - cf1_count % 2) / 2)
            if discount_counter >= 1:
                for item in self.items:
                    if item['code'] == 'CF1' and discount_counter >= 1:
                        item['promotion'] = 'BOGO'
                        item['discount'] = -1123
                        discount_counter -= 1
                    if discount_counter < 1:
                        break
        if self.item_counter['CH1'] > 0 and self.item_counter['MK1'] > 0 and self.chmk is False:
            for item in self.items:
                if item['code'] == 'MK1':
                    item['promotion'] = 'CHMK'
                    item['discount'] = -475
                    self.chmk = True
                if self.chmk:
                    break
        if self.item_counter['OM1'] > 0 and self.item_counter['AP1'] > 0 and self.apom is False:
            for item in self.items:
                if item['code'] == 'AP1':
                    item['promotion'] = 'APOM'
                    item['discount'] = -item['price'] / 2
                    self.apom = True
                if self.apom:
                    break
    def value(self):
        """Return the value of all items"""
        basket_value = 0
        for item in self.items:
            basket_value += item['price']
            if 'discount' in item:
                basket_value += item['discount']
        return basket_value
    def find(self, code):
        """Looks for item with matching code in basket"""
        for index, item in enumerate(self.items):
            if item['code'] == code:
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
            print user_basket.show()
        elif user_input == 'add':
            user_add_input = raw_input('Add an item: ')
            user_basket.add(user_add_input)
        elif user_input == 'remove':
            user_remove_input = raw_input('Remove an item: ')
            user_basket.remove(user_remove_input)
        else:
            print 'Not a valid command. Try again.'

if __name__ == '__main__':
    main()
