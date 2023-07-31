import random


# names = ["melech", "reuel","abraham"]
# who_will_pay = random.choice(names)
# print(who_will_pay)

# x = random.randint(1,6)
# y = random.randint(1,6)


# def main():
#     who_pays()
#     car_motion
#     hello()


def who_pays():
    while True:
        names = ["melech", "reuel","abraham "]
        who_will_pay = random.choice(names)
        print(who_will_pay)
        again = input("wanna play again? yes or no ").title()
        if again == "No":
            break
    print("thanks for your time!!! ")


who_pays()


# def car_motion():
#     print("you have started the car")
#     stop = input("wanna stop the car? Yes or No: ").title()
#     if stop == 'Yes':
#         print("you have stoped the car")
#     else:
#         print("keep going")


# def hello():
#     name = input("please enter your name ")
#     mode = input("are you happy ")
#     if mode == 'No':
#         print("you are not nice")
#     else:
#         print("God bless you richily  🤣😂")



# if __name__ == "__main__":
#     main()