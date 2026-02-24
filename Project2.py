import pandas as pd
#  TELECOM DATASET

telecom = pd.read_csv("telecom_churn.csv")

print("Telecom Head:\n", telecom.head())
print("Shape:", telecom.shape)
print("\nInfo:")
print(telecom.info())
print("\nDescription:\n", telecom.describe())
print("\nMissing Values:\n", telecom.isnull().sum())

# Handle Missing Values (Using fillna)
telecom.fillna(telecom.mean(numeric_only=True), inplace=True)

# Sort by Tenure
if "Tenure_Months" in telecom.columns:
    sorted_telecom = telecom.sort_values(by="Tenure_Months")
    print("\nSorted Telecom Data:\n", sorted_telecom.head())


#  EMPLOYEE ATTRITION DATASET

employee = pd.read_csv("employee_attrition.csv")

print("\nEmployee Head:\n", employee.head())
print("Shape:", employee.shape)
print("\nInfo:")
print(employee.info())
print("\nDescription:\n", employee.describe())
print("\nMissing Values:\n", employee.isnull().sum())

# Handle Missing Values
employee.fillna(employee.mean(numeric_only=True), inplace=True)

# Rename Column (Only if exists)
if "Employee_ID" in employee.columns:
    employee.rename(columns={"Employee_ID": "Emp_ID"}, inplace=True)

# Sort by Monthly Income
if "Monthly_Income" in employee.columns:
    sorted_employee = employee.sort_values(by="Monthly_Income")
    print("\nSorted Employee Data:\n", sorted_employee.head())


 # SALES / DATA1 DATASET

data = pd.read_csv("data1.csv")

print("\nSales Data Head:\n", data.head())
print("Shape:", data.shape)
print("\nInfo:")
print(data.info())
print("\nDescription:\n", data.describe())
print("\nMissing Values:\n", data.isnull().sum())

# Handle Missing Values
data.fillna(data.mean(numeric_only=True), inplace=True)

# Rename Column
if "Employee_ID" in data.columns:
    data.rename(columns={"Employee_ID": "Emp_ID"}, inplace=True)

# Sort by Region 
if "Region" in data.columns:
    sorted_data = data.sort_values(by="Region")
    print("\nSorted Sales Data:\n", sorted_data.head())
