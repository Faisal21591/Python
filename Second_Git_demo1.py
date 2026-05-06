#Example-1 Variable
a=10
b=20
print(a,b)
#Out Put will --- 10 20
#
#Example-2 Variable: Check Memory Location
a=20
b=20
print(a,b)
print(id(a),id(b))
#Out Put will be ---
# 20 20 variable "a" is overwritten previously it was 10 now it is 20 & It will
# remain 20 till we chane the value of "a"
# 140723973056008 140723973056008
#Both variable value are safed at same memory location
#It will not take garbage value Kay ake ki ake location bana day ga aur dosri ki
# ake No it is not like that
#
#Example-3
print('a',b,id('a'),id(b))
#Out Put will be--- a 20 140723973119920 140723973056008
#a and b has different memory locations because now 'a' is behaving like string
#
#Example-4
print(a,b,id(a),id(b))
#Out Put will be--- 20 20 140723973056008 140723973056008
#
#Example-5
c= "\'Rise and Shine\'"
print(c)
#Out Put will be --- "Welcome to our College ABC" now when ever we want to print
# this statement we will call "c" Variable any number of time till
# we change the value of variable "c"
#
#Example-6
print("write "+str(a)+ " time College Slogan " + c)
#Out Put will be----
# 'Rise and Shine'
# write 20 time College Slogan 'Rise and Shine'