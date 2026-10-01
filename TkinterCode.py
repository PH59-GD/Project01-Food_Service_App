import tkinter as tk
from tkinter import ttk, messagebox

UD = {"JSmith": {"Password": {"1234": "John Smith"}}, } #Dictonary of customers
BD = {"TWells": {"Password": {"5678": {"Tom Wells": "Tom's Diner"}}}, } #Dictonary of Business Owners
BDN = {"TWells": "Tom Wells"} #Business Owner names
AD = {"PHammel": {"Password": {"1010": "Payton Hammel"}}, "BEthier": {"Password": {"1100": "Brian Ethier"}} } #Dictonary of Admins
#print(BD["TWells"]["Password"]["5678"]["Tom Wells"])
DL = []
CU = "" #Current User's name
BN = "" #Current Business's name

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
                print("[CART HERE]")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1

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
                print("[CART HERE]")
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
        print("Welcome, "+CU)
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
                print("[CART HERE]")
                AC = input("Input: ")
                if(AC == "0"):
                    SM += 1
def LoginScr():
   window = tk.TK()

    window.title("Login")
    
    
