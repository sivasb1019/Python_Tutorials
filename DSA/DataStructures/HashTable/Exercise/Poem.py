wordCount = {}

with open("poem.txt", "r") as f:
    for line in f:
        words = line.split(' ')
        for word in words:
            word = word.replace('\n', '')
            if word in wordCount:
                wordCount[word]+=1
            else:
                wordCount[word] = 1

print(wordCount)
