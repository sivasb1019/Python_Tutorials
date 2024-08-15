dict = {}
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = tokens[1]
            dict[day] = int(temperature)
        except:
            print()
print(dict)
print(dict['Jan 9'])
print(dict['Jan 7'])