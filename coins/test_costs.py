#!/usr/bin/python3

import costs


def classify_transaction(transaction, all_purchases, all_sales):
    """
    This function classifies if a transaction is a purchase or a sale
    :param transaction: transaction with currency, dictionary
    :param all_purchases: list of purchases
    :param all_sales: list of sales
    :return: both lists modified - all year of purchases and all year of sales
    """
    if transaction['type'] == 'buying':
        all_purchases.append(transaction)
    elif transaction['type'] == 'prodej':
        all_sales.append(transaction)


# TEST CASE 1
transaction1 = {'type': 'buying', 'date': '1.1.2021', 'currency': 'ETH', 'quantity': 0.8,
                'price': 1000.0, 'value': None}
transaction1['value'] = transaction1['price'] * transaction1['quantity']

transaction2 = {'type': 'buying', 'date': '1.2.2021', 'currency': 'ETH', 'quantity': 0.5,
                'price': 2000.0, 'value': None}
transaction2['value'] = transaction2['price'] * transaction2['quantity']

transaction3 = {'type': 'prodej', 'date': '1.3.2021', 'currency': 'ETH', 'quantity': 0.3,
                'price': 3000.0, 'value': None}
transaction3['value'] = transaction3['price'] * transaction3['quantity']

transaction4 = {'type': 'prodej', 'date': '1.4.2021', 'currency': 'ETH', 'quantity': 0.9,
                'price': 4000.0, 'value': None}
transaction4['value'] = transaction4['price'] * transaction4['quantity']

purchases = list()
sales = list()
classify_transaction(transaction1, purchases, sales)
classify_transaction(transaction2, purchases, sales)
classify_transaction(transaction3, purchases, sales)
classify_transaction(transaction4, purchases, sales)


def test_average_coin_price():
    assert costs.average_coin_value(purchases) == 1385


def test_average_costs():
    assert costs.average_costs(sales, purchases) == 2838

# TEST CASE 2
buying = {'type': 'buying', 'date': '1.6.2021', 'currency': 'ETH', 'quantity': 0.1,
          'price': 1385.0, 'value': None}
buying['value'] = buying['price'] * buying['quantity']

buying2 = {'type': 'buying', 'date': '1.7.2021', 'currency': 'ETH', 'quantity': 0.5,
           'price': 3000.0, 'value': None}
buying2['value'] = buying2['price'] * buying2['quantity']

purse = list()
purse.append(buying)
purse.append(buying2)


def test_average_coin_price2():
    assert costs.average_coin_value(purse) == 2731
