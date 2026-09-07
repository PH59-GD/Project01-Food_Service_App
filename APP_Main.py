import time
UD = {"JSmith": 1234}
LM = 0
while LM != 1:
    print("Welcome user!")
    print("")
    print("[1] Login")
    print("[2] Sign up")
    print("")
    UC = input("Select a number: ")
    if(UC == "1"):
        print("This is the login screen.")
        print("")
        print("Enter your username:")
        UN = input()
        print("")
        print("Enter your password:")
        UP = input()

    elif(UC == "2"):
        print("This is the sign up screen.")
time.sleep(60)