#
#++++++++++++++++++++++++++++++++++++++Tuples++++++++++++++++++++++++++++++++++++++++++
#
#
#
#Ex-1 Tuple Syntax it supports elements with multiple data tpye
from numpy.ma.core import count

Tuple_practice =(1, 2, 3, "a", "ammy", 10.5, (1,2,3))
print(Tuple_practice)
print(Tuple_practice,type(Tuple_practice))
#Output
# (1, 2, 3, 'a', 'ammy', 10.5, (1, 2, 3))
# (1, 2, 3, 'a', 'ammy', 10.5, (1, 2, 3)) <class 'tuple'>
#Ex-2 Tuple are ordered and that can be accessed using their index number
print("")
print("-------------------------------------------------------------------")
print("")
Tuple_Indexing =(1, 2, 3, "a", "ammy", 10.5, (1,2,3))
Tuple_Length=len(Tuple_Indexing)
print(Tuple_Length)
print(Tuple_Indexing[1])
print(Tuple_Indexing[4])
print(Tuple_Indexing[5])
print(Tuple_Indexing[6])
#Out Put
# 7 (length of the tuple)
# 2
# ammy
# 10.5
# (1, 2, 3)
print("")
print("-------------------------------------------------------------------")
print("")
#Ex-3 Positive Indexing and traversing items of tuple
Tuple_Indexing =(1, 2, 3, "a", "ammy", 10.5, (1,2,3))
Tuple_Length=len(Tuple_Indexing)
print("Total Tuple length is",Tuple_Length)
for i in range(Tuple_Length):
    print(i,": At Index", i ,"value is :",Tuple_Indexing[i]) # i is zero in Tuple_Indexing[i=0] and at  0 index in Tuple_Indexing tuple  is 1
#OutPut
# Total Tuple length is 7
# 0 : At Index 0 value is : 1
# 1 : At Index 1 value is : 2
# 2 : At Index 2 value is : 3
# 3 : At Index 3 value is : a
# 4 : At Index 4 value is : ammy
# 5 : At Index 5 value is : 10.5
# 6 : At Index 6 value is : (1, 2, 3)
print("")
print("-------------------------------------------------------------------")
print("")
#Ex-3 Negative Indexing and traversing items of tuple
Tuple_Indexing =(1, 2, 3, "a", "ammy", 10.5, (1,2,3))
Tuple_Length=len(Tuple_Indexing)
print("Total Tuple length is",Tuple_Length)
for i in range(-1,-Tuple_Length-1,-1):# range(-1,-7-1=8,-1) O/P will be -1,-2,-3,-4,-5,-6,-7
    print(i,": At Index", i ,"value is :",Tuple_Indexing[i]) # i is zero in Tuple_Indexing[i=0] and at  0 index in Tuple_Indexing tuple  is 1
#OutPut
# Total Tuple length is 7
# -1 : At Index -1 value is : (1, 2, 3)
# -2 : At Index -2 value is : 10.5
# -3 : At Index -3 value is : ammy
# -4 : At Index -4 value is : a
# -5 : At Index -5 value is : 3
# -6 : At Index -6 value is : 2
# -7 : At Index -7 value is : 1
print("")
print("-------------------------------------------------------------------")
print("")
#Ex-4 concatenating two or more tuple
Tuple_1 =(1, 2, 3)
Tuple_2 =("a", "ammy", 10.5)
Tuple_3 =(120, "John", 10.5,(5,6,7))
print(Tuple_1 + Tuple_2 + Tuple_3)
# Out PUT
#(1, 2, 3, 'a', 'ammy', 10.5, 120, 'John', 10.5, (5, 6, 7))
print("")
print("-------------------------------------------------------------------")
print("")
#Ex-5 Nesting tuple mean tuple inside  another tuple
Tuple_4 =(1, 2, 3)
Tuple_5 =("a", "ammy", 10.5)
Tuple_6 =(Tuple_4 , Tuple_5)
print(Tuple_6)
#Out Put
#((1, 2, 3), ('a', 'ammy', 10.5))
print("")
print("-------------------------------------------------------------------")
print("")
#Ex-6 Tuples repetition single tuple should have comma
Tuple_7 =("Rome",)*3
print(Tuple_7)
#Out Put
#('Rome', 'Rome', 'Rome')
print("")
print("-------------------------------------------------------------------")
print("")
#Ex-7 Tuples repetition single tuple should have comma
Tuple_8 =(10)
Tuple_9 =(10,)
print("See the difference with comma is type is Tuple and without comma it type is integer")
print(Tuple_8,type(Tuple_8))
print((Tuple_9,type(Tuple_9)))
#Out Put
#10 <class 'int'>
#((10,), <class 'tuple'>)

