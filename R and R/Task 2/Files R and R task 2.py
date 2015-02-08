#Daniel Ogunlana
#08/02/2015
#Files R and R task 2

with open("task2file.txt", mode="w", encoding="utf-8") as task2file:
    task2file.write("John\n")
    task2file.write("Isabella\n")
    
with open("task2file.txt", mode="r", encoding="utf-8") as task2file:
    for line in task2file:
        print(line)
