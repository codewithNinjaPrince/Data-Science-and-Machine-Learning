
import pandas as pd

telecom = pd.read_csv("/Users/ayush/Desktop/project/telecom_churn - Sheet1.csv")

telecom.head()
telecom.shape
telecom.info()
telecom.describe()
telecom.isnull().sum()
telecom.dropna(inplace=True)
telecom.rename(columns={"Customer_ID": "Cust_ID"}, inplace=True)
print(telecom)

telecom.fillna(telecom.mean(numeric_only=True), inplace=True)
print(telecom)

sorted_customers = telecom.sort_values(by="Tenure_Months")
print(sorted_customers)