# print("")
# print("-------------------------------------------------------------------")
# print("")
# #Ex - 8 Tuples are Immutable removing/ replacing individual tuple is not possible
# Tuple_Indexing =(1, 2, 3, "a", "ammy", 10.5, (1,2,3))
# Tuple_Length[5]= 55
# print(Tuple_Length)
# # Out Put
# # Generates Error
# # TypeError: 'int' object does not support item assignment
print("")
print("-------------------------------------------------------------------")
print("")
#Ex - 8 Tuples slicing
Tuple_slicing = (10, 20, 30,40, 50, 60,70, 80, 90)
Tuple_length = len(Tuple_slicing)
print("Tuple Length is :", Tuple_length)
print("One   :",Tuple_slicing[:])
print("Two   :",Tuple_slicing[2:5])
print("Three :",Tuple_slicing[:7:2])
print("Four  :",Tuple_slicing[2:7:3])
print("Five  :",Tuple_slicing[::-1])
print("Six   :",Tuple_slicing[-1:-Tuple_length-1:-1]) #(-1:-9-1=10:-1)
print("Seven :",Tuple_slicing[-1:5:-1])
# Out Put
# Tuple Length is : 9
# One   : (10, 20, 30, 40, 50, 60, 70, 80, 90)
# Two   : (30, 40, 50)
# Three : (10, 30, 50, 70)
# Four  : (30, 60)
# Five  : (90, 80, 70, 60, 50, 40, 30, 20, 10)
# Six   : (90, 80, 70, 60, 50, 40, 30, 20)
# Seven : (90, 80, 70)
print("")
print("-------------------------------------------------------------------")
print("")

print("")
print("-------------------------------------------------------------------")
print("")
#Ex -10 Misc tuples
a,b,c = 10,20,30
Tp=(a,b,c)
print("It is called packing Tuple :",Tp)
Tp_1=()
print("It is called Empty Tuple  :",Tp_1)
Tp_2 = 1,2,3
print("Creating a Tuple i/p is with out brackets:",Tp_2)
#Out Put
#It is called packing Tuple : (10, 20, 30)
# It is called Empty Tuple  : ()
# Creating a Tuple i/p is with out brackets: (1, 2, 3)
print("")
print("-------------------------------------------------------------------")
print("")
#Ex -11 Built in Methods count() Method.
# index() Method.
Tuple_index = (10, 20, 30,40, 50, 60,70, 80, 90)
Location=Tuple_index.index(40)
print("Index Location :",Location)
#Out Put
#Index Location : 3
print("-------------------------------------------------------------------")
# sorted() Method.
Tuple_sorted = (10, 20, 30,40, 50, 60,70, 80, 90)
Sorted_Tuple=sorted(Tuple_sorted)
Sorted_TupleR=sorted(Tuple_sorted,reverse=True)
print("Original Tuple---------- :",Tuple_sorted)
print("Sorted Tuple (ascending) :",Sorted_Tuple)
print("Sorted Tuple (descending):",Sorted_TupleR)
#Out Put
# Original Tuple---------- : (10, 20, 30, 40, 50, 60, 70, 80, 90)
# Sorted Tuple (ascending) : [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Sorted Tuple (descending): [90, 80, 70, 60, 50, 40, 30, 20, 10]
print("count-------------------------------------------------------------------")
# min() and max() Methods.
Tuple_sorted = (10, 20, 30,40, 50, 60,70, 80, 90)
Min_in_Tuple= min(Tuple_sorted)
Max_in_Tuple= max(Tuple_sorted)
count_in_Tuple= count(Tuple_sorted)
print("The minimum value : ",Min_in_Tuple)
print("The maximum value : ",Max_in_Tuple)
print("The count value : ",count_in_Tuple)
#Out Put
# The minimum value :  10
# The maximum value :  90
# The count value :  9
print("-------------------------------------------------------------------")
#Ex - 9 Converting list to tuple using tuple() constructor
List_to_be_Converted_to_tuple = [10, 20, 30,40, 50, 60,70, 80, 90]
Convert_to_Tuple = tuple(List_to_be_Converted_to_tuple)
print(Convert_to_Tuple)
#Out Put
#(10, 20, 30, 40, 50, 60, 70, 80, 90)
# tuple() Function.
Tuple_List = [10, 20, 30,40, 50, 60,70, 80, 90]
Tuple_fun=tuple(Tuple_List)
print(Tuple_fun)
# Out Put
#(10, 20, 30, 40, 50, 60, 70, 80, 90)
print("-------------------------------------------------------------------")
#len() Function
Tuple_List1 = [10, 20, 30,40, 50, 60,70, 80, 90]
Tuple_fun1=len(Tuple_List1)
print("Length of the Tuple :",Tuple_fun1)
#Out Put
#Length of the Tuple : 9

Tuple_List1 = [10, 20, 30,40, 50, 60,70, 80, 90]
Tuple_fun1=count(Tuple_List1)
print("Length of the Tuple :",Tuple_fun1)