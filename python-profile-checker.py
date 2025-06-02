fname=input("enter you'r name: ")
age=input("enter you'r age: ")

if not age.isdigit():
    age=input("please enter your age in digits: ")
   
graduated=input("Are you graduated('yes' or 'no')? ")
if graduated !="yes" or  graduated != "no":
    print("answer by yes or no")
    graduated=input("Are you graduated('yes' or 'no')? ")
fOI=input("what are the field you intersted in? ")
gpa=input("enter your GPA: ")

if not gpa.isdigit() :
     print("pleases enter valid value for GPA 0-5." )    
     gpa=input("enter your GPA: ")
elif float(gpa)<0 or float(gpa)>5:
     print("pleases enter valid value for GPA 0-5." )    
     gpa=input("enter your GPA: ")

print("-your name is: ",fname + " \n -you are:",age + "years old \n your gpa is:",gpa )
if graduated=="yes":
     print("you are graduated!")
else:
     print("continue and work hard")

print("your intrests are: " ,fOI)    
if int(age)<25 and float(gpa)>=3.5 and graduated=="yes":
     print("you are eligible for a scholarship")
elif int(age)>30 and float(gpa)>=2.5:
     print('you are eligible for an internship ')
else:
     print("please apply agian")
     

     

    
  
    




