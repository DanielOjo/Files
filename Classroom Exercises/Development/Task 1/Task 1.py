#Daniel Ogunlana
#10/02/2015
#Classroom Exercises
#Development Task 1

class Person:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None

people = []

person = Person()
person.first_name = input("Please enter your first name :")
person.last_name = input("Please enter your last name :")
person.date_of_birth = input("Please enter your date of birth (YEAR/MONTH/DAY) :")

people.append(Person)

for each in people:
    print(each)
