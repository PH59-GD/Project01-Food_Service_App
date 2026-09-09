import time
UD = {"JSmith": 1234}
def LoginScr():
    LM = 0
    while LM != 1:
        print("Welcome user!")
        print("")
        print("[1] Login")
        print("[2] Sign up")
        print("")
        UC = input("Select a number: ")

        if(UC == "1"):
            #print(UD)
            print("This is the login screen.")
            print("")
            print("Enter your username:")
            UN = input()
            print("")
            print("Enter your password:")
            UP = input()
            if(UN in UD.keys() and int(UP) == UD[UN]):
                print("Logging in...")
                print("")
            else:
                print("")
                print("Incorrect Username or Password!")


        elif(UC == "2"):
            SM = 0
            while SM != 1:
                print("This is the sign up screen.")
                print("")
                print("Welcome New User!")
                print("")
                print("Create a username:")
                NUN = input()
                if len(NUN) == 0:
                    print("Error! Username cannot be blank")# or a number!")
                else:
                    print("Enter your password:")
                    NUP = input()


LoginScr()