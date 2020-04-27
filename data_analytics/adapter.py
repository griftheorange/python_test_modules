import pandas as pd
import re

def load_excel_file(address):
    df = pd.read_excel(address, parse_dates=['Date'])
    filename = re.search(r"(?<=/)(\w|_)+(?=\.)", address).group()
    df.filename = filename
    return df 

def save_as_pickle(df, address):
    df.to_pickle(address + '/' + df.filename + ".p")