arr = []
with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            arr.append(int(tokens[1]))
        except:
            print("Invalid temperature... Ignore the row")

print("Average temperature in first week of Jan:",
      sum(arr[0:7]) / len(arr[0:7]))
print("Maximum temperature in Jan:", max(arr))
