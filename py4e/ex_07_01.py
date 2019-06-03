#Exercise 7.01

valid = None
while valid is None:
    fileName = input('Enter file name: ')
    try:
        fileHandle = open(fileName)
        count = 0
        for line in fileHandle:
            count = count + 1
            print(line.upper().rstrip())
        valid = 1
    except Exception as e:
        print('Enter a valid file name')
