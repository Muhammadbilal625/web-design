
x=676
y=8
print(x,y)
tuple = ("exo",78, "programing")
print(tuple)
set= {"example", "bilal", 565}
print(set)
list=[56, "exo", 67]
print(list)
dictionary = {
    "age":34,
        "name":bilal
        }
print(dictionary)
print(dictionary["name"])
x1=int(input("Enter first number:"))
x2=int(input("Enter 2nd number:"))
x3=int(input("Enter 3rd number:"))
x4=int(input("Enter forth number:"))
x5=int(input("Enter 5th number:"))
list=[x1,x2,x3,x4,x5]
print(list)
print("Sorted list")
print(sorted(list))  



marks=int(input("Enter your marks:"))
if(marks>=80):
    print("Your Grade is A")
elif(marks>=70):
    print("Your Grade is b")
elif(marks>=60):
    print("Your Grade is c")
elif(marks>=50):
    print("Your Grade is d")
else:
    print("You are fail and your grade is D")

#nested for loop
for i in range (0,7):
    print(i)
    a=[1,2,3]
    for item in a:
        print(a)
    else:
        print("Done")
for i in range(0,80):
    print(i)
    if i==3:
        break
    for i in range(4):
        print("hello")
        if i==2:
            continue
        print(i)
i= 2
while i < 7:
    print(i)
    if i == 3:
        break
    i+= 3   
#function 
def my_fun():
    print("this is function")     
my_fun()

m1=int(input("Enter first marks:"))
m2=int(input("Enter 2nd marks:"))
m3=int(input("Enter 3rd marks:"))
marks=(m1+m2+m3)//3
print(marks)
if(m1<33 & m2<33 & m3<33 ):
    print(" sorry! You are fail ")
elif((m1+m2+m3)/3>=33):
    print(" Congratulations You are pass")
    if(marks>=80):
        print("Your Grade is A")
    elif(marks>=70):
        print("Your Grade is b")
    elif(marks>=60):
        print("Your Grade is c")
    elif(marks>=50):
        print("Your Grade is d")
    else:
        print("You are fail and your grade is D")
    

