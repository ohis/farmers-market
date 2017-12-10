"""Unit tests for app.py"""
import pytest #pylint: disable=unused-import
import app

def test_basket_add():
    """Test inserting items into basket"""
    items = ['CH1', 'MK1']
    basket = start_basket(items)
    assert len(basket.items) == len(items)

def test_basket_add_sensitivity():
    """Test sensitivity on inserting items into basket"""
    items = ['ch1', 'ch', 'aP1', 'ap']
    basket = start_basket(items)
    assert len(basket.items) == 2

def test_basket_remove():
    """Test removing items from basket"""
    items = ['CH1', 'AP1', 'AP1']
    basket = start_basket(items)
    basket.remove('AP1')
    assert len(basket.items) == len(items) - 1

def test_basket_show():
    """Test basket inventory display"""
    basket = start_basket(['CH1', 'AP1'])
    expected_display = ('Item\t\t\t\tPrice\n----\t\t\t\t-----\n'
                        'CH1\t\t\t\t3.11\nAP1\t\t\t\t6.00\n'
                        '-------------------------------------\n'
                        '\t\t\t\t9.11')
    assert basket.show() == expected_display

def test_basket_show_discount():
    """Test basket inventory display with discounts"""
    basket = start_basket(['CH1', 'AP1', 'AP1', 'AP1', 'MK1'])
    expected_display = ('Item\t\t\t\tPrice\n----\t\t\t\t-----\n'
                        'CH1\t\t\t\t3.11\nAP1\t\t\t\t6.00\n'
                        '\t\tAPPL\t       -1.50\nAP1\t\t\t\t6.00\n'
                        '\t\tAPPL\t       -1.50\nAP1\t\t\t\t6.00\n'
                        '\t\tAPPL\t       -1.50\nMK1\t\t\t\t4.75\n'
                        '\t\tCHMK\t       -4.75\n-------------------------------------\n'
                        '\t\t\t\t16.61')
    assert basket.show() == expected_display

def test_basket_value():
    """Test expected price of simple basket"""
    basket = start_basket(['CH1', 'AP1'])
    expected_value = 311 + 600
    assert basket.value() == expected_value

def test_basket_value_spec0():
    """Test given sample basket"""
    basket = start_basket(['CH1', 'AP1', 'CF1', 'MK1'])
    assert basket.value() == 2034

def test_basket_value_spec1():
    """Test given sample basket"""
    basket = start_basket(['MK1', 'AP1'])
    assert basket.value() == 1075

def test_basket_value_spec2():
    """Test given sample basket"""
    basket = start_basket(['CF1', 'CF1'])
    assert basket.value() == 1123

def test_basket_value_spec3():
    """Test given sample basket"""
    basket = start_basket(['AP1', 'AP1', 'CH1', 'AP1'])
    assert basket.value() == 1661

def test_basket_value_bogo():
    """Test expected price of basket: BOGO discount"""
    items = ['CF1', 'CF1', 'CF1', 'CF1', 'CF1']
    basket = start_basket(items)
    expected_value = (1123 * (len(items) - len(items) % 2) / 2) + (len(items) % 2) * 1123
    assert basket.value() == expected_value

def test_basket_value_appl():
    """Test expected price of basket: BOGO discount"""
    items = ['AP1', 'AP1', 'AP1', 'AP1']
    basket = start_basket(items)
    expected_value = (600 - 150) * len(items)
    assert basket.value() == expected_value

def test_basket_value_chmk():
    """Test expected price of basket: CHMK discount"""
    basket = start_basket(['CH1', 'MK1', 'CH1', 'CH1', 'MK1'])
    expected_value = 311 * 3 + 475 * 0 + 475
    assert basket.value() == expected_value

def test_basket_value_apom():
    """Test expected price of basket: APOM discount"""
    basket = start_basket(['OM1', 'AP1', 'AP1'])
    expected_value = 369 + 600 + 600 / 2
    assert basket.value() == expected_value

def test_basket_removed_discount():
    """Test expected price of basket with removing discount"""
    basket = start_basket(['AP1', 'AP1', 'AP1'])
    basket.remove('AP1')
    expected_value = 600 * 2
    assert basket.value() == expected_value

def start_basket(items):
    """Initialize basket with items"""
    basket = app.Basket()
    for item in items:
        basket.add(item)
    return basket
