# the loop control statement are used to change a loop execution from its normal sequence
# they are break, continue and pass 

# continue skips to the next iteration
# break terminates the loop entrely
# and pass does nothing, it just acts as a placeholder

# numbers = [8,2,2,2,2]
# for i in  numbers:
#     if i == 8:
#         continue
#     print("*"* i)
# secret_number = 9
# while True:
#     user = int(input("please enter a number from 0-9"))
#     if user == secret_number:
#         print("you won")
        # break
for i in range(1,12):
    if i == 6:
        pass
#     else:
#         print(i)


# for i in range(1,30):
#         if i % 2 == 0:
#             print(i)

# for i in range(1,30):
#         if i % 2 != 0:
#             print(i)
# for i in range(10,20):
#     if i % 100 != 0:
#         print(i)

for i in range(10,20):
    if i % 2 == 0:
        print(str(i), "is an even number")



    

