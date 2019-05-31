#EX 4.6

# function to compute pay given hours and hourly rate
# function will check for numerical value entry. Function will quit if numerical values are not entered
# function will evaluate overtime pay and calculate the pay
def computepay(hour, rate):
    pay = 0
    flhour = 0
    flrate = 0

    try:
        flhour = float(hour)
        flrate = float(rate)
    except Exception as e:
        print("Please enter numerical values")
        quit()

    overtime = flhour - 40
    if overtime > 0:
        pay = (40*flrate) + (overtime * (1.5*flrate))
    else:
        pay = (flhour * flrate)
    return pay

strhr = input("Enter hours: ")
strrate = input("Enter rate: ")
print(computepay(strhr,strrate))
