import csv
import pandas

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for each_row in data:
        if each_row[1] != "temp":
            temperatures.append(int(each_row[1]))
    print(temperatures)

# dataframe = name of csv file

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()

# If the temp is the highest, retrieve the row
print(data[data["temp"] == data["temp"].max()])




