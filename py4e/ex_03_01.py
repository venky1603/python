#Ex 3.1 Python 4 everybody
strhr = input("Enter Hours:")
fhr = float(strhr)
strrate = input("Enter Rate:")
frate = float(strrate)
overtime = fhr - 40
pay = 0
if(overtime>0):
    pay = (40*frate) + (overtime * (1.5*frate))
else:
    pay = (fhr*frate)
print(pay)
