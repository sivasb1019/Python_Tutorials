def swap(a, b, arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
        # arr[a] = arr[a] + arr[b]
        # arr[b] = arr[a] - arr[b]
        # arr[a] = arr[a] - arr[b]

def HoarePartition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        while start <len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -=1
        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)
    return end

def quickSort(elements, start, end):
    if start < end:
        partition_index = HoarePartition(elements, start, end)
        print(partition_index)
        quickSort(elements, start, partition_index-1)
        quickSort(elements, partition_index + 1, end)

if __name__ == '__main__':
    # elements = [11, 9, 29, 7, 2, 15, 28]
    # quickSort(elements, 0, len(elements) - 1)
    # print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],a
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        ["mona", "dhaval", "aamir", "tina", "chang"]
    ]

    for elements in tests:
        quickSort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')
