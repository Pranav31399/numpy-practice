import  matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import pandas as pd
import sys

x=[2023,2024,2025,2026]
y=[15,25,30,20]

# figure 1
# plt.plot(x,y)
# plt.show()

# figure 2
# plt.plot(y)
# plt.show()

x=np.array([2023,2024,2025,2026])
y=np.array([15,25,30,20])
# plt.plot(x,y)
# plt.show()

#######################################################################################################################
# plot customization #
#######################################################################################################################

# figure 3
# plt.plot(x,y,
#          marker="*",
#          markersize=30,
#          markerfacecolor="cyan",
#          markeredgecolor="red",
#          linestyle="solid",
#          linewidth=4,
#          color="green")
# plt.show()

# figure 4
x=np.array([2023,2024,2025,2026])
y1=np.array([15,25,30,20])
y2=np.array([17,23,38,5])

plt.plot(x,y1,
         marker="*",
         markersize=30,
         markerfacecolor="cyan",
         markeredgecolor="red",
         linestyle="solid",
         linewidth=4,
         color="green")

line_style=dict(
         marker="*",
         markersize=30,
         markerfacecolor="cyan",
         markeredgecolor="red",
         linestyle="solid",
         linewidth=4,
         color="green"
)
plt.plot(x,y2,**line_style)
plt.show()

#######################################################################################################################
# plot customization: labels #
#######################################################################################################################

# figure 5
plt.title("Class size",
          fontsize=25,
          family="Arial",
          fontweight="bold",
          color="blue")

plt.xlabel("Year",
           fontsize=20,
           fontweight="bold",
           family="Arial",
           color="red")

plt.ylabel("Students",
           fontsize=20,
           fontweight="bold",
           family="Arial",
           color="red")

plt.tick_params(axis="both",
                colors="green")

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

#######################################################################################################################
# grid() = helps make plots easier to read by adding reference lines. #
#######################################################################################################################

# figure 6
x=[1,2,3,4,5]
y=[5,10,15,20,25]

# we will have grid lines in both axis
plt.grid()

#  just for y axis
plt.grid(axis="y",
         linewidth=2,
         color="lightgray",
         linestyle="dashdot")


plt.plot(x,y)
plt.show()

#######################################################################################################################
# bar chart = compare categories of data by representing each category with a bar #
#######################################################################################################################

# figure 7
categories=np.array(["Grains","Fruit","Vegetables","Proteins","Dairy","Sweets"])
values=np.array([4,3,2,5,3,1])

plt.bar(categories,values,color="skyblue")
# horizontal bar chart
# plt.barh(categories,values,color="skyblue")

plt.title("Daily consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()

#######################################################################################################################
# pie chart = circular chart divided into slices to show percentage
# of the total #
#######################################################################################################################

# figure 8
categories=["Freshmen","Sophomores","Juniors","Seniors"]
values=[300,250,275,225]
colors=["red","yellow","blue","green"]

plt.pie(values,labels=categories,
        autopct="%1.1f%%",
        colors=colors,
        explode=[0,0,0,0.1],
        shadow=True,
        startangle=90)
plt.title("College")
plt.show()

#######################################################################################################################
# scatter graph - shows the relationship between two variables #
# helps to identify a correlation(+, -, None) #
# Example: Study hours vs. test scores #
#######################################################################################################################

# figure 9
x1=np.array([0,1,1,2,3,4,5,6,7,7,8]) #Hours studied
y1=np.array([55,60,65,62,68,70,75,78,82,85,87]) #grades

x2=np.array([0,1,1,2,3,4,5,6,7,8]) #Hours studied
y2=np.array([50,58,65,70,72,78,83,88,90,92]) #grades

plt.scatter(x1,y1,
            color="skyblue",
            alpha=0.6,
            s=100,
            label="class A")
plt.scatter(x2,y2,
            color="red",
            alpha=0.6,
            s=100,
            label="class B")
plt.title("Test scores")
plt.xlabel("Hours Studies")
plt.ylabel("Grade")
plt.legend()
plt.show()

#######################################################################################################################
# histogram - a visual representation of the distribution of quantitative data #
# they group values into bins (intervals) #
# and counts how many fall in each range #
#######################################################################################################################

# figure 10
# loc = where most of the data is clustered, scale = std deviation
scores=np.random.normal(loc=80,scale=10,size=100)
# setting the boundary
scores=np.clip(scores,0,100)

plt.hist(scores,
         bins=10,
         color="lightgreen",
         edgecolor="black")
plt.title("Exam scores")
plt.xlabel("Score")
plt.ylabel("# of students")
plt.show()

#######################################################################################################################
# subplots #
# figure = the entire canvas #
# Ax = a single plot (subplot) #
#######################################################################################################################

# print(plt.subplots(2,2))
# (<Figure size 1280x960 with 4 Axes>, array([[<Axes: >, <Axes: >],
#        [<Axes: >, <Axes: >]], dtype=object))

# figure 11
x=np.array([1,2,3,4,5])

figure, axes=plt.subplots(2,2)
axes[0,0].plot(x,x*2,color="red")
axes[0,0].set_title("x*2")

axes[0,1].bar(x,x**2,color="blue")
axes[0,1].set_title("x**2")

axes[1,0].plot(x,x**3,color="green")
axes[1,0].set_title("x**3")

axes[1,1].plot(x,x**4,color="purple")
axes[1,1].set_title("x**4")

plt.tight_layout()
plt.show()

#######################################################################################################################
# matplotlib + pandas #
# figure = the entire canvas #
# Ax = a single plot (subplot) #
#######################################################################################################################

# figure 12
csv_path = Path(__file__).parent / "data.csv"
print("looking for:", csv_path.resolve())

if not csv_path.exists():
    sys.exit(f"File not found: {csv_path}. Place `data.csv` next to `pandas/main.py` or update the path.")

df = pd.read_csv(csv_path)
print(df.head())

# it will return the counts of each type1 like groupby
print(df["Type1"].value_counts(ascending=True))

type_count=df["Type1"].value_counts()

plt.barh(type_count.index,type_count.values,
         color="blue",
         edgecolor="black")
plt.title("# of pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()

