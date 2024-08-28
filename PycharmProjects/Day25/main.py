import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # temps = data["temp"]
# # max = data["temp"].max()
#
#
#
# #print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# temp_mon = monday.temp
# temp_mon_f = (temp_mon * 9/5) + 32
# print(f"Monday temp in F: {temp_mon_f}")
#
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240730.csv")
#how many gray, cinnamon, black ones
fur_col = data["Primary Fur Color"]
black = 0
gray = 0
cinamon = 0
for col in fur_col:
    if col == "Black":
        black += 1
    if col == "Gray":
        gray += 1
    if col == "Cinnamon":
        cinamon += 1
list = {
    "Fur color" : ["Black","Gray", "Red"],
    "Total": [black, gray, cinamon],
}
data2 = pandas.DataFrame(list)
data2.to_csv("squirrel_count.csv")