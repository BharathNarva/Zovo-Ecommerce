# # # # Instance Method
# # # # class MyClass:
# # # #     def display(self):
# # # #         print("Instance Method")
# # # # obj=MyClass()
# # # # obj.display()   

     
# # # #Two instance methods
# # # # class MyClass:
# # # #     def display1(self):
# # # #         print("Instance Method 1")
# # # #     def display2(self):
# # # #         print("Instance Method 2")
# # # # obj1=MyClass()
# # # # obj1.display1()
# # # # obj1.display2()
# # # #  
# # # # WAP to create addition using instance method:
# # # # class MyClass:
# # # #     def add(self,a,b):
# # # #         return a+b
# # # # obj=MyClass()             #creating the object of class
# # # # result=obj.add(10,20)     #calling add method
# # # # print("Addition:",result) #printing the method  
# # # #  
# # # ############################  
# # # ''' 
# # # #constructer:
# # # class MyClass:
# # #     def __init__(self,a,b):  #constructor
# # #         self.a=a
# # #         self.b=b
# # #     def add(self):
# # #         return self.a+self.b
# # # obj=MyClass(10,20)          #creating the object of class
# # # result=obj.add()            #calling add method
# # # print("Addition:",result)    #printing the method
# # # ############################
# # # '''
# # # '''
# # # #initialize instance variables:-
# # # class Student:
# # #     def __init__(self, name, age, grade):   # constructor with parameters
# # #         # instance variables
# # #         self.name = name
# # #         self.age = age
# # #         self.grade = grade

# # #     def display_info(self):  # method to display student details
# # #         print("Student Name:", self.name)
# # #         print("Age:", self.age)
# # #         print("Grade:", self.grade)

# # # # creating objects of Student class
# # # s1 = Student("Alice", 20, "A")
# # # s2 = Student("Bob", 19, "B")

# # # # calling method to display info
# # # s1.display_info()
# # # print("----------------")
# # # s2.display_info()
# # # ''' 
# # # ############################
# # # '''  
# # # #class loading and unloading
# # # class MyClass:
# # #     def __init__(self):
# # #         print("Constructor called")
# # #     def display(self):
# # #         print("Instance Method called")
# # #     def __del__(self):
# # #         print("Destructor called")
# # # obj=MyClass()          #constructor called
# # # obj.display()         #instance method called   
# # # del obj                #destructor called
# # # '''
# # # ''' 
# # # ############################
# # # #static method
# # # class Student:
# # #     # Method without self parameter
# # #     def school_name():
# # #         print("ABC International School")

# # # # Calling method directly using class name
# # # Student.school_name()
# # # # Output: ABC International School
# # # # Note: Static methods cannot access instance variables or methods directly.
# # # ############################
# # # '''
# # # ''' 

# # # '''
# # # ''' 
# # # #WAP to define the class if with the name employee with following details:
# # # class employee:
# # #     company_name="Wipro Pvt Ltd"  #class variable
# # #     def emp_details(emp_id,emp_name,emp_salary):  #static method
# # #         print("Employee ID:",emp_id)
# # #         print("Employee Name:",emp_name)
# # #         print("Employee Salary:",emp_salary)
# # #         print("Company Name:",employee.company_name) #accessing class variable
# # # employee.emp_details(101,"John",50000)  #calling static method
# # # ############################
# # # '''
# # # '''
# # # #instance variable [object level variable]
# # # #inside the constructor using self keyword
# # # class Student:
# # #     def __init__(self, name, age):  # constructor with parameters
# # #         # instance variables
# # #         self.name = name
# # #         self.age = age

# # #     def display_info(self):  # method to display student details
# # #         print("Student Name:", self.name)
# # #         print("Age:", self.age)
# # # # creating objects of Student class
# # # s1 = Student("Alice", 20)
# # # s2 = Student("Bob", 19)
# # # # calling method to display info
# # # s1.display_info()
# # # print("----------------")
# # # s2.display_info()
# # # ############################
# # # '''
# # # ''' 
# # # #inside the instance method using self keyword
# # # class Student:
# # #     def set_details(self, name, age):  # instance method to set details
# # #         self.name = name  # instance variable
# # #         self.age = age    # instance variable

