#Ex 3.2 Python 4 everybody
strhr = input("Enter Hours:")
strrate = input("Enter Rate:")
fhr = 0
fr = 0
try:
    fhr = float(strhr)
    frate = float(strrate)
except Exception as e:
    print("Please enter numerical values")
    quit()

overtime = fhr - 40
pay = 0
if(overtime>0):
    pay = (40*frate) + (overtime * (1.5*frate))
else:
    pay = (fhr*frate)
print(pay)
