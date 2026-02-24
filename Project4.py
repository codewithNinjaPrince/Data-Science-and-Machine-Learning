import matplotlib.pyplot as plt
import numpy as np

salaries=np.random.normal(50000,10000,1000)

#Plot Histogram
plt.hist(salaries, bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary ($)")
plt.ylabel("Number of Employees")
plt.show()


# ANSWERS:-

# 1.The histogram shows a bell-shaped (normal) distribution.
# This indicates that salaries are symmetrically distributed around the average salary.

# 2 Yes.
# Most employees earn salaries close to $50,000, typically within the range of $40,000 to $60,000.
# Fewer employees earn extremely low or extremely high salaries.

# 3.The variation is moderate, not extreme.
# The spread of about $10,000 shows reasonable salary differences across roles and experience levels.
