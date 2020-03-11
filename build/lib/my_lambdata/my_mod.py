# my_lambdata/my_mod.py

# pull functions out of here.

import pandas as pd
import numpy as np


# The code in here would break our package if it was outside this
# "super weird Python convention".
if __name__ == "__main__":
    # only run this code if invoked from the command line
    # not if imported from another module
    print('Hello World.')
    x = 100
    print('x: ', x)
    print('Enlarged x: ', enlarge(x))
    pass

# Needs Pandas
def list_to_new_column(list, df, column_name):
    '''
    Param list is a list.
    Param df is a df.
    Function will take the list, turn it into a series and add it to
    the dataframe as a new column
    '''
    df = df
    list = list

    series = pd.Series(list)

    df[column_name] = series
    # df.append(series, ignore_index=True)

    return df

# needs Numpy and Pandas
def outlier_remover(df, column):
    '''
    Function finds values > 1.5*interquartile range and removes them
    from the df.

    Value passed should be in the form of df['column_name']
    '''
    df = df

    x = np.percentile(column, 0.25)
    y = np.percentile(column, 0.75)

    df = df[(column <= (y + 1.5(y - x))) & 
    (column >= (x - 1.5(y - x)))]

    return df


def enlarge(n):
    '''
    Param n is a number.
    Function will enlarge the number.
    '''
    return n * 100
