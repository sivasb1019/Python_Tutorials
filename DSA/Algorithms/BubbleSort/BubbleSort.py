def bubbleSort1(elements):
    size = len(elements)
    steps = 0
    for i in range(size):
        swap = False
        steps += 1
        for j in range(i+1, size):
            steps += 1
            if elements[i] > elements[j]:
                elements[i] = elements[i] + elements[j]
                elements[j] = elements[i] - elements[j]
                elements[i] = elements[i] - elements[j]
                swap = True
        if not swap:
            break
    print("Steps:", steps)
    return elements

def bubbleSort2(elements):
    size = len(elements)
    steps = 0
    for i in range(size-1):
        swap = False
        steps += 1
        for j in range(size-i-1):
            steps += 1
            if elements[j] > elements[j+1]:
                elements[j] = elements[j] + elements[j+1]
                elements[j+1] = elements[j] - elements[j+1]
                elements[j] = elements[j] - elements[j+1]
                swap = True
        if not swap:
            break
    print("Steps:", steps)
    return elements


if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    # elements = [1, 2, 3, 4, 5]
    print("Bubble Sort 1 Function:")
    print(bubbleSort1(elements))
    print("Bubble Sort 2 Function:")
    print(bubbleSort2(elements))
