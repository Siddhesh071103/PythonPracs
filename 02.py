#Aim:To Implement Conditional and Looping Structures

#if else
x = int(input("Enter the number:"))         #take an input from the user
if(x>5):                                    #Check whether the number is greater or less than 5
     print("Number is greater than 5")
else:
     print("Number is smaller than 5")

#Nested if 
x = input("Enter an alphabet in range of a,b and c:")       #take an input from the user
if x == "a":                                                #check whether the alphabet is a,b and c
    print("Alphabet is a")                                      
elif x == "b":
    print("Alphabet is b")
elif x == "c":
    print("Alphabet is c")

#for loop
for i in range(1,6):
    print(i)
