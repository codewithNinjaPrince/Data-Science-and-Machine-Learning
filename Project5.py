import numpy as np
import pandas as pd

#load Dataset
customer=pd.read_csv("Customers1.csv")
support=pd.read_csv("support1.csv")
sales=pd.read_csv("Sales1.csv")

# Inspect Elements
print("\nCustomers Info:")
print(customer.info())
print("\nSales Info:")
print(sales.info())
print("\nSupport Info:")
print(support.info())

#Handle Missing values
customer["Age"].fillna(customer["Age"].median(),inplace=True)

#Rename Columns for clarity
customer.rename(columns={"CustomerID":"Customer_ID"},inplace=True)
sales.rename(columns={"CustomerID":"Customer_ID"},inplace=True)
support.rename(columns={"CustomerID":"Customer_ID"},inplace=True)

# Numerical Operations (Numpy integration)

#Apply 10 % discount on product prices
sales["DiscountedPrice"]=sales["Price"]*0.9
print(sales)

#Compute revenue per order
sales["Revenue"]=sales["Quantity"]*sales["Price"]
print(sales)


#Extract Orders Places in April 2023
april_orders=sales[sales["OrderDate"].str.startswith("2023-04")]
print("\nAprilOrders:\n",april_orders)

#Slice first 5 rows of sales
print("\nFirst 5 sales Records:\n",sales.head())


#Customer from north region
north_customers=customer[customer["Region"]=="North"]
print(north_customers)

#Order with revenue>50000
high_value_orders=sales[sales["Revenue"]>50000]
print(high_value_orders)


#Sort customer by Signup Date
sorted_customers=customer.sort_values(by="SignupDate")
print(sorted_customers)

#Sort values by revenue descending
sorted_Sales=sales.sort_values(by="Revenue", ascending=False)
print(sorted_Sales)


#Average revenue per prodcut
avg_revenue_product=sales.groupby("Product")["Revenue"].mean()
print(avg_revenue_product)

# Average resolution time per issue type
avg_resolution_issue = support.groupby("IssueType")["ResolutionTime"].mean()

print("\nAverage Revenue per Product:\n", avg_revenue_product)
print("\nAverage Resolution Time per Issue Type:\n", avg_resolution_issue)

#Merge Datasets
merged_data=sales.merge(customer,on="Customer_ID").merge(support,on="Customer_ID")
print(merged_data)


#Customer lifetime value(CLV)
clv=sales.groupby("Customer_ID")["Revenue"].sum().reset_index()
clv.rename(columns={"Revenue":"CustomerLifetimeValue"},inplace=True)

#Merge Clv Back into customers
customer=customer.merge(clv,on="Customer_ID",how="left")
print(customer)


#Export Cleaned Dataset
merged_data.to_csv("Cleaned_Data.csv",index=False)
print("\nCleaned dataset exported to Cleaned_Data.csv")
