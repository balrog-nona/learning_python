#!/usr/bin/python3

"""
This script introduces one of the methods how to calculate tax
out of revenue from selling crypto currencies.

Method:
Average costs
- average value of all the quantity hold at the time of the sale is part of the equation
of calculating costs of sales. Average value must be recalculated after every transaction.
- cost of sales for a sale is derived from average value of all the quantity
hold at the time of the sale and quantity which is being sold.
- revenue for a sale is derived from the actual selling price
- profit/loss is defined by the difference between revenues and costs of sales
"""


def average_coin_value(all_purchases):
    """
    This function takes the current state of coins and
    calculates their average value.
    :param all_purchases: list
    :return: int
    """
    sum_value = sum(purchase['value'] for purchase in all_purchases)
    sum_quantity = sum(purchase['quantity'] for purchase in all_purchases)
    average = sum_value / sum_quantity
    return round(average)


def average_costs(all_sales, all_purchases):
    """
    This function calculates the total profit/loss of the year.
    First, it calculates the average value of the coins hold at the time
    of selling.
    Then, for every sale it calculates sales revenue, cost of sales and profit
    or loss.
    :param all_sales: list of all sales of the year, must be sorted by date
    :param all_purchases: list of hold coins, will vary over the year
    :return: profit or loss, negative or positive float
    """
    profit_loss = 0
    average_value = average_coin_value(all_purchases)
    for sale in all_sales:
        sales_revenue = sale['price'] * sale['quantity']
        cost_of_sales = average_value * sale['quantity']
        profit_loss += sales_revenue - cost_of_sales
    return profit_loss
