#!/usr/bin/python3

import fifo


# TEST CASE 1
transaction1 = {'type': 'buy', 'date': '1.1.2021', 'currency': 'ETH', 'quantity': 0.8, 'price': 1000.0,
              'value': None}
transaction1['value'] = transaction1['price'] * transaction1['quantity']

transaction2 = {'type': 'buy', 'date': '1.2.2021', 'currency': 'ETH', 'quantity': 0.5, 'price': 2000.0,
              'value': None}
transaction2['value'] = transaction2['price'] * transaction2['quantity']

transaction3 = {'type': 'sale', 'date': '1.3.2021', 'currency': 'ETH', 'quantity': 0.3, 'price': 3000.0,
              'value': None}
transaction3['value'] = transaction3['price'] * transaction3['quantity']

transaction4 = {'type': 'sale', 'date': '1.4.2021', 'currency': 'ETH', 'quantity': 0.9, 'price': 4000.0,
              'value': None}
transaction4['value'] = transaction4['price'] * transaction4['quantity']

purchases = list()
sales = list()

def classify_transaction(transaction, all_purchases, all_sales):
    """
    This function classifies if a transaction is a purchase or a sale
    :param transaction: transaction with currency, dictionary
    :param all_purchases: list of purchases
    :param all_sales: list of sales
    :return: both lists modified - all year of purchases and all year of sales
    """
    if transaction['type'] == 'buy':
        all_purchases.append(transaction)
    elif transaction['type'] == 'sale':
        all_sales.append(transaction)

classify_transaction(transaction1, purchases, sales)
classify_transaction(transaction2, purchases, sales)
classify_transaction(transaction3, purchases, sales)
classify_transaction(transaction4, purchases, sales)

def test_fifo_coin():
    assert fifo.fifo_coin(purchases, sales) == 2900.0

