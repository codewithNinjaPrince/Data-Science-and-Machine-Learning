import pandas as pd


#  Create Dataset

data = {
    "Employee": ["Amit", "Priya", "Rahul", "Sneha", "Arjun", "Meera",
                 "Karan", "Anjali", "Vikram", "Pooja"],
    "Department": ["Sales", "HR", "IT", "Finance", "Sales", "IT",
                   "HR", "Finance", "Sales", "IT"],
    "Quarter": ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2",
                "Q3", "Q3", "Q4", "Q4"],
    "Score": [92, 85, 88, 91, 95, 89, 87, 93, 90, 96]
}

df = pd.DataFrame(data)

print(" Employee Performance Dataset")

print(df)

print("Exceptional Performers (Score > 90)")


exceptional = df[df["Score"] > 90]
print(exceptional)

print(" Sales Department Records")


sales_dept = df[df["Department"] == "Sales"]
print(sales_dept)


print(" Overall Performance Ranking (High to Low)")


ranked = df.sort_values(by="Score", ascending=False)
print(ranked)



print(" Department-wise Ranking")


dept_ranking = df.sort_values(by=["Department", "Score"], ascending=[True, False])
print(dept_ranking)


print(" Average Score per Department")


dept_avg = df.groupby("Department")["Score"].mean()
print(dept_avg)


print(" Maximum Score per Quarter")


quarter_max = df.groupby("Quarter")["Score"].max()
print(quarter_max)

top_performers = df.loc[df.groupby("Department")["Score"].idxmax()]
print(top_performers)

print(" Department Score Statistics")


dept_stats = df.groupby("Department")["Score"].agg(["mean", "max", "min", "count"])
print(dept_stats)
