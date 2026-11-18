import streamlit as st
import pickle
TEST = [{"Business Name": "Tom's Diner", "Products": {"Apple Pie": 2.99, "Eggs and Bacon": 6.99}, "Description": "A cozy diner located in Siloam Springs Arkansas. Located at 123456 South 1st Street."}, {"Business Name": "Dave's Hardware", "Products": {"Screws": 1.99, "Screwdriver": 8.99}, "Description": "A professional hardware store located in Siloam Springs Arkansas. Located at 253732 North Howard Way."}]
#{"Business Name": "Tom's Diner", "Products": {"Apple Pie": 2.99, "Eggs and Bacon": 6.99}, "Description": "A cozy diner located in Siloam Springs Arkansas. Located at 123456 South 1st Street."}
st.set_page_config(
    page_title="Login",
    layout="centered",
)

if "screen" not in st.session_state:
    st.session_state.screen = "welcome"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "account" not in st.session_state:
    st.session_state.account = None

if "role" not in st.session_state:
    st.session_state.role = None

RLU = []
RLBO = []
RLADMIN = []


class User:
    def __init__(self):
        self.Username = ""
        self.Name = ""
        self.Password = ""
        self.Cart = []
        self.Orders = []
        self.Info = {}

    def Create_New_user(self, UName, Pass, UsrName):
        self.Username = UName
        self.Name = UsrName
        self.Password = Pass
        self.Cart = []
        self.Orders = []
        self.Info = {"User": self.Username, "Name": self.Name, "Password": self.Password,
                     "Cart": self.Cart, "Orders": self.Orders}


class BusinessOwner:
    def __init__(self):
        self.Username = ""
        self.Name = ""
        self.Password = ""
        self.Cart = ""
        self.Business = ""
        self.Products = []
        self.Orders = []
        self.BInfo = {}

    def Create_New_businessO(self, UName, Pass, UsrName, BusinessName):
        self.Username = UName
        self.Name = UsrName
        self.Password = Pass
        self.Business = BusinessName
        self.Cart = []
        self.Products = []
        self.Orders = []
        self.BInfo = {"User": self.Username, "Name": self.Name, "Password": self.Password, "Cart": self.Cart,
                      "Business": self.Business, "Products": self.Products,
            "Orders": self.Orders}


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

class Product:
    def __init__(self):
        self.ProductID = 0
        self.Name = ""
        self.Description = ""
        self.Price = 0.00
        self.Quantity = 0

    def Edit_Product(self):
        self.Name = ""
        self.Description = ""
        self.Price = 0.00
        self.Quantity = 0

    def Delete_Product(self):
        return self.ProductID


#class Order:
 #   def __init__(self):
        self.OrderID = 0
        self.Customer = ""
        self.Business = ""
        self.Items = ""

        self.Total = sum(
            item["Price"] * item["Quantity"]
            for item in Items
        )

        self.Status = "Pending"

   # def Update_Status(self):
        self.Status = NewStatus


try:
    File3 = open("Users.dat", "rb")
    while True:
        try:
            data = pickle.load(File3)

            RLU.append(data)
        except(EOFError):
            break
    File3.close()
except(FileNotFoundError):
    print("")
    print("WARNING! ''Users.dat'' not found!")

try:
    File6 = open("BusinessOwners.dat", "rb")
    while True:
        try:
            data = pickle.load(File6)
            # print(data.USR)
            RLBO.append(data)
        except(EOFError):
            break
    File6.close()
except(FileNotFoundError):
    print("")
    print("WARNING! ''BusinessOwners.dat'' not found!")


AD = {"PHammel": {"Name": "Payton Hammel", "Password": "1010", "Cart": []},
      "BEthier": {"Name": "Brian Ethier", "Password": "1100", "Cart": []}}  # Dictonary of Admins
for username, admin in AD.items():

    admin["User"] = username
    RLADMIN.append(admin)
NPS = []
LS = ["Tom's Diner"]
DL = []
CU = ""  # Current User's name
BN = ""  # Current Business's name
st.write(f" {RLU} ")
st.write(f"{RLBO}")



def LoginScr(username, password):
    global CU, BN

    if len(RLU) > 0 or len(RLBO) > 0 or len(RLADMIN) > 0:
        for i in range(len(RLU)):
            if username == RLU[i]['User']:
                if password == RLU[i]["Password"]:
                    CU = RLU[i]['Name']
                    BN = ""

                    st.success("Login Successful")
                    st.write(f"Welcome, {CU}!")

                    st.session_state.account = RLU[i]
                    st.session_state.role = "Customer"
                    st.session_state.logged_in = True

                    return True

        for d in range(len(RLBO)):
            if username == RLBO[d]['User']:
                if password == RLBO[d]["Password"]:
                    CU = RLBO[d]['Name']
                    BN = RLBO[d]['Business']

                    st.success("Login Successful")
                    st.write(f"Welcome, {CU}!")
                    st.write(f"Business: {BN}")

                    st.session_state.account = RLBO[d]
                    st.session_state.role = "Business Owner"
                    st.session_state.logged_in = True

                    return True

        for k in range(len(RLADMIN)):
            if username == RLADMIN[k]['User']:
                if password == RLADMIN[k]["Password"]:
                    CU = RLADMIN[k]['Name']
                    # BN = ADMIN[k]['Business']
                    st.success("Login Successful")
                    st.write(f"Welcome, {CU}!")

                    st.session_state.account = RLADMIN[k]
                    st.session_state.role = "Admin"
                    st.session_state.logged_in = True

                    return True

    st.error("Login Failed")
    st.write("Invalid username or password.")

    return False

