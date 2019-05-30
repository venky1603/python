#Ex 05.02

largest = None
smallest = None
mylist = []

while True:
    strVal = input('Enter a number: ')
    if strVal == 'done':
        break
    try:
        intVal = int(strVal)
        mylist.append(intVal)
        #print(mylist)
    except Exception as e:
        print('Invalid input')
        continue

def maxValue(alist):
    max = None
    for thisNum in alist:
        if max is None:
            max = thisNum
        elif thisNum > max:
            max = thisNum
    return max

def minValue(alist):
    min = None
    for thisNum in alist:
        if min is None:
            min = thisNum
        elif thisNum < min:
            min = thisNum
    return min

largest = maxValue(mylist)
smallest = minValue(mylist)
print('Maximum is',largest)
print('Minimum is',smallest)
