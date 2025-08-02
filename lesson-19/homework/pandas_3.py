#1.1
# a
import pandas as pd
df = pd.read_csv(r"C:\Users\user\Downloads\sales_data.csv")
df.head()
sum_df = df.groupby('Category')['Quantity'].sum()
print(sum_df)
# b 
average_price = df.groupby('Category')['Price'].mean()
average_price
# c
max = df.groupby('Category')['Quantity'].max() 
max
# 1.2 identify the top seling product d=based on the quantity it is sold
top_prod = df.groupby(['Category','Product'])['Quantity'].max().reset_index()
top_prod 
sort = top_prod.sort_values(['Category','Product'], ascending = [True,False])\
    .groupby('Category').first()
print('The top selling products per each category are:', sort)
# 1.3 date when highest total sales occured
df['Total_Sales'] = df['Quantity'] * df['Price']
ts = df.groupby('Date')['Total_Sales'].sum().reset_index()
sort_ts = ts.sort_values('Total_Sales', ascending = False)
top = sort_ts.iloc[0]['Date']

print('Date when highest total sales occured:', top)

# 2.1
df = pd.read_csv(r"C:\Users\user\Downloads\customer_orders.csv")
df
order_count = df.groupby('CustomerID',)['OrderID'].count().reset_index()
new_oc = order_count.rename(columns = {'OrderID':'OrderCount'}, inplace = True)
few_order_cust = order_count.loc[order_count['OrderCount']< 20]
few_order_cust
# 2.2
avg = df.groupby('CustomerID')['Price'].mean().reset_index()
rename = avg.rename(columns = {'Price':'Avg_price'}, inplace = True)
filtered = avg.loc[avg['Avg_price'] > 120]
filtered
#2.3
total = df.groupby('Product')[['Quantity','Price']].sum().reset_index()
filter_totals = total.loc[total['Quantity'] < 5]
filter_totals.head()
df = pd.read_csv(r"C:\Users\user\Downloads\customer_orders.csv")
df