def SignUp(username, password, full_name):
    if not username or not password or not full_name:
        st.error("Please fill out all fields")
        return

    if len(RLU) > 0 or len(RLBO) > 0 or len(RLADMIN) > 0:
        for i in range(len(RLU)):
            if username == RLU[i]['User']:
                st.error("That username already exists, please choose another one.")
                return
        for d in range(len(RLBO)):
            if username == RLBO[d]['User']:
                st.error("That username already exists, please choose another one.")
                return

    NUser = User()
    NUser.Create_New_user(username, password, full_name)
    file1 = open("Users.dat", "ab")
    pickle.dump(NUser.Info, file1)
    RLU.append(NUser.Info)
    file1.close()

    st.success("Account created successfully!")
    st.write(f"Welcome, {full_name}!")
    st.info("You can now return to Login Screen and log in.")


def BusinessSignUp(username, password, full_name, business_name):
    if not username or not password or not full_name or not business_name:
        st.error("Please fill out all fields")
        return

    if len(RLU) > 0 or len(RLBO) > 0 or len(RLADMIN) > 0:
        for i in range(len(RLU)):
            if username == RLU[i]['User']:
                st.error("That username already exists, please choose another one.")
                return
        for d in range(len(RLBO)):
            if username == RLBO[d]['User']:
                st.error("That username already exists, please choose another one.")
                return
        # for k in range(len(RLADMIN)):
        # st.error("That username already exists, please choose another one.")
        # return

    NBusinessO = BusinessOwner()
    NBusinessO.Create_New_businessO(username, password, full_name, business_name)
    file2 = open("BusinessOwners.dat", "ab")
    pickle.dump(NBusinessO.BInfo, file2)
    RLBO.append(NBusinessO.BInfo)
    file2.close()
    st.success("Business account created successfully!")
    st.write(f"Welcome, {full_name}!")
    st.write(f"Business: {business_name}")
    st.info("You can now return to Login and log in.")

def Dashboard():
    account = st.session_state.account # jsmith, bethier, etc
    role = st.session_state.role # Admin, Business, Customer

    st.sidebar.title("Local-E Market")
    st.sidebar.write("Dashboard")

    if role == "Customer":

        options = [
            "Home",
            "Browse Businesses",
            "Shopping Cart",
            "My Orders",
            "User Statistics"
        ]

    elif role == "Business Owner":

        options = [
            "Home",
            "Manage Products",
            "View Incoming Orders",
            "Business Statistics"
        ]

    elif role == "Admin":

        options = [
            "Home",
            "Manage Products",
            "View Incoming Orders",
            "Customer Management",
            "Business Management",
            "App Statistics"
        ]


    selection = st.sidebar.radio(
        "Navigation",
        options)


    if selection == "Home":

        st.subheader("Dashboard Overview")
        st.write(f"Welcome back, {account['Name']}!")

        col1, col2, col3 = st.columns(3)

        if role == "Customer":

            with col1:
                st.metric(
                    "Total Orders",
                    len(account.get("Orders", []))
                )

            with col2:
                st.metric(
                    "Cart Items",
                    len(account.get("Cart", []))
                )

            with col3:
                st.metric("Account Type", role)

        elif role == "Business Owner":

            with col1:
                st.metric(
                    "Products",
                    len(account.get("Products", []))
                )

            with col2:
                st.metric(
                    "Orders",
                    len(account.get("Orders", []))
                )

            with col3:
                st.metric("Account Type", role)

        elif role == "Admin":

            with col1:
                st.metric("Customers", len(RLU))

            with col2:
                st.metric("Businesses", len(RLBO))

            with col3:
                st.metric("Administrators", len(RLADMIN))
    if selection == "Browse Businesses":
        st.title("Local Businesses")
        for i in range(len(TEST)):
            left, middle, right = st.columns(3)
            st.divider()
            st.subheader(f"{TEST[i]["Business Name"]}")
            st.caption(f"{TEST[i]["Description"]}")
            st.badge("NEW", icon="✨", color="red")
            if st.button("Open", key=i):
                st.write(f"{TEST[i]["Products"]}")



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

        if not username or not password:

            st.error("Please enter a username and password.")

        elif LoginScr(username, password):

            st.session_state.screen = "dashboard"
            st.rerun()

        else:

            st.error("Incorrect username or password.")

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

    if st.button("Back"):
        st.session_state.screen = "welcome"
        st.rerun()

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

elif st.session_state.screen == "dashboard":

    if st.session_state.logged_in:
        Dashboard()

    else:
        st.session_state.screen = "welcome"
        st.rerun()
