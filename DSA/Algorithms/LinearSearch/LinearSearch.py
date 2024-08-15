def linearSearch(numbers_list, num):
    for n in numbers_list:
        if n == num:
            return True
    return False

numbers_list = [1, 3, 8, 10, 11, 12, 19, 27, 28, 30]
value = 35
print("Numbers List:", numbers_list)
print(f"Is {value} is present in numbers_list? {linearSearch(numbers_list, value)}")
