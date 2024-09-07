"""
TODO:

Create a new csv 'squirrel count' containing 3 columns; Fur & Color, Count.
How many grey, cinnamon, black squirrels - based on fur color column in 2018 file.
Take the table, build a new DataFrame to fill fur color and count.

1. Get hold of your Data, making relevant imports and finding the file to open.
2. Ideally, retrieve the column of all colors 'Primary Fur Colors' as int()
3. Create a new list called Colors, then append to that (to new colors).
4. Create a new dataframe consisting of 3 columns
5. Import the new list into the new table / dataframe
6. Create a new CSV

"""

import pandas
import csv

# Gray
# Black
# Cinnamon

data = pandas.read_csv("squirrel data analysis.csv")    # Use to read the CSV, now we have dataframe
gray = len(data[data["Primary Fur Color"] == "Gray"])      # find the column belonging to the data, from
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray)
print(black)
print(cinnamon)

data_dict = {
    "Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon]
}

new_data = pandas.DataFrame(data_dict)   # Use the DataFrame class, before turning into DataFrame it can be in dict
new_data.to_csv("new_data")
