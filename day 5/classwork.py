# 1. WRITE A PYTHON PROGRAM TO PRINT ALL THE EVEN NUMBERS FROM 1 TO 50 USING A FOR LOOP
# 2.CREATE A WHILE LOOP THAT PRINTS NUMBERS FROM 10 TO 1 IN REVERSE ORDER.
# 3.WRITE A PROGRAM THAT CALCULATES THE SUM OF ALL NUMBERS FROM 1 TO 100 USING A FOR Loop
# 4. CREATE A PROGRAM THAT TAKES A POSITIVE INTERGER AS INPUT AND PRINTS ITS MULTIPLICATION TABLE USING A WHILE LOOP
# 5. WRITE A PYTHON PROGRAM TO FIND THE FACTORIAL OF GIVEN NUMBER USING FOR LOOP 

#              answer 1
# def even():
#     for i in range(1,50):
#         if i % 2 == 0:
#             print(i)


# even()


            #  answer 2
def reverse():
     i = 10
     while i > 0:
        print(i)
        i = i - 1

reverse()


#       answer 3
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)



#        answer 4
# num = int(input ("Enter the number: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num*i}")
#     i += 1
    


#       answer 5
# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         while(n > 1):
#             fact *= n
#             n -= 1
#         return fact
# num =int(input("input the number "))
# print("Factorial of",num,"is",
# factorial(num))
 