from operator import index

import pandas as pd

# series - 1d labelled array (can hold any data type)
# dataframes - 2d labelled column, similar to excel spreadsheet
print(pd.__version__)

#######################################################################################################################
# series #
#######################################################################################################################

data=[100,102,104]
# converting data into series
series=pd.Series(data)
print(series)
# 0    100
# 1    102
# 2    104
# dtype: int64

series=pd.Series(data,index=["a","b","c"])
print(series)
# a    100
# b    102
# c    104
# dtype: int64

# return a value where label is a
print(series.loc["a"])
# updating
series.loc["c"]=200
print(series)

# we can also locate using position
print(series.iloc[0])

print(series[series>=200])

calories={
    "day1":1750,
    "day2":2100,
    "day3": 1700
}

series=pd.Series(calories)
print(series)
# day1    1750
# day2    2100
# day3    1700
# dtype: int64

data={
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30,35,50]
}

#######################################################################################################################
# dataframe #
#######################################################################################################################

# creating dataframe
df=pd.DataFrame(data)
print(df)
#         Name  Age
# 0  Spongebob   30
# 1    Patrick   35
# 2  Squidward   50

df=pd.DataFrame(data,index=["employee1","employee2","employee3"])
print(df)
#                 Name  Age
# employee1  Spongebob   30
# employee2    Patrick   35
# employee3  Squidward   50

print(df.loc["employee1"])
print(df.iloc[1])

# add a new column
df["Job"]=["Cook", "N/A","Cashier"]
print(df)

# add new row
# new_row=pd.DataFrame(
#     [
#         {
#             "Name":"Sandy",
#             "Age":28,
#             "Job":"Engineer"
#         }
#     ],index=["employee4"]
# )
#
# df=pd.concat([df,new_row])
# print(df)
#                 Name  Age       Job
# employee1  Spongebob   30      Cook
# employee2    Patrick   35       N/A
# employee3  Squidward   50   Cashier
# employee4      Sandy   28  Engineer

# add new row
new_rows=pd.DataFrame(
    [
        {
            "Name":"Sandy",
            "Age":28,
            "Job":"Engineer"
        },
        {
            "Name":"Eugene",
            "Age":60,
            "Job":"Manager"
        }
    ],index=["employee4","employee5"]
)

df=pd.concat([df,new_rows])
print(df)





