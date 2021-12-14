#!/usr/bin/python3

"""
This script introduces one of the methods how to calculate tax
out of revenue from selling crypto currencies.

Method:
FIFO - first in first out
- cost of sales for a sale is calculated against the price of the earliest purchase.
If this purchase isn't large enough to cover the sale, the rest of the sale
is calculated against the price of the second purchase and so on until all
sales of the year are matched with corresponding purchase's price.
- revenue for a sale is derived from the actual selling price
- profit/loss is defined by the difference between revenues and costs of sales
"""


def fifo_coin(all_purchases, all_sales):
    """
    This function calculates the total profit/loss of the year.
    First, it calculates sales revenue for every sale of the year.
    Then, it calculates cost of sales using purchase history. Cost of sales is calculated
    against the price of the earliest purchase. If this purchase doesn't have enough
    quantity to cover the sale, the remaining quantity of the sale is calculated against
    next purchase's price and so on until the total quantity of the sale is matched with
    corresponding purchase's price.
    After using all the quantity of a purchase for calculating cost of sales completely,
    the purchase is removed from list of purchases and the second purchase takes the
    first place in the list and its quantity will be used for calculation.
    :param all_purchases: list of all purchases of the year, must be sorted by date
    :param all_sales: list of all sales of the year, must be sorted by date
    :return: profit or loss, negative or positive float
    """
    profit_loss = 0
    for sale in all_sales:
        cost_of_sales = 0
        sales_revenue = sale['price'] * sale['quantity']

        while sale['quantity'] > 0:
            # sale is smaller that first purchase, sale consumed, purchase stays
            if sale['quantity'] < all_purchases[0]['quantity']:
                # calculating against the first element from the list
                cost_of_sales += all_purchases[0]['price'] * sale['quantity']
                # there is remaining quantity in first purchase
                all_purchases[0]['quantity'] = all_purchases[0]['quantity'] - sale['quantity']
                sale['quantity'] = 0
            # sale is larger or same as first purchase - purchase is consumed
            if sale['quantity'] >= all_purchases[0]['quantity']:
                # calculating against first element from the list
                cost_of_sales += all_purchases[0]['price'] * all_purchases[0]['quantity']
                # there is remaining quantity in sale for next iteration
                sale['quantity'] = sale['quantity'] - all_purchases[0]['quantity']
                # first element is removed, next iteration = next element
                del all_purchases[0]

        profit_loss += sales_revenue - cost_of_sales
    return profit_loss
