#Ex 11.1 Regex Extracting data from text files
import re

valid = None
while valid is None:
    fileName = input('Enter file name: ')
    try:
        fileHandler = open(fileName)
        valid = 1
        sum = 0
        num = 0
        for line in fileHandler:
            numList = re.findall('[0-9]+',line)
            for numStr in numList:
                num = int(numStr)
                sum = sum + num
        print(sum)
    except Exception as e:
        print('Enter a valid file name')
    pass
