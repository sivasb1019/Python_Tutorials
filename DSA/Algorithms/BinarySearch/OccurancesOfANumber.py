# from util import time_it
#
# @time_it
def binarySearch(numbers_list, value):
    start = 0
    end = len(numbers_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers_list[mid] == value:
            return mid
        elif numbers_list[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# @time_it
def findAllOccurances(numbers_list, value):
    index = binarySearch(numbers_list, value)
    occurances = [index]
    i = index - 1
    steps = 0
    while i >= 0:
        steps = steps + 1
        if numbers_list[i] == value:
            occurances.append(i)
        else:
            break
        i -= 1
    i = index + 1
    while i < len(numbers_list):
        steps = steps + 1
        if numbers_list[i] == value:
            occurances.append(i)
        else:
            break
        i += 1
    # return sorted(occurances)  # 1.148223876953125 mil sec
    # return occurances  # 0.99945068359375 mil sec
    return steps

# @time_it
def occuranceOfNumber(numbers_list, value):
    index = binarySearch(numbers_list, value)
    occurances = [index]
    i = index - 1
    j = index + 1
    steps=0
    while i >= 0 or j < len(numbers_list):
        steps = steps+1
        if numbers_list[i] == value:
            occurances.append(i)
        if numbers_list[j] == value:
            occurances.append(j)
        if numbers_list[i] != value and numbers_list[j] != value:
            break
        i -= 1
        j += 1

    # return sorted(occurances)  # 1.148223876953125 mil sec
    # return occurances  # 0.99945068359375 mil sec
    return steps

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15
print("Lenght of Numbers list", len(numbers))
print("Steps in 'FindAllOccurances' function:", findAllOccurances(numbers, number_to_find))
print("Steps in 'OccuranceOfNumber' function:",occuranceOfNumber(numbers, number_to_find))
# occuranceOfNumber(numbers, number_to_find)
