def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    mergeTwoSortedArray(left, right, arr)


def mergeTwoSortedArray(a, b, arr):
    # sorted_list = []
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            # sorted_list.append(a[i])
            arr[k] = a[i]
            i += 1
        else:
            # arr.append(b[j])
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        # sorted_list.append(a[i])
        arr[k] = a[i]
        i += 1
        k += 1


    while j < len(b):
        # sorted_list.append(b[j])
        arr[k] = b[j]
        j += 1
        k += 1

    # return  sorted_list


if __name__ == "__main__":
    # a = [17, 21, 209, 38]
    # b = [4, 9, 25, 32]
    # print("Merging two sorted array:", mergeTwoSortedArray(a, b))

    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        mergeSort(arr)
        print("Merging one unsorted array:", arr)
