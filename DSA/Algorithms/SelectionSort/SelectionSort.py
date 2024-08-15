def selectionSort(arr):
    size = len(elements)
    for i in range(size-1):
        small = arr[i]
        index = None
        for j in range(i+1, size):
            if small > arr[j]:
                small = arr[j]
                index = j
        if index is not None:
            arr[index] = arr[i]
            arr[i] = small


if __name__ == '__main__':
    # elements = [78, 12, 15, 8, 61, 53, 23, 27]
    # selectionSort(elements)
    # print(elements)

    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selectionSort(elements)
        print(elements)