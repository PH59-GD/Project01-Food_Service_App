import time
UD = {"JSmith": {"Name": "John Smith", "Password": "1234", "Cart": [], "UName": "JSmith"}, } #Dictonary of customers
BD = {"TWells": {"Name": "Tom Wells", "Password": "5678", "Business": "Tom's Diner", "Cart": [] }, } #Dictonary of Business Owners
AD = {"PHammel": {"Name": "Payton Hammel", "Password": "1010", "Cart": []}, "BEthier": {"Name": "Brian Ethier", "Password": "1100", "Cart": []} } #Dictonary of Admins
NPS = []
LS = ["Tom's Diner"]
DL = []
CU = "" #Current User's name
BN = "" #Current Business's name
def AdmMenu():
    global CU
    global NPS
    global LS
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
        elif UC == "1":
            
            AM = 0
            while AM != 1:
                print('\x1bc')
                print("|"+CU+"'s"+" Account|")
                print("")
                print("[1]Change Username")
                print("[2]Change Password")
                print("[3][ADD EXTRA FUNCTION HERE]")
                print("[4]Back")
                print("")
                AC = input("Input: ")
                if(AC == "4"):
                    AM += 1
        elif UC == "2":
            
            SM = 0
            while SM != 1:
                print('\x1bc')
                print("| "+str(len(DL))+" Stores found |")
                print("")
                print("[LIST OF STORES HERE]")
                print("")
                print("[0]Back")
                print("")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1
        elif UC == "3":
            
            SM = 0
            while SM != 1:
                print('\x1bc')
                print(UD[CU]["Cart"])
                print("")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1
        elif UC == "5":
            BMM = 0
            while BMM != 1:
                print("Business Management")
                print("")
                if(len(NPS) > 0):
                    print("Unapproved Businesses:")
                    print(NPS)


                else:
                    print("No unapproved businesses.")
                print("")
                if(len(LS) > 0):
                    print("Approved Businesses:")
                    print(LS)

                else:
                    print("No approved businesses.")
                print("[0] Back")
                UI = input("Input: ")
                if(UI == "0"):
                    BMM += 1
def BusMenu():
    global CU
    global BN
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
            BN = ""
            LoginScr()
        elif UC == "1":
            
            AM = 0
            while AM != 1:
                print('\x1bc')
                print("|"+CU+"'s"+" Account|")
                print("")
                print("[1]Change Username")
                print("[2]Change Password")
                print("[3][ADD EXTRA FUNCTION HERE]")
                print("[4]Back")
                print("")
                AC = input("Input: ")
                if(AC == "4"):
                    AM += 1
        elif UC == "2":
            print('\x1bc')
            SM = 0
            while SM != 1:
                print('\x1bc')
                print("| "+str(len(DL))+" Stores found |")
                print("")
                print("[LIST OF STORES HERE]")
                print("")
                print("[0]Back")
                print("")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1
        elif UC == "3":
            
            SM = 0
            while SM != 1:
                print('\x1bc')
                print(UD[CU]["Cart"])
                print("")
                print("[0]Back")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1
        elif UC == "5":
            
            SM = 0
            while SM != 1:
                print('\x1bc')
                print("Management for: "+BN)
                print("Overview:")
                print("[STATS HERE]")
                print("[0]Back")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1
def UsrMenu():
    global CU
    UMM = 0
    while UMM != 1:
        print('\x1bc')
        print("Welcome, "+UD[CU]["Name"])
        print(" ________________________________________________")
        print("|TABS:    |[1]Account|[2]Stores|[3]Cart|[4]Logout|")
        print("")
        print("")
        print("")
        print("")
        print("")
        
        
        UC = input("Input: ")
        if UC == "4":
            CU = ""
            LoginScr()
        elif UC == "1":
            
            AM = 0
            while AM != 1:
                print('\x1bc')
                print("|"+CU+"'s"+" Account|")
                print("")
                print("[1]Change Username")
                print("[2]Change Password")
                print("[3][ADD EXTRA FUNCTION HERE]")
                print("[4]Back")
                print("")
                AC = input("Input: ")
                if(AC == "4"):
                    AM += 1
        elif UC == "2":
            
            SM = 0
            while SM != 1:
                print('\x1bc')
                print("| "+str(len(DL))+" Stores found |")
                print("")
                print("[LIST OF STORES HERE]")
                print("")
                print("[0]Back")
                print("")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1
        elif UC == "3":
            
            SM = 0
            while SM != 1:
                print('\x1bc')
                
                print(UD[CU]["Cart"])
                print("")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1
def LoginScr():
    global CU
    global BN
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
                print('\x1bc')
                print("Welcome Customer!")
                print("")
                print("Enter your username:")
                UN = input("Input: ")
                print("")
                print("Enter your password:")
                UP = input("Input: ")
                if(UN in UD.keys() and UD[UN]["Password"] == UP): 
                    print('\x1bc')
                    CU = UD[UN]["UName"] 
                    print("Logging in...")
                    time.sleep(0.5)
                    UsrMenu()
            elif(UC == "2"):
                print('\x1bc')
                print("Welcome Business Owner!")
                print("")
                print("Enter your username:")
                UN = input("Input: ")
                print("")
                print("Enter your password:")
                UP = input("Input: ")
                if(UN in BD.keys() and BD[UN]["Password"] == UP): 
                    print('\x1bc')
                    CU = BD[UN]["Name"] 
                    BN = BD[UN]["Business"]
                    print("Logging in...")
                    time.sleep(0.5)
                    BusMenu()
            elif(UC == "3"):
                print('\x1bc')
                print("Welcome Admin!")
                print("")
                print("Enter your username:")
                UN = input("Input: ")
                print("")
                print("Enter your password:")
                UP = input("Input: ")
                if(UN in AD.keys() and AD[UN]["Password"] == UP): 
                    print('\x1bc')
                    CU = AD[UN]["Name"] 
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
                print("[1]Customer")
                print("[2]Business")
                print("")
                UC = input("Input: ")
                if (UC == "1"):
                    print('\x1bc')
                    print("Welcome new customer!")
                    print("Fill out the information below to create an account.")
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
                        UD[NUN] = {"Name": NN, "Password": NUP, "Cart": []} #Creating a new user for the UD dictonary 
                        print("Creating new account...")
                        time.sleep(0.5)
                        LoginScr()
                if (UC == "2"):
                    print('\x1bc')
                    print("Welcome business owner!")
                    print("Fill out the information below to create an account.")
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
                        print("")
                        print("Enter your business's name:")
                        NBN = input()
                        BD[NUN] = {"Name": NN, "Password": NUP, "Business": NBN, "Cart": []} #Creating a new user for the UD dictonary 
                        NPS.append[NBN]
                        print("Creating new account...")
                        time.sleep(0.5)
                        LoginScr()

LoginScr()
#CU = "name"
#UsrMenu()
