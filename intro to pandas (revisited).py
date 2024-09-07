# Create a list named 'data' that contains the values from the .csv file

# data = ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n',
#         'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

# with open("weather_data.csv") as file:
#     data_file = file.readlines()
#     print(data_file)


""" Python has an in-built library for csv files, to access this 'import csv' as
 Python is used for data analysis. It has many methods """

# import csv

"""
reader() is a method belonging to csv libray.
"""
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)    # reader() is a method belonging to csv libray.
""" Retrieve all the temperatures in a list as integers """
# temperatures = []
# for each_row in data:
# if each_row[1] != "temp":
# temperatures.append(int(each_row[1]))
# print(temperatures)

"""
In order to use Pandas, it needs to be installed since it is NOT in-built
When using new  libraries always check out the documentation.

To use Pandas -> pandas.read_csv(name of file) which we can assign to a variable.

There are many use-cases in the brackets but the one that's necessary is the 
CSV file itself

# Pandas is separated into:
pandas.dataframe.method()   - Using the dataframe     - pandas.data.method()
series.method()     - Using the series    - data[colum].method() or data.column.method()

"""

import pandas

data = pandas.read_csv("weather_data.csv")
# type(data)   # Dataframe (Whole table)
# type(data["temp"])   # Series (column)

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# Method 1

average = data["temp"].mean()
# print(average)

# Method 2
# average = sum(temp_list) / len(temp_list)
# print(average)

# print max value
max_value = data.temp.max()
""" # Alternatively data["temp] """
# print(max_value)

""" Get the row of data from the dataframe. We code like data[data.column] because 
we're picking out a column from the dataframe, otherwise, we'd use Series structure 
"""
# data[data.column == "Monday"]
# print(temp_list)
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
# print(monday.temp) # monday's temp
# monday_temp = monday.temp
# print(monday.temp * 9/5 + 32)   # celsius to Fahrenheit

""" 
1. How to create a DataFrame
2. How to create a series

# x = pandas.DataFrame(data_dict_2)   # Use the DataFrame class
# print(x)
# data.to_csv("x")  

"""

# data_dict_2 = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# x = pandas.DataFrame(data_dict_2)   # Use the DataFrame class
# print(x)
# data.to_csv("x")                      # Convert to CSV
#
