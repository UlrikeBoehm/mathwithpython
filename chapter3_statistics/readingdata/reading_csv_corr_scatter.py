# data based on:
# https://www.google.com/trends/correlate/search?e=summer&e=swimming+lessons&t=weekly&p=us

import matplotlib.pyplot as plt
import csv

def read_csv(filename):

    with open(filename) as f:

        reader =csv.reader(f)
        next(reader)

        summer = []
        highest_correlated = []

        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))

    return summer, highest_correlated

def find_corr_x_y(x, y):
    n = len(x)

    # Find the sum of the products
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi * yi)

    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    x_square = []
    for xi in x:
        x_square.append(xi ** 2)
    # Find the sum
    x_square_sum = sum(x_square)

    y_square = []
    for yi in y:
        y_square.append(yi ** 2)
    # Find the sum
    y_square_sum = sum(y_square)

    # Use formula to calculate correlation
    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator_term1 = n * x_square_sum - squared_sum_x
    denominator_term2 = n * y_square_sum - squared_sum_y
    denominator = (denominator_term1 * denominator_term2) ** 0.5
    correlation = numerator / denominator

    return correlation

def scatter_plot(x,y):
    plt.scatter(x,y)
    plt.xlabel('summer')
    plt.ylabel('swimming lessons')
    plt.show()

if __name__ == '__main__':
    summer, highest_correlated = read_csv('correlate-summer.csv')
    corr = find_corr_x_y(summer, highest_correlated)
    print('Highest correlation: {0}' .format(corr))
    scatter_plot(summer, highest_correlated)

