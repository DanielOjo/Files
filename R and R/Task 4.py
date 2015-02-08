#Daniel Ogunlana
#08/02/2015
#Files R and R task 4


try:
    Number_Range = False
    while not Number_Range:
        number = int(input("Please enter a number: "))
        if number >=1 and number <=100:
            Number_Range = True
            print(number)
        else:
            print("The value {0} is not an integer".format(number))
            
except ValueError:
    print("The value entered was not a number")
