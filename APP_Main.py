import time

UD = {"JSmith": {"Password": {"1234": "John Smith"}}, }
CU = ""
def UsrMenu():
    global CU
    UMM = 0
    while UMM != 1:
        print('\x1bc')
        print("Welcome, "+CU)
        print(" ______________________________________")
        print("|TABS:    |[1]Account|[2]Stores|[3]Cart|")
        print("")
        print("")
        print("")
        print("")
        print("")
        print(UD)
        
        UC = input()
def LoginScr():
    global CU
    LM = 0
    print(UD)
    print(UD.keys)
    
    while LM != 1:
        print("Welcome user!")
        print("")
        print("[1] Login")
        print("[2] Sign up")
        print("")
        UC = input("Select a number: ")
        print('\x1bc')
        if(UC == "1"):
            #print(UD)
            print("This is the login screen.")
            print("")
            print("Enter your username:")
            UN = input()
            print("")
            print("Enter your password:")
            UP = input()
            
            if(UN in UD.keys() and UP in UD[UN]["Password"].keys()):
                print('\x1bc')
                CU = UD[UN]["Password"][UP]
                print("Logging in...")
                time.sleep(0.5)
                UsrMenu()
                print("")
            else:
                print("")
                print("Incorrect Username or Password!")


        elif(UC == "2"):
            SM = 0
            while SM != 1:
                print('\x1bc')
                print("This is the sign up screen.")
                print("")
                print("Welcome New User!")
                print("")
                print("Create a username:")
                NUN = input()
                if len(NUN) == 0:
                    print("Error! Username cannot be blank")# or a number!")
                    time.sleep(1)
                else:
                    print("Enter your password:")
                    NUP = input()
                    print("")
                    print("Enter your name(EX: John Smith):")
                    NN = input()
                    UD[NUN] = {"Password": {NUP: NN}}
                    
                    LoginScr()
#print(UD["JSmith"]["Password"].keys())


LoginScr()
#UsrMenu()
