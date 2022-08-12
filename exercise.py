# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


"""1"""



for i in range(3):
    a = int(input("Enter first number: "))
    b = int(input("input second number: "))
    if a > b:
        print("first is bigger than the second number")
    if a < b:
        print("the second number is bigger than the first one")
    if a <= b:
        print("first number is smaller or is even to the second number")
    if a >= b:
        print("the first number is bigger or is even to second number")
    if a != b:
        print("the numbers are not even!")
    if a == b:
        print("the numbers are even")
    if a >= 1000:
        print("first number is a big number!")
    if b <= 10:
        print("second number is a tiny number!")
    if (a + b) > 10000:
        print("the sum of first and second number is more than 10k")
    if 10 < a < 100:
        print("a is bigger than 10, but smaller than 100")




"""2"""
"""
January - 31 days
February - 28 days in a common year and 29 days in leap years
March - 31 days
April - 30 days
May - 31 days
June - 30 days
July - 31 days
August - 31 days
September - 30 days
October - 31 days
November - 30 days
December - 31 days
"""
"""
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months31 = ["January","March","May","July","August","October","December"]
months30 = ["April","June","September","November"]
months28 = ["February"]
print(months)




mon = str(input("enter  a month: "))
if mon in months31:                            
    print("this month has 31 days")
elif mon in months30:
    print("This month has 30 days")
else:  
    print("This Month has 28 days")
"""