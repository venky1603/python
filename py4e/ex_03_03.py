#EX 03.03
strScore = input("Enter Score:")
fScore = 0.0
try:
    fScore = float(strScore)
except Exception as e:
    print("Please enter numerical value")
    quit()

if (fScore >= 0.0 and fScore <= 1.0):
    if (fScore >= 0.9):
        print("A")
    elif (fScore >= 0.8):
        print("B")
    elif(fScore >= 0.7):
        print("C")
    elif(fScore >= 0.6):
        print("D")
    else:
        print("F")
else:
    print("Please enter a score between 0.0 and 1.0")
    quit()
