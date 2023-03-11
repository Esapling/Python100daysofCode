# comma seperated values CSV
#
#with open("weather_data.csv", "r") as d_file:
#    weather_data = d_file.read().split()

# read returns string
# split makes them a list of items
#print(type(weather_data))
#print(weather_data)

#import csv
#temperatures = []
#with open("weather_data.csv", "r") as data_file:
#   csv_format = csv.reader(data_file)
#    #print(type(csv_format))
#   for row in csv_format:
#       if row[1] != "temp":
#           temperatures.append(int(row[1]))
#   print(temperatures)
#print(data)
#print(data["temp"])

#import pandas
#data = pandas.read_csv("weather_data.csv")
#data_dict = data.to_dict()
#print(data_dict)
#temp_list = data["temp"].to_list()
#print(temp_list)

#avg_temp = data.mean(axis=1)
""" FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; 
in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
avg_temp = data.mean(axis=1)
"""
#avg_temp = data["temp"].mean(numeric_only=True)
#print(avg_temp)
#print(max_temp)
#print(data["condition"])
#print(data.condition)
#max_temp = data["temp"].max()
# row_max = data[data.temp == max_temp]
# temp_cels = int(row_max.temp)* 9 / 5 + 32
# #print(temp_cels)
# data_students = {"students":["Enes", "Selim", "Baybars"],
#                  "scores": [76, 56, 65] }
# data = pandas.DataFrame(data_students)
# #print(data) table
# data.to_csv("new_data.csv")
#
# data_squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# num_black = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Black"])
# num_red = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Cinnamon"])
# num_gray = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Gray"])

# fur_color_list = data_squirrel["Primary Fur Color"]
# for color in fur_color_list:
#     if color == "Gray":
#         num_gray += 1
#     elif color == "Black":
#         num_black += 1
#     else:
#         num_red += 1
# data_dict = {
#     "Colors": ["Gray","Black", "Red"],
#     "Numbers": [num_gray, num_black, num_red]
# }
#
# df = pandas.DataFrame(data_dict)
#
# df.to_csv("colors.csv")
