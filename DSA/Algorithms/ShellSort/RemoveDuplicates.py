def shellSort(elements):
    sorted_list = []
    div = 2
    size = len(elements)
    gap = size // div
    while gap > 0:
        index_to_delete = []
        for i in range(gap, size):
            anchor = elements[i]
            j = i

            while j >= gap and anchor <= elements[j-gap]:
                if anchor == elements[j - gap]:
                   index_to_delete.append(j)
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = anchor
        index_to_delete = list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del elements[i]
        # div *= 2
        size = len(elements)
        gap = gap // 2



if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    shellSort(elements)
    print(elements)
