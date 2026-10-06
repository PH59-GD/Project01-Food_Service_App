import tkinter as tk #Justus says to possibly use streamlit GUI
from tkinter import ttk, messagebox

UD = {"JSmith": {"Password": {"1234": "John Smith"}}, } #Dictonary of customers
BD = {"TWells": {"Password": {"5678": {"Tom Wells": "Tom's Diner"}}}, } #Dictonary of Business Owners
BDN = {"TWells": "Tom Wells"} #Business Owner names
AD = {"PHammel": {"Password": {"1010": "Payton Hammel"}}, "BEthier": {"Password": {"1100": "Brian Ethier"}} } #Dictonary of Admins
#print(BD["TWells"]["Password"]["5678"]["Tom Wells"])
DL = []
CU = "" #Current User's name
BN = "" #Current Business's name

def LoginScr():
    global CU, BN

    username = username_entry.get()
    password = password_entry.get()

    if username in UD:
        if password in UD[username]["Password"]:
            CU = UD[username]["Password"][password]

            messagebox.showinfo(
                "Login Successful",
                f"Welcome, {CU}!"
            )
            return

    if username in BD:
        if password in BD[username]["Password"]:
            business_info = BD[username]["Password"][password]

            for name, business in business_info.items():
                CU = name
                BN = business

            messagebox.showinfo(
                "Login Successful",
                f"Welcome, {CU}! \nBusiness: {BN}"
            )
            return

    if username in AD:
        if password in AD[username]["Password"]:
            CU = AD[username]["Password"][password]

            messagebox.showinfo(
                "Login Successful",
                f"Welcome, Admin {CU}!"
            )
            return

    messagebox.showerror(
        "Login Failed",
        "Invalid username or password."
    )



root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=LoginScr).pack()

root.mainloop()