# # #     def display_info(self):  # method to display student details
# # #         print("Student Name:", self.name)
# # #         print("Age:", self.age)
# # # # creating objects of Student class
# # # s1 = Student()
# # # s2 = Student()
# # # # setting details using instance method
# # # s1.set_details("Alice", 20)
# # # s2.set_details("Bob", 19)
# # # # calling method to display info
# # # s1.display_info()
# # # print("----------------")
# # # s2.display_info()
# # # ############################
# # # '''
# # # '''
# # # #outside the object using object reference
# # # class orange:
# # #     def __init__(self):
# # #             self.a=10  #instance variable
# # #             self.b=20  #instance variable
# # #     def m(self):
# # #         self.c=30  #instance variable
# # # m=orange()
# # # print(m.__dict__)  #printing instance variable
# # # m.d=40           #instance variable
# # # print(m.__dict__)  #printing instance variable
# # # m.m()
# # # print(m.__dict__)  #printing instance variable
# # # ############################
# # # '''
# # # '''
# # # '''
# # # ''' 
# # # #local variable
# # # class MyClass:
# # #     def display(self):
# # #         a=10  #local variable
# # #         b=20  #local variable
# # #         print("Addition:",a+b)
# # # obj=MyClass()
# # # obj.display()
# # # ############################
# # # ''' 
# # # '''
# # # '''
 
# # # # #how to access instance variable
# # # # class MyClass:
# # # #     def __init__(self):
# # # #         self.a=10  #instance variable
# # # #         self.b=20  #instance variable
# # # #     def m(self):
# # # #         self.c=30  #instance variable
# # # # m=MyClass()
# # # # print(m.a)  #accessing instance variable
# # # # print(m.b)  #accessing instance variable
# # # # m.m()
# # # # print(m.c)  #accessing instance variable
# # # ############################
# # # '''
# # # ''' 


# # # #how to delete the instance variable form object
# # # class MyClass:
# # #     def __init__(self):
# # #         self.a=10  #instance variable
# # #         self.b=20  #instance variable
# # #     def m(self):
# # #         self.c=30  #instance variable
# # # m=MyClass()
# # # print(m.__dict__)  #printing instance variable
# # # del m.a            #deleting instance variable
# # # print(m.__dict__)  #printing instance variable
# # # m.m()
# # # print(m.__dict__)  #printing instance variable
# # # del m.c            #deleting instance variable
# # # print(m.__dict__)  #printing instance variable
# # # ############################

# # #write a program to declare the static variable & print the value to see class name & object ?
# # # class myclass:
# # #     x = 10   # Class variable
    
# # #     def __init__(self):
# # #         self.y = 20   # Instance variable


# # # # Create objects outside the class
# # # mc1 = myclass()
# # # mc2 = myclass()

# # # print("value using class name =", myclass.x)
# # # print("value using object name =", mc1.x)
# # # print("value using object name =", mc2.x)
# # # print("value using object name =", mc1.y)
# # # print("value using object name =", mc2.y)

# # # # Changing values
# # # mc1.x = 100   # Creates instance variable x for mc1
# # # mc2.x = 200   # Creates instance variable x for mc2
# # # myclass.x = 300   # Changes class variable

# # # mc1.y = 400   # Changes mc1’s y
# # # mc2.y = 500   # Changes mc2’s y

# # # print("\nAfter changing values:")
# # # print("class variable x =", myclass.x)
# # # print("mc1.x =", mc1.x)
# # # print("mc2.x =", mc2.x)
# # # print("mc1.y =", mc1.y)
# # # print("mc2.y =", mc2.y)
# # # print("mc1.__dict__ =", mc1.__dict__)
# # # print("mc2.__dict__ =", mc2.__dict__)


