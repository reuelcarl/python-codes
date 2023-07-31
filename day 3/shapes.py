# numbers = [2,2,2,2,8]
# for i in numbers:
#     print("*"* i)

# numbers = [8,2,2,8,2,2] 
# for i in numbers:
#     print("*"* i)

# numbers = [8,2,2,8,2,2,8]
# for i in numbers:
#     print("*"* i)

# numbers = [8,2,2,8,2,2,8]
# for i in numbers:
#     print("*" * i)
# str="";
# for row in range(0,7):
#     for col in range(0,7):
#         if(col == 1 or col == 5)or(row == 3 and col > 1 and col < 6):
#             str=str+"*"
#         else:
#             str=str+" "
#             str=str+"\n"
#             print("*" * col , "  " )

rows = int(input("Enter H Star Pattern Rows = "))
print("====The H Star Pattern====")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end = '')
    for k in range(i * 2, rows * 2):
        print(end = ' ')
    for l in range(1, i + 1):
        print('*', end = '')
    print()

for i in range(1, rows):
    for j in range(rows - 1, i - 1, -1):
        print('*', end = '')
    for k in range(1, i * 2 + 1):
        print(end = ' ')
    for l in range(rows - 1, i - 1, -1):
        print('*', end = '')
    print()




# lets print A
# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str)



# def personal_details():
#     name, age = "reuel", 12
#     address ="paradise , estate , rivers state"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# personal_details()