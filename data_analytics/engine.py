import matplotlib.pyplot as plt
from column_sets import ColumnSets
from adapter import *

def run(path):
    budget_df = load_excel_file(path+'/resources/data.xlsx')
    # plot_columns(budget_df, ColumnSets.BUDGET_ALL)
    plot_columns(budget_df, ColumnSets.BUDGET_STD)
    save_as_pickle(budget_df, path+'/resources')

def plot_columns(df, columns):
    df[columns].plot(x='Date')
    plt.show()