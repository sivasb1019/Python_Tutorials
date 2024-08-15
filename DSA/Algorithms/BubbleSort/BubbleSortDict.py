def bubbleSortDict(elements, key):
    size = len(elements) - 1
    steps = 0
    for i in range(size):
        swap = False
        steps += 1
        for j in range(size-i):
            steps += 1
            if elements[j][key] > elements[j+1][key]:
                temp = elements[j+1]
                elements[j+1] = elements[j]
                elements[j] = temp
                swap = True
        if not swap:
            break
    print(f"Sorted by {key}:")
    print("Steps:", steps)
    for element in elements:
        print(element)


if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubbleSortDict(elements, "name")
    bubbleSortDict(elements, "transaction_amount")