# # # class myclass:
# # #     a=10
# # #     def __init__(self):
# # #         myclass.b=20
# # #     def m1(self):
# # #         myclass.c=30
# # #     @classmethod
# # #     def cm1(cls):
# # #         myclass.d=40
# # #         cls.e=50
# # #     @staticmethod
# # #     def sm1():
# # #         myclass.f=60
# # # mc1=myclass()
# # # print(myclass.__dict__)
# # # mc1.m1()
# # # print(myclass.__dict__)
# # # mc1.cm1()
# # # print(myclass.__dict__)
# # # mc1.sm1()
# # # print(myclass.__dict__)



# # class myclass:
# #     a = 10
# #     def __init__(self):
# #         self.b = 20   # instance variable
# #     def m1(self):
# #         self.c = 30   # instance variable
# #     @classmethod
# #     def cm1(cls):
# #         cls.d = 40    # class variable
# #     @staticmethod
# #     def sm1():
# #         print("Static method called")  # does not create attributes

# # mc1 = myclass()
# # print(mc1.__dict__)    # {'b': 20}
# # mc1.m1()
# # print(mc1.__dict__)    # {'b': 20, 'c': 30}
# # mc1.cm1()
# # print(myclass.__dict__)  # contains a=10, d=40
# # mc1.sm1()

# class myclass:
#     a = 10
#     def __init__(self):
#         self.b = 20   # instance variable
#     def m1(self):
#         self.c = 30   # instance variable
#     @classmethod
#     def cm1(cls):
#         cls.d = 40    # class variable
#     @staticmethod
#     def sm1():
#         print("Static method called")  # does not create attributes
# mc1 = myclass()
# print(mc1.__dict__)    # {'b': 20}
# mc1.m1()
# print(mc1.__dict__)    # {'b': 20, 'c': 30}
# mc1.cm1()
# print(myclass.__dict__)  # contains a=10, d=40
# mc1.sm1()


#write a program to handle zero divide error by using exceptional handling
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = a / b
#     print("Result:", c)
# except ZeroDivisionError:
#     print("B value cannot be zero")
# finally:
#     print("finally block executed")


#with in a program we will have one try block which will followed by any number of exception block?
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = a / b
# except ZeroDivisionError:
#     print("B value cannot be zero")
# except ValueError:
#     print("Invalid input. Please enter numeric values.")
# finally:
#     print("finally block executed")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = a / b
# except(ZeroDivisionError,ValueError):
#         print("B value cannot be zero & Invalid input. Please enter numeric values.")
# finally:
#     print("finally block executed")

# 4.Default exception catch any type of Exception?
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = a / b
#     print("Division:", c)
# except:
#     print("Exception occurred")
# finally:
#     print("finally block executed")

#5 program using else instead of finally
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = a / b
#     print("Division:", c)
# except:
#     print("please check the code for error")
# else:
#     print("no error in the code")

# class Bc:
#     def __init__(self,ai,aj):
#      self.i=ai
#      self.j=aj
#      print("i=",self.i)
#      print("j=",self.j)

# class Dc(Bc):
#     def __init__(self,am,an):
#      super().__init__(am,an)
#      self.m=am
#      self.n=an
#      print("m=",self.m)
#      print("n=",self.n)
# object=Dc(10,20)

# class A:
#     def __init__(self, ax, ay):
#         self.x = ax
#         self.y = ay
#         self.z = ax + ay
#         print("Addition =", self.z)

#     def addition(self, ax, ay):
#         self.x = ax
#         self.y = ay
#         self.z = ax + ay
#         print("Addition =", self.z)

#     def subtract(self, ax, ay):
#         self.x = ax
#         self.y = ay
#         self.z = ax - ay
#         print("Subtraction =", self.z)

# class B(A):
#     def m(self, ax, ay):
#         self.x = ax
#         self.y = ay
#         self.z = ax * ay
#         print("Multiplication =", self.z)


# # Create object
# obj = B(10, 5)       # Calls __init__, does addition
# obj.addition(10, 5)  # Calls addition method
# obj.subtract(10, 5)  # Calls subtraction method
# obj.m(10, 5)         # Calls multiplication method

# class A:
#     def m1(self):
#         print("Apple")
# class B(A):
#     def m2(self):
#         print("Banana")
# obj=B()
# obj.m1()
# obj.m2()        