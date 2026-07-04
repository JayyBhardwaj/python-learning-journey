#SCHOLARSHIP ELIGIBILITY CRITERIA:
Maths=float(input("Enter Marks scored in Mathematics: "))
Acc=float(input("Enter Marks scored in Accountancy: "))
Eco=float(input("Enter Marks scored in Economics: "))

if(Maths>100 or Maths<0 or Acc>100 or Acc<0 or Eco>100 or Eco<0):
    print("Invalid Data")
else:
    #CALCULATING THE AVERAGE
    avg=(Maths+Acc+Eco)/3
    print("Your Average marks are:",avg)

    #GRADE ACHIEVED
    if(avg>=90):
        print("EXCELLENT! You have achieved A+ grade")
    elif(avg>=80 and avg<90):
        print("GREAT! You have achieved A grade")
    elif(avg>=70 and avg<80):
        print("GOOD! You have achieved B grade")
    elif(avg>=60 and avg<70):
        print("FAIR! You have achieved C grade")
    elif(avg>=50 and avg<60):
        print("BELOW AVERAGE! You have achieved D grade")
    else:
        print("FAIL! You have failed the exam")

    #SCHOLARSHIP ELIGIBILITY
    if(avg>=85 and Maths>=65 and Acc>=65 and Eco>=65):
        print("CONGRATULATIONS! YOU ARE ELIGIBLE FOR SCHOLARSHIP")
    else:
        print("NOT ELIGIBLE FOR SCHOLARSHIP")
