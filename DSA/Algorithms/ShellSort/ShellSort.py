def shellSort(elements):
    size = len(elements)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j >= gap and anchor < elements[j-gap]:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap = gap // 2



if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shellSort(elements)
    print(elements)
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]
    for elements in tests:
        shellSort(elements)
        print(elements)