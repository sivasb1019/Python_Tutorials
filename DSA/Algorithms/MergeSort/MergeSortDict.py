def mergeSort(elements, key, descending=False):
    if len(elements) <= 1:
        return elements
    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    mergeSort(left, key, descending)
    mergeSort(right, key, descending)
    mergeUnsortedArray(left, right, elements, key, descending)

def mergeUnsortedArray(a, b, elements, key, descending):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i][key] <= b[j][key]:
            if descending:
                elements[k] = b[j]
                j += 1
            else:
                elements[k] = a[i]
                i += 1
        else:
            if descending:
                elements[k] = a[i]
                i += 1
            else:
                elements[k] = b[j]
                j += 1
        k += 1

    while i < len(a):
        elements[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        elements[k] = b[j]
        j += 1
        k += 1

def display(elements):
    for element in elements:
        print(element)

if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2},
        { 'name': 'ashok',  'age': 31,  'time_hours': 5},
        { 'name': 'siva',  'age': 11,  'time_hours': 4},
        { 'name': 'balan',  'age': 22,  'time_hours': 2.5},
        { 'name': 'bala',  'age': 3,  'time_hours': 1.5},
    ]
    mergeSort(elements, 'name', True)
    display(elements)