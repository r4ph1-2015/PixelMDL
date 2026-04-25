import time
def hello():
    print("Hello World!")

def sprint():
    print("What should be printed")
    text = input()

    print("How many times would you like to repeat")
    amount = int(input())  

    for i in range(amount):
        time.sleep(0.05)
        print(text)

def quiz():
    answer1 = input("What is your Name?")
    print("Hello",answer1,",Nice to meet you")
    answer2 = input("What is the capital of Germany")
    if answer2 == "Berlin":
        print("That is correct")
    else:
        print("Incorrect")
    
    answer3 = input("What coding language do you think this module was built in?")
    if answer3 == "Python":
        print("That is correct, Thank you for trying out the Quiz Function")
    else:
        print("Thats is incorrect but Thank you for trying out the Quiz Function...")
