"""This module defines the function which creates a chart
using a table containing the data in form of csv file.

The chart will contain a line representating that
data in time and a line representing an average of
the data."""


import csv
import matplotlib.pyplot as plt


def chart_creation(csv_file):
    """The function makes a chart taking csv file
    and saves the chart.

    csv_file: it will always be kms.cvs created by main.py
    """
    x_date = list()
    y_distance = list()

    with open(csv_file, 'r') as csvfile:
        plots = list(csv.reader(csvfile, delimiter=','))
        # iteration from the second line because the first one
        # contains a description, not data
        for row in plots[1:]:
            x_date.append(row[0])
            y_distance.append(float(row[1]))

    y2_average = [sum(y_distance) / len(y_distance)] * len(x_date)

    plt.plot(x_date, y_distance, color='magenta', linewidth=2)
    plt.plot(x_date, y2_average, color='cyan', linestyle='dashed', linewidth=2, label='average')

    plt.title('Cycling record')
    plt.ylabel('Distance')
    plt.tick_params(axis='x', rotation=55, labelsize=6)
    plt.legend()
    #plt.show()
    plt.savefig('../../../../../chart.png')
