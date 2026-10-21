import streamlit as st
import pickle
class User:
    def __init__(self):
        self.Username = ""
        self.Name = ""
        self.Password = ""
        self.Cart = []
    def Create_New_user(self, UName, Pass, UsrName):
        self.Username = UName
        self.Name = UsrName
        self.Password = Pass
        self.Cart = []
class BusinessOwner:
    def __init__(self):
        self.Username = ""
        self.Name = ""
        self.Password = ""
        self.Cart = ""
        self.Business = ""
    def Create_New_businessO(self, UName, Pass, UsrName, BusinessName):
        self.Username = UName
        self.Name = UsrName
        self.Password = Pass
        self.Business = BusinessName
        self.Cart = []
class Admin:
    def __init__(self):
        self.Username = ""
        self.Name = ""
        self.Cart = ""
    def Create_New_Admin(self, UName, Pass, UsrName):
        self.Username = UName
        self.Name = UsrName
        self.Password = Pass
        self.Cart = []

UD = {"JSmith": {"Name": "John Smith", "Password": "1234", "Cart": [], "UName": "JSmith"}, } #Dictonary of customers
BD = {"TWells": {"Name": "Tom Wells", "Password": "5678", "Business": "Tom's Diner", "Cart": [] }, } #Dictonary of Business Owners
AD = {"PHammel": {"Name": "Payton Hammel", "Password": "1010", "Cart": []}, "BEthier": {"Name": "Brian Ethier", "Password": "1100", "Cart": []} } #Dictonary of Admins
NPS = []
LS = ["Tom's Diner"]
DL = []
CU = "" #Current User's name
BN = "" #Current Business's name

def LoginScr(username, password):
    global CU, BN

    if username in UD:
        if password == UD[username]["Password"]:
            CU = UD[username]["Name"]
            BN = ""

            st.success("Login Successful")
            st.write(f"Welcome, {CU}!")
            return

    elif username in BD:
        if password == BD[username]["Password"]:
            CU = BD[username]["Name"]
            BN = BD[username]["Business"]

            st.success("Login Successful")
            st.write(f"Welcome, {CU}!")
            st.write(f"Business: {BN}")
            return

    elif username in AD:
        if password == AD[username]["Password"]:
            CU = AD[username]["Name"]
            BN = ""

            st.success("Login Successful")
            st.write(f"Welcome, Admin {CU}!")
            return

    st.error("Login Failed")
    st.write("Invalid username or password.")

def SignUp(username, password, full_name):
    if not username or not password or not full_name:
        st.error("Please fill out all fields")
        return

    if username in UD or username in BD or username in AD:
        st.error("That username already exists, please choose another one.")
        return

    NUser = User()  
    NUser.Create_New_user(username, password, full_name)
    file1 = open("Users.dat", "ab")
    pickle.dump(NUser, file1)
    file1.close()

    st.success("Account created successfully!")
    st.write(f"Welcome, {full_name}!")
    st.info("You can now return to Login Screen and log in.")

def BusinessSignUp(username, password, full_name, business_name):
    if not username or not password or not full_name or not business_name:
        st.error("Please fill out all fields")
        return

    if username in UD or username in BD or username in AD:
        st.error("That username already exists, please choose another one.")
        return

    NBusinessO = BusinessOwner()
    NBusinessO.Create_New_businessO(username, password, full_name, business_name)
    file2 = open("BusinessOwners.dat", "ab")
    pickle.dump(NBusinessO, file2)
    file2.close()

    

    st.success("Business account created successfully!")
    st.write(f"Welcome, {full_name}!")
    st.write(f"Business: {business_name}")
    st.info("You can now return to Login and log in.")




st.set_page_config(
    page_title="Login",
    layout="centered",
)

st.markdown("""
<style>
    .stApp {
        background-color: lightblue;
    }

    .login-title {
        font-family: Georgia;
        font-size: 64px;
        text-align: center;
        color: black;
    }

    .stTextInput label {
        font-family: Georgia;
        font-size: 24px;
    }

    .stTextInput input {
        font-family: Georgia;
        font-size: 24px;
    }

    .stButton button {
        font-family: Georgia;
        font-size: 32px;
    }

   
</style>
""", unsafe_allow_html=True)

if "screen" not in st.session_state:
    st.session_state.screen = "welcome"


if st.session_state.screen == "welcome":
    st.title("Welcome!")
    st.write("Please Log In or Sign Up")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            st.session_state.screen = "login"
            st.rerun()

    with col2:
        if st.button("Sign Up"):
            st.session_state.screen = "signup"
            st.rerun()


elif st.session_state.screen == "login":

    st.markdown(
        '<div class="login-title">Login</div>',
        unsafe_allow_html=True
    )

    username = st.text_input(
        "Username",
        key="login_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login", key="login_button"):

        # Don't allow empty login information
        if not username or not password:
            st.error("Please enter a username and password.")
        else:
            LoginScr(username, password)

    if st.button("Back"):
        st.session_state.screen = "welcome"
        st.rerun()

    if st.button("Create an Account"):
        st.session_state.screen = "signup"
        st.rerun()

elif st.session_state.screen == "signup":

    st.markdown(
        '<div class="login-title">Sign Up</div>',
        unsafe_allow_html=True
    )

    account_type = st.radio(
        "Account Type",
        ["Customer", "Business Owner"]
    )

    new_name = st.text_input(
        "Full Name",
        key="signup_name"
    )

    new_username = st.text_input(
        "Username",
        key="signup_username"
    )

    new_password = st.text_input(
        "Password",
        type="password",
        key="signup_password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        key="confirm_password"
    )

    business_name = ""

    if account_type == "Business Owner":
        business_name = st.text_input(
            "Business Name",
            key="business_name"
        )

    if st.button("Sign Up", key="signup_button"):

        if not all([
            new_name,
            new_username,
            new_password,
            confirm_password
        ]):
            st.error("Please fill out all of the fields.")

        elif new_password != confirm_password:
            st.error("Passwords do not match.")

        elif account_type == "Business Owner" and not business_name:
            st.error("Please enter your business name.")

        elif account_type == "Customer":

            SignUp(
                new_username,
                new_password,
                new_name
            )

        elif account_type == "Business Owner":

            BusinessSignUp(
                new_username,
                new_password,
                new_name,
                business_name
            )
