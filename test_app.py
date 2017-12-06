"""Unit tests for app.py"""
import pytest #pylint: disable=unused-import
import app

def test_basket_add():
    """Test inserting items into basket"""
    items = ['CH1', 'MK1']
    basket = app.Basket()
    basket.add(items)
    assert basket.items == items

def test_basket_show():
    """Test basket inventory display"""
    items = ['CH1', 'AP1']
    basket = app.Basket()
    basket.add(items)
    expected_display = 'Item\t\t\t\tPrice\n----\t\t\t\t-----\nCH1\t\t\t\t3.11\nAP1\t\t\t\t6.00\n-------------------------------------\n\t\t\t\t9.11' #pylint: disable=line-too-long
    assert basket.show == expected_display

def test_basket_value():
    """Test expected price of simple basket"""
    items = ['CH1', 'AP1']
    basket = app.Basket()
    basket.add(items)
    expected_value = 3.11 + 6
    assert basket.value == expected_value

def test_basket_value_bogo():
    """Test expected price of basket: BOGO discount"""
    items = ['CF1', 'CF1', 'CF1', 'CF1', 'CF1']
    basket = app.Basket()
    basket.add(items)
    expected_value = (11.23 * (len(items) - len(items) % 2) / 2) + (len(items) % 2) * 11.23
    assert basket.value == expected_value

def test_basket_value_appl():
    """Test expected price of basket: BOGO discount"""
    items = ['AP1', 'AP1', 'AP1', 'AP1']
    basket = app.Basket()
    basket.add(items)
    expected_value = (6 - 1.5) * len(items)
    assert basket.value == expected_value

def test_basket_value_chmk():
    """Test expected price of basket: CHMK discount"""
    items = ['CH1', 'MK1', 'CH1', 'CH1', 'MK1']
    basket = app.Basket()
    basket.add(items)
    expected_value = 3.11 * 3 + 4.75 * 0 + 4.75
    assert basket.value == expected_value

def test_basket_value_apom():
    """Test expected price of basket: APOM discount"""
    items = ['OM1', 'AP1', 'AP1']
    basket = app.Basket()
    basket.add(items)
    expected_value = 3.69 + 6 + 6 / 2
    assert basket.value == expected_value