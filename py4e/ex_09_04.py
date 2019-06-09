#Exercise 9.4
valid = None
while valid is None:
    fileName = input('Enter file name: ')
    try:
        fileHandler = open(fileName)
        valid = 1
        counts = dict()
        for line in fileHandler:
            if line.startswith('From '):
                lineList = line.split()
                prsnAddr = lineList[1]
                counts[prsnAddr] = counts.get(prsnAddr,0) + 1
        bigCount = None
        bigAddr = None
        for addr,count in counts.items():
            if bigCount is None or count > bigCount:
                bigAddr = addr
                bigCount = count
        print(bigAddr, bigCount)
    except Exception as e:
        print('Enter a valid file name')
    pass
