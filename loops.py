#  for loop
# a =range(1,20,2)
# for i in a:
    #print(i)
# for i in range(2):
#     print(i)
# q1:- 20 to 51
# for i in range(20,52):
#     print(i)

# q2:- 16 to 1
# for i in range(16,0,-1):

# question 3:- print table of 8
#for i in range(8,81,8):
 #   print(i)

# n= int(input("which table you want to print:-"))
# for i in range(n,(n*10)+1,n):
#     print(i)
# how to print string
# a= "Nitesh is a good boy"
# for i in range(len(a)):
#     print (a[i])
# a= "Nitesh is a good boy"
# for i in a:
#     print(i)

    # break continue else

# for i in range(1,21):
#     if i== 15:
#         break
#     else:
#         print(i)


# for i in range(1,21):
#     if i== 15:
#         continue
#     else:
#         print(i)


# question 1:- accept an integer and print hello world n times
# n=int(input("plzz enter the number:-"))
# for i in range(n):
#     print("Hello World")

#question 2:-print natural numbers from 1 to n
# n=int(input("plzz enter the number:-"))
# for i in range(1,n+1):
#     print(i)

#question 3:-print reverse afor loop.print n to 1
# n=int(input("plzz enter the number:-"))
# for i in range(n,0,-1):
#     print(i)

# quest 4:- print a table of a number accepted from the user
# n=int(input("plzz enter the number:-"))
# for i in range(n,(n*10)+1,n):
#     print(i)
# n = int(input("plzz enter the number:-"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# question 5:- print the sum of first n natural numbers
# n=int(input("plzz enter the number:-"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(f"the sum of first {n} natural numbers is {sum}")

# question 6:- print the sum of first n even numbers
# n=int(input("plzz enter the number:-"))
# sum=0
# for i in range(2,n*2+1,2):
#     sum=sum+i
# print(f"the sum of first {n} even numbers is {sum}")

#question 7:- print the sum of first n odd numbers
# n=int(input("plzz enter the number:-"))
# sum=0     
# for i in range(1,n*2+1,2):    
#     sum=sum+i
# print(f"the sum of first {n} odd numbers is {sum}")

# qustion 8:- factorial of a number
# n=int(input("plzz enter thre number:-"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"the factorial of {n} is {fact}")

# Question 9:-print the sum of all even and odd numbers in a range seprately
# n=int(input("plzz enter the numnber:-"))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even=even+i
#     else:
#         odd=odd+i
# print(f" the sum of even and odd number are {even} and {odd}")

# question 10:-print all the factors of a number
# n=int(input("plzz enter the number:-"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# question 11:-accept a number and check it a perfect number or not
# n=int(input("plzz enter the number:-"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("The number is a perfect number")
# else:
#     print("The number is not a perfect number")
       
    
#question 12:- accept a number and check it a prime number or not
# n=int(input("plzz enter the number:-"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count= count + 1
# if count==2:
#     print("The number is a prime number")
# else:
#     print("The number is not a prime number")

# Question 13:-reverse a string without using built-in function
# a="Nitesh is a good boy"
#b= ""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# print(b)
# question 14:- accept a string from the user and check it a palindrome or not
# a="naman"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# if a==b:
#     print("The string is a palindrome")

    # question 15:- accept a string from the user and print the number of vowels and consonants in it
# a="Nitesh is a good boy"
# vowels=0
# consonants=0
# for i in a:
#     if i in "aeiouAEIOU":
#         vowels=vowels+1
#     elif i.isalpha():
#         consonants=consonants+1
# print(f"The number of vowels in the string is {vowels} and the number of consonants in the string is {consonants}")
a="sghtybs12345@#$%^&U"
char=0
digit=0
special=0
for i in a:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        char+=1
    else:
        special+=1
        print(f"your digit are {digit} and your char are {char} and your special char are {special}")