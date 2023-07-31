age = int(input("what is your age "))
if age >= 18:
    print("you are an adult")
elif age < 18 and age > 0:
    print("you are a child")
else:
    print("you have not been born yet")