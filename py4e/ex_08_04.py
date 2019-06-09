# Exercise 8.4
valid = None
while valid is None:
    fileName = input('Enter file name: ')
    try:
        fileHandle = open(fileName)
        wordList = []
        for line in fileHandle:
            words = line.strip().split()
            for word in words:
                if word not in wordList:
                    wordList.append(word)
        wordList.sort()
        print(wordList)
        valid = 1
    except Exception as e:
        print('Enter a valid file name')
