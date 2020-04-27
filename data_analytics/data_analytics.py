import pandas as pd
import matplotlib.pyplot as plt
import re


def run(path):
    budget_df = loadExcelFile(path+'/resources/data.xlsx', ['Date', 'Cost', 'Checking', 'Savings', 'Total', 'Total Income Brought In(Pre Tax, Spendings)'])
    print(budget_df.filename)
    budget_df.plot(x='Date')
    plt.show()
    saveAsPickle(budget_df, path+'/resources')

def loadExcelFile(address, colArr):
    df = pd.read_excel(address, usecols=colArr, parse_dates=['Date'])
    filename = re.search(r"(?<=/)(\w|_)+(?=\.)", address).group()
    df.filename = filename
    return df 

def saveAsPickle(df, address):
    df.to_pickle(address + '/' + df.filename + ".p")
