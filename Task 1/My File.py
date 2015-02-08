#Daniel Ogunlana
#07/02/15
#My File

with open("studentstextfile.txt", mode="r", encoding="utf-8") as students_text_file:
    for line in students_text_file:
        #for count in range(len(line)):
            #print("{0} {1}".format(count,line))
        print(line)
