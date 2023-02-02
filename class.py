#AIM: Construct function,class and object using python

#CODE:

print("FACTORIAL OF A NUMBER")

num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)

#OUTPUT:

FACTORIAL OF A NUMBER
Enter a number: 5
The factorial of 5 is 120

#CODE:

class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
     
    def average(self):
            print("Student Name: ",self.name)
            if(self.marks>60):
                  print("Grade: Student",self.name,"get A")
          
            elif(self.marks>50):
                  print("Grade: Student",self.name,"get B")

            elif(self.marks>40):
                  print("Grade: Student",self.name,"get C")

            else:
            	print("Student {} is fail")

a=input("Enter your Name: ")
b=int(input("Enter your Marks: "))

s1=Student(a,b)
s1.average()

#OUTPUT:
Enter your Name: Rohit Sharma
Enter your Marks: 45
Student Name:  Rohit Sharma
Grade: Student Rohit Sharma get C

