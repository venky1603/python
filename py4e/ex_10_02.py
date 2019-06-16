# Exercise 10.2
valid = None
while valid is None:
    fileName = input('Enter a file name: ')
    try:
        fileHandle = open(fileName)
        valid = 1
        counts = dict()
        for line in fileHandle:
            if line.startswith('From '):
                lineList = line.split()
                sentTime = lineList[5]
                sentTimeLst = sentTime.split(':')
                sentTimeHr = sentTimeLst[0]
                counts[sentTimeHr] = counts.get(sentTimeHr,0) + 1
        sortedList =  sorted ( [ (k,v) for k,v in counts.items()])
        for iter in sortedList:
            print(iter[0], iter[1])
    except Exception as e:
        print('Enter a valid file name')
    continue
