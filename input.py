
import pandas as pd


final = pd.read_csv('final.csv', sep=',', names=['mobile_number', 'current_type', 'best_type', 'rank', 'most',
                                                 'day_min_value', 'week_min_value', 'month_min_value',
                                                 'three_month_min_value', 'six_month_min_value', 'year_min_value',
                                                 'sh_min_value'])


def find_rec():

    number = input('Enter a Number\n')

    for row in range(1, len(final)):
        if final.iloc[row, 0] == number:
            print("best:")
            print(final.iloc[row, 2])
            print("daily best type:")
            print(final.iloc[row, 4])
            print("weekly best type:")
            print(final.iloc[row, 5])
            print("monthly best type:")
            print(final.iloc[row, 6])
            print("3month best type:")
            print(final.iloc[row, 7])
            print("6month best type:")
            print(final.iloc[row, 8])
            print("yearly best type:")
            print(final.iloc[row, 9])
            print("shegeftangiz best type:")
            print(final.iloc[row, 10])

find_rec()
