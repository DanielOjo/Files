#Daniel Ogunlana
#10/02/2015
#Classroom Exercises
#Revision Task 1

#Writing
with open("student_text", mode = "w", encoding = "utf-8") as student_text:
    for text in range(5):
        student_text.write(input("Please write a message: ") + "\n")

#Printing
with open("student_text", mode = "r", encoding = "utf-8") as student_text:
    for text in student_text:
        print(text)
