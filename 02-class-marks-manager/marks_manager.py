##### STUDENTS MARKS
marks_list=[]
def add_marks():
    std_marks=int(input("Enter marks of Student"))
    if(std_marks>100 or std_marks<0):
        print("Invalid data")
    else:
        marks_list.append(std_marks)
        print("Data entered Succesfully")
add_marks()
add_marks()
add_marks()
add_marks()
add_marks()
add_marks()
add_marks()
add_marks()
add_marks()
add_marks()
#SHOWING MARKS
def show_marks():
    print("Entered Marks are:", marks_list)
show_marks()
#AVERAGE CALCULATOR
def avg():
    average=sum(marks_list)/ len(marks_list)
    print("Your average marks are:", average)
    if(average<=100 and average>90):
        print("You got A+ Grade")
    elif(average<=90 and average>80):
        print("You got A Grade")
    elif(average<=80 and average>70):
        print("You got B+ Grade")
    elif(average<=70 and average>60):
        print("You got B Grade")
    elif(average<=60 and average>50):
        print("You got C Grade")
    elif(average<=50 and average>40):
        print("You got D Grade")
    else:
        print("You got F Grade")
avg()
#REMOVE LOWEST MARK
def remove_lowest():
    lowest=min(marks_list)
    marks_list.remove(lowest)
    print("Lowest marks removed is:", lowest)
remove_lowest()
