mark = int(input("Enter the marks: "))
if(mark>=90):
    grade='S'
if(mark<90 and mark>=80):
    grade='A'
if(mark<80 and mark>=70):
    grade='B'
if(mark<70 and mark>=60):
    grade='C'
if(mark<60 and mark>=50):
    grade='D'
if(mark<50 and mark>=40):
    grade='E'
if(mark<40):
    grade='F'
print("You have scored " + grade + " grade")