CODE:
emp.py

class Employee():
    def __init__(self,roll,name,sal):
        self.roll=roll
        self.name=name
        self.sal=sal 
        
    def display(self):
        print("Employee ID is:",self.roll);
        print("Employee name is:",self.name);
        print("Employee salary is:",self.sal);

main.py

import emp, pickle
f=open('myfile.dat','wb')
n = int(input('Enter total no. of employee: '))
for i in range(n):
    roll = int(input('Enter employee rollno.: '))
    name = input('Enter employee name: ')
    sal = float(input('Enter Salary: '))
    e=emp.Employee(roll,name,sal)
    pickle.dump(e,f)
f.close()
f=open('myfile.dat','rb')
print('\nEmployee details: ')
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print('End of file reached')
        break
f.close()

OUTPUT:

Enter total no. of employee: 2
Enter employee rollno.: 56
Enter employee name: siddhesh
Enter Salary: 500000000000000
Enter employee rollno.: 57
Enter employee name: prathmessh
Enter Salary: 150

Employee details: 
Employee ID is: 56
Employee name is: siddhesh
Employee salary is: 500000000000000.0
Employee ID is: 57
Employee name is: prathmessh
Employee salary is: 150.0
End of file reached
