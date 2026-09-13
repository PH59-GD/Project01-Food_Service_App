import time
UD = {"JSmith": {"Password": {"1234": "John Smith"}}, } #Dictonary of customers
BD = {"TWells": {"Password": {"5678": {"Tom Wells": "Tom's Diner"}}}, } #Dictonary of Business Owners
BDN = {"TWells": "Tom Wells"} #Business Owner names
AD = {"PHammel": {"Password": {"1010": "Payton Hammel"}}, "BEthier": {"Password": {"1100": "Brian Ethier"}} } #Dictonary of Admins
#print(BD["TWells"]["Password"]["5678"]["Tom Wells"])

CU = "" #Current User's name
def AdmMenu():
    global CU
    UMM = 0
    while UMM != 1:
        print('\x1bc')
        print("Welcome, "+CU)
        print(" __________________________________________________________________________________________")
        print("|TABS:    |[1]Account|[2]Stores|[3]Cart|[4]Logout|[5]Business Management|[6]User Management|")
        print("")
        print("")
        print("")
        print("")
        print("")
        
        
        UC = input()
        if UC == "4":
            CU = ""
            LoginScr()
def BusMenu():
    global CU
    UMM = 0
    while UMM != 1:
        print('\x1bc')
        print("Welcome, "+CU)
        print(" _____________________________________________________________________")
        print("|TABS:    |[1]Account|[2]Stores|[3]Cart|[4]Logout|[5]Business Overview|")
        print("")
        print("")
        print("")
        print("")
        print("")
        
        
        UC = input()
        if UC == "4":
            CU = ""
            LoginScr()
def UsrMenu():
    global CU
    UMM = 0
    while UMM != 1:
        print('\x1bc')
        print("Welcome, "+CU)
        print(" ________________________________________________")
        print("|TABS:    |[1]Account|[2]Stores|[3]Cart|[4]Logout|")
        print("")
        print("")
        print("")
        print("")
        print("")
        
        
        UC = input()
        if UC == "4":
            CU = ""
            LoginScr()
def LoginScr():
    global CU
    LM = 0
    #print(UD)
    #print(UD.keys)
    while LM != 1: #Welcome screen
        print('\x1bc')
        print("Welcome user!")
        print("")
        print("[1] Login")
        print("[2] Sign up")
        print("")
        UC = input("Select a number: ")
        print('\x1bc')
        if(UC == "1"):
            print('\x1bc')
            print("This is the login screen.") #Login screen
            print("")
            print("[1]Customer")
            print("[2]Business")
            print("[3]Administrator")
            print("")
            UC = input("Input: ")
            if(UC == "1"):
                print("Welcome Customer!")
                print("")
                print("Enter your username:")
                UN = input("Input: ")
                print("")
                print("Enter your password:")
                UP = input("Input: ")
                if(UN in UD.keys() and UP in UD[UN]["Password"].keys()): #Checks to see that the username is a key, and then checks for the matching password
                    print('\x1bc')
                    CU = UD[UN]["Password"][UP] #Retrieves the current user's name to be displayed
                    print("Logging in...")
                    time.sleep(0.5)
                    UsrMenu()
            elif(UC == "2"):
                print("Welcome Business Owner!")
                print("")
                print("Enter your username:")
                UN = input("Input: ")
                print("")
                print("Enter your password:")
                UP = input("Input: ")
                if(UN in BD.keys() and UP in BD[UN]["Password"].keys()): #Checks to see that the username is a key, and then checks for the matching password
                    print('\x1bc')
                    if BDN[UN] in BD[UN]["Password"][UP].keys(): 
                        CU = BDN[UN] #Retrieves the current user's name to be displayed
                        print("Logging in...")
                        time.sleep(0.5)
                        BusMenu()
            elif(UC == "3"):
                print("Welcome Admin!")
                print("")
                print("Enter your username:")
                UN = input("Input: ")
                print("")
                print("Enter your password:")
                UP = input("Input: ")
                if(UN in AD.keys() and UP in AD[UN]["Password"].keys()): #Checks to see that the username is a key, and then checks for the matching password
                    print('\x1bc')
                    CU = AD[UN]["Password"][UP] #Retrieves the current user's name to be displayed
                    print("Logging in...")
                    time.sleep(0.5)
                    AdmMenu()
            else:
                print("")
                print("Incorrect Username or Password!")
        elif(UC == "2"):
            SM = 0
            while SM != 1: #The sign up screen
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
                    UD[NUN] = {"Password": {NUP: NN}} #Creating a new user for the UD dictonary 
                    LoginScr()
LoginScr()
#UsrMenu()
