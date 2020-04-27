import pandas as pd
import matplotlib.pyplot as plt

budget_df = pd.read_excel("resources/budget_data.xlsx", usecols=['Date', 'Cost', 'Checking', 'Savings', 'Total'], parse_dates=['Date'])
# budget_df.set_index('Date',inplace=True)
budget_df.plot(x='Date')
plt.show()
print(budget_df)

# pd.set_option("display.max_rows", None)
# print(budget_df[['Date']])