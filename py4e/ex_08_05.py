# Exercise 8.5
valid = None
while valid is None:
    fileName = input('Enter file name: ')
    try:
        fileHandle = open(fileName)
        count = 0
        for line in fileHandle:
            if line.startswith('From '):
                lineList = line.strip().split()
                prsnAddr = lineList[1]
                print(prsnAddr)
                count = count + 1
        print('There were',count,'lines in the file with From as the first word')
        valid = 1
    except Exception as e:
        print('Enter a valid file name')
