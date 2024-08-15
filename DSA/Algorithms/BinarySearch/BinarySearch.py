def recursiveBinarySearch(numbers_list, value, start, end):
    if start > end:
        return False
    mid = (start + end)//2
    if numbers_list[mid] == value:
        return True
    elif numbers_list[mid] < value:
        start = mid+1
        return recursiveBinarySearch(numbers_list, value, start, end)
    else:
        end = mid - 1
        return recursiveBinarySearch(numbers_list, value, start, end)

def binarySearch(numbers_list, value):
    start = 0
    end = len(numbers_list) - 1
    while start <= end:
        mid = (start + end)//2
        if numbers_list[mid] == value:
            return True
        elif numbers_list[mid] < value:
            start = mid+1
        else:
            end = mid - 1
    return False


numbers_list = [1, 3, 8, 10, 11, 12, 19, 27, 28, 30]
value = 30
print("Numbers List:", numbers_list)
print(f"Is {value} is present in numbers_list(Recursive Binary Search)? "
      f"{recursiveBinarySearch(numbers_list, value, 0, len(numbers_list)-1)}")
print(f"Is {value} is present in numbers_list(Binary Search)? "
      f"{binarySearch(numbers_list, value)}")
