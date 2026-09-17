# a=int(input("enter your no"))
# b=int(input("enter your no"))
# s=a+b
# print(s)

# a=int(input("Enter your first number: "))
# b=int(input("Enter your second number: "))
# c=int(input("Enter your third number: "))
# avg=(a+b+c)/3
# print(avg)

# price=int(input("Enter the price of the product"))
# quantity=int(input("Enter the quantity of the product"))
# t=price*quantity
# print(t)

# name=input("Enter your name")
# age=int(input("Enter your age"))
# marks=int(input("Enter your marks"))
# print(name,age,marks)

# a=10
# b=90
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# english=int(input("Enter your english marks"))
# maths=int(input("Enter your maths marks"))
# science=int(input("Enter your science marks"))
# hindi=int(input("Enter your hindi marks"))
# ip=int(input("Enter your ip marks"))
# marks=500
# print(english+maths+science+hindi+ip/marks*100)

# a=input("Enter the first number: ")
# b=input("Enter the second number: ")
# a,b = b,a
# print(a,b)

# n=int(input("Enter a number: "))
# if n<18:
#     print("You are not eligible to vote")
# elif n==18:
#     print("You are eligible to vote")
# elif n>18:
#     print("You are eligible to vote")
# else:
#     print(" you are not eligible to vote")            

# n=int(input("Enter a number: "))
# if n>0:
#     print("The number is positive")
# elif n<0:
#     print("The number is negative")
# else:
#     print("The number is zero")
            
# n1=int(input("Enter a number: "))
# n2=int(input("Enter a number: "))
# if n1>n2:
#     print("The first number is greater than the second number")
# elif n1<n2:
#     print("The second number is greater than the first number")
# else:
#     print("Both numbers are equal")

# english=int(input("Enter your english marks"))
# maths=int(input("Enter your maths marks"))
# science=int(input("Enter your science marks"))
# hindi=int(input("Enter your hindi marks"))
# total_marks=english+maths+science+hindi
# p=(total_marks/400)*100
# print(p)
# if p>=90:
#     print("A grade")
# elif p>=80:
#     print("B grade")
# elif p>=70:
#     print("C grade")
# elif p>=60:
#     print("D grade")
# elif p>=50:
#     print("E grade")
# else:
#     print("F grade")        
    
# name=input("Enter your name: ")
# print("Hello",name,)

# length=int(input("Enter the length of the rectangle: "))
# breadth=int(input("Enter the breadth of the rectangle: "))
# area=length*breadth
# perimeter=2*(length+breadth)
# print(area)          
# print(perimeter)          

# n= int(input("Enter a number "))
# if n%5==0:
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 5")
    
# n=input("enter your name ")
# print(n*5)
  
# n=int(input("Enter a number: "))
# if n<10:
#     print("its a single digit number")  
# elif n<100:
#     print("its a two digit number")

            
# n=int(input("Enter a number: "))
# print(n*2)        

# n=input("Enter your color: ")
# if n=="red":
#     print("stop")       
# elif n=="yellow":
#     print("wait")    
# elif n=="green":
#     print("go")
# else:
#     print("invalid color")
        
# n1=int(input("Enter a number: "))
# n2=int(input("Enter a number: "))
# print(n1*n2)       

# armstrong number
# n=int(input("Enter a number: "))
# x=n
# s=0                                             
# while n>0:
#     r=n%10
#     s=s+r**3
#     n=n//10
# print("armstrong" if s==x else "not armstrong")

#palindrome number
# n=int(input("Enter a number: "))
# x=n
# s=0
# while n>0:
#     r=n%10
#     s=s*10+r
#     n=n//10
# print("palindrome" if s==x else "not palindrome")

#fibonacci series
# n=int(input("Enter a number: "))
# a=0
# b=1
# while n>0:
#     print(a)
#     a,b=b,a+b
#     n-=1

# digit frequency

# n = int(input("Enter a number: "))

# for i in range(10):
#     count = 0
#     temp = n

#     for j in range(10):
#         digit = temp % 10

#         if digit == i:
#             count += 1

#         temp = temp // 10

#     if count > 0:
#         print(i, "=", count)

#   second largest number
# numbers = [45, 12, 89, 34, 67, 90, 56]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# second = numbers[0]

# for num in numbers:
#     if num > second and num != largest:
#         second = num

# print("Second largest =", second)

a=int(input("Enter a  first number: "))
b=int(input("Enter a second number: "))
while True:
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("5 exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a/b)
    elif choice==5:
        break
    else:
        print("invalid choice")