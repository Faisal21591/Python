print("----------------------------------------------")
print("Out Put of Example-1 ")
#
#Example-1
x=22
print(x,type(x))
#Out Put of Example-1
#22 <class 'int'>
#
print("----------------------------------------------")
print("Out Put of Example-2 ")
#
#Example-2
y = "Enter to Learn and leave to serve"
print(y, type(y))
#Out Put of Example-2
#Enter to Learn and leave to serve <class 'str'>
#
print("----------------------------------------------")
print("Out Put of Example-3 ")
#
#Example-3 Python is case-sensitive
Y= "Book are Good companion"
print(Y,type(Y))
#Out Put of Example-3
#Book are Good companion <class 'str'>
#
print("----------------------------------------------")
print("Out Put of Example-4 ")
#
#Example-4
print(y)
print(Y)
#Out Put of Example-4
#Enter to Learn and leave to serve
#Book are Good companion
# Now New Type of Variables
#
print("----------------------------------------------")
print("Out Put of Example-5 ")
#
#Example-5
x,y,z,= "Mangoes","Cherry","Apple"
print(x)
print(y)
print(z)
#----------------------------------------------
#Out Put of Example-5
#Mangoes
#Cherry
#Apple
#
print("----------------------------------------------")
print("Out Put of Example-6 ")
#
#Example-6
x=y=z= "Mangoes are very sweet"
print(x)
print(y)
print(z)
#----------------------------------------------
#Out Put of Example-6
#Mangoes are very sweet
#Mangoes are very sweet
#Mangoes are very sweet
#
print("----------------------------------------------")
print("Out Put of Example-7 ")
#
#Example-7
fruits=["Mangoes","Cherry","Apple"]
x,y,z,= fruits
print(x)
print(y)
print(z)
#----------------------------------------------
#Out Put of Example-7
#Mangoes
#Cherry
#Apple
#
print("----------------------------------------------")
print("Out Put of Example-8 ")
#
#Example-8 How to print variable
Exam_Score= 98
print(Exam_Score)
print("My Name Is Ali and Exam Score is " +str(Exam_Score)+ " Percent")#Add Str why explain
print("My Name Is Ali and Exam Score is",Exam_Score,"Percent")#No need to create space
print(f"I am Ali and I Secure {Exam_Score} Percent in exam")#used format string
#----------------------------------------------
# Out Put of Example-8
# 98
# My Name Is Ali and Exam Score is 98 Percent
# My Name Is Ali and Exam Score is 98 Percent
# I am Ali and I Secure 98 Percent in exam
#
print("----------------------------------------------")
print("Out Put of Example-9 ")
#
#Example-9 Exercise no 1
#get input name ,gpa,  over all position in College and is he is online
name = input("Enter your name :- ") # Passing string
gpa  =float(input("Enter your GPA   :- ")) # Passing float
online=input("He is Online (y/n):-   ").strip().lower()=="yes"
position_in_College= int(input("Enter your Postion In Collage :- "))#Passing Integer
print(f"{name} your overall GPA is {gpa} and secure {position_in_College} Position in college")
if gpa > 3.5:
    print(f"Greeting for {name}, you can apply for Phd")
else:
    print("You need to improve your GPA to get admission in Phd")

if online:
    print("Jimmy is Online")
else:
    print("No Jimmy is Offline")
#
print("----------------------------------------------")
print("Out Put of Example-10 ")
#
#Example-10 Boolean
Online= True
sale_is_On= False
Game_is_On= True
print(f"Are You Online {Online}")
print(f"Sale On Shoes is On or Not {sale_is_On}")
print(f"Is Game On ? {Game_is_On} ")
if Online:
    print("Yes I am Online")
else:
    print("Offline")