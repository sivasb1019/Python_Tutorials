def swap(a, b, elements):
    if a!= b:
        temp = elements[a]
        elements[a] = elements[b]
        elements[b] = temp
        # print(elements)

def lomutoPartition(elements, start, end):
    # Median of three concept
    mid = (start + end) // 2
    if elements[mid] < elements[start]:
        swap(mid, start, elements)
    if elements[end] < elements[start]:
        swap(start, end, elements)
    if elements[mid] < elements[end]:
        swap(mid, end, elements)

    pivot = elements[end]
    partition_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            print(i, partition_index)
            swap(i, partition_index, elements)
            partition_index += 1

    swap(partition_index, end, elements)

    return  partition_index



def quickSort(elements, start, end):
    if len(elements) <=1:
        return
    if start < end:
        partition_index = lomutoPartition(elements, start, end)
        print(partition_index)
        quickSort(elements, start, partition_index-1)
        quickSort(elements, partition_index+1, end)

if __name__ == '__main__':
    # elements = [11, 9, 29, 7, 2, 15, 28]
    # quickSort(elements, 0, len(elements) - 1)
    # print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        ["mona", "dhaval", "aamir", "tina", "chang"]
    ]

    for elements in tests:
        quickSort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')
