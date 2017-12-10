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
            new_item = copy.deepcopy(PRODUCTS[item.upper()])
            self.items.append(new_item)
            self.item_counter[new_item['code']] += 1
            self.discount()
        except KeyError:
            print "Not a valid item for sale!"
    def remove(self, item):
        """Remove item from basket list"""
        item_code = item.upper()
        item_index = self.find(item_code)
        if item_index is not None:
            del self.items[item_index]
            self.item_counter[item_code] -= 1
            self.discount()
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
                inv_display += ('\t\t' + str(item['promotion']) + '\t       '
                                + '{0:.2f}'.format(item_discount) + '\n')
        inv_value = float(self.value()) / 100
        inv_display += ('-------------------------------------\n'
                        '\t\t\t\t' + '{0:.2f}'.format(inv_value))
        return inv_display
    def discount(self):
        """Apply discounts to items in basket"""
        # Apply counter for BOGO discount before loop
        if self.item_counter['CF1'] >= 2:
            cf1_count = self.item_counter['CF1']
            bogo_counter = ((cf1_count - cf1_count % 2) / 2)
        else:
            bogo_counter = 0
        for item in self.items:
            # Remove discounts to have them reapplied in case items were removed
            if 'promotion' in item:
                item.pop('promotion', None)
                item.pop('discount', None)
                self.chmk = False
                self.apom = False
            if self.item_counter['AP1'] >= 3 and item['code'] == 'AP1':
                item['promotion'] = 'APPL'
                item['discount'] = -150
            if  item['code'] == 'CF1' and bogo_counter >= 1:
                item['promotion'] = 'BOGO'
                item['discount'] = -1123
                bogo_counter -= 1
            if self.item_counter['CH1'] > 0 and self.item_counter['MK1'] > 0 and self.chmk is False:
                if item['code'] == 'MK1':
                    item['promotion'] = 'CHMK'
                    item['discount'] = -475
                    self.chmk = True
            if self.item_counter['OM1'] > 0 and self.item_counter['AP1'] > 0 and self.apom is False:
                if item['code'] == 'AP1':
                    item['promotion'] = 'APOM'
                    item['discount'] = -item['price'] / 2
                    self.apom = True
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
    print ('Welcome to the farmer\'s market. Enter items for purchase and see our deals.\n'
           '+--------------|--------------|---------+\n'
           '| Product Code |     Name     |  Price  |\n'
           '+--------------|--------------|---------+\n'
           '|     CH1      |   Chai       |  $3.11  |\n'
           '|     AP1      |   Apples     |  $6.00  |\n'
           '|     CF1      |   Coffee     | $11.23  |\n'
           '|     MK1      |   Milk       |  $4.75  |\n'
           '|     OM1      |   Oatmeal    |  $3.69  |\n'
           '+--------------|--------------|---------+\n'
           'Commands: add, remove, inv, exit\n')
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
            add_toggle = True
            while add_toggle:
                user_add_input = raw_input('Add an item (enter "stop" to go back): ')
                if user_add_input == 'stop':
                    add_toggle = False
                # Specifically to allow checking of basket during adding
                elif user_add_input == 'inv':
                    print user_basket.show()
                else:
                    user_basket.add(user_add_input)
        elif user_input == 'remove':
            remove_toggle = True
            while remove_toggle:
                user_remove_input = raw_input('Remove an item (enter "stop" to go back): ')
                if user_remove_input == 'stop':
                    remove_toggle = False
                # Specifically to allow checking of basket during removing
                elif user_remove_input == 'inv':
                    print user_basket.show()
                else:
                    user_basket.remove(user_remove_input)
        else:
            print 'Not a valid command. Try again.'

if __name__ == '__main__':
    main()
