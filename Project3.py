import matplotlib.pyplot as plt


months = ["January", "February", "March", "April"]
attendance = [85, 90, 95, 88]


plt.plot(months, attendance, marker='o', linestyle='-', color='blue')

plt.xlabel("Month")
plt.ylabel("Average Student Attendance")
plt.title("Monthly Student Attendance Trend")


plt.grid(True)

plt.show()


# ANSWERS:-
# 1.March had the highest attendance with 95 students on average.

# 2.Attendance increased from January to March:
# January → 85
# February → 90
# March → 95
# but there was a drop in April to 88, so attendance did not increase steadily throughout.

# 3.there was an increase in the trend initially, followed by a decline in April.
