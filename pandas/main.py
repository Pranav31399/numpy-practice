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

#######################################################################################################################
# importing #
#######################################################################################################################

# importing csv, json

from pathlib import Path
# import pandas as pd
import sys

# show current working directory (where Python is looking for relative files)
print("cwd:", Path.cwd())

# build a path relative to this script's directory (recommended)
csv_path = Path(__file__).parent / "data.csv"
print("looking for:", csv_path.resolve())

if not csv_path.exists():
    sys.exit(f"File not found: {csv_path}. Place `data.csv` next to `pandas/main.py` or update the path.")

df = pd.read_csv(csv_path)
print(df.head())

# to print all
# print(df.to_string())

# json_path = Path(__file__).parent / "data.json"
# df=pd.read_json(json_path)
# print(df.to_string())

# selection by column
print(df["Name"])

# selection of multiple columns
print(df[["Name","Height","Weight"]].to_string())

# selection by row/s
# starting by 0
print(df.loc[0])

# add name to serve as index
df=pd.read_csv(csv_path,index_col="Name")
print(df.to_string())

print(df.loc["Pikachu"])

# columns you want to select
print(df.loc["Pikachu",["Height","Weight"]])

# you can use slicing as well using Name index (as in this case) or int index
# print(df.iloc[0:11:2, 0:3])

# pokemon=input("Enter a pokemon name: ")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")

#######################################################################################################################
# filtering #
#######################################################################################################################

tall_pokemon=df[df["Height"]>=2]
print(tall_pokemon)

#######################################################################################################################
# aggregate functions #
#######################################################################################################################

# whole dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

# single column
print(df["Height"].mean(numeric_only=True))

# group by
group=df.groupby("Type1")

# getting the mean of each group type1
print(group["Height"].mean())

#######################################################################################################################
# data cleaning #
#######################################################################################################################

# drop irrevalent columns
df=df.drop(columns=["Legendary","No"])
print(df)

# handle missing data
# drop any row which misses a value
# df=df.dropna(subset=["Type2"])
# print(df.to_string())

# replace n/a values with None
df=df.fillna({"Type2":"None"})
print(df)

# fix any inconsistent values
df["Type1"]=df["Type1"].replace(
    {
        "Grass":"GRASS",
        "Fire":"FIRE"
    })
print(df.to_string())

# standardize text
df=pd.read_csv(csv_path)
df["Name"]=df["Name"].str.lower()
print(df)

# fix data type
df["Legendary"]=df["Legendary"].astype(int)
print(df)

# remove duplicate values
df=df.drop_duplicates()
print(df)



