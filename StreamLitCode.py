import streamlit as st

UD = { #Dictonary of customers
    "JSmith": {
        "Password": {
            "1234": "John Smith"
        }
    }
}
BD = { #Dictonary of Business Owners
    "TWells": {
        "Password": {
            "5678": {
                "Tom Wells": "Tom's Diner"
            }
        }
    }
}
BDN = { #Business Owner names
    "TWells": "Tom Wells"
}
AD = { #Dictonary of Admins
    "PHammel": {"Password": {"1010": "Payton Hammel"}},
      "BEthier": {"Password": {"1100": "Brian Ethier"}}
} #Dictonary of Admins
#print(BD["TWells"]["Password"]["5678"]["Tom Wells"])
DL = []
CU = "" #Current User's name
BN = "" #Current Business's name

def LoginScr(username, password):
    global CU, BN

    if username in UD:
        if password in UD[username]["Password"]:
            CU = UD[username]["Password"][password]

            st.success("Login Successful")
            st.write(f"Welcome, {CU}!")
            return

    if username in BD:
        if password in BD[username]["Password"]:
            business_info = BD[username]["Password"][password]

            for name, business in business_info.items():
                CU = name
                BN = business

            st.success("Login Successful")
            st.write(f"Welcome, {CU}!")
            st.write(f"Business: {BN}")
            return

    if username in AD:
        if password in AD[username]["Password"]:
            CU = AD[username]["Password"][password]

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

    UD[username] = {
        "Password": {
            password: full_name
        }
    }

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

    BD[username] = {
        "Password": {
            password: {
                full_name: business_name
            }
        }
    }

    BDN[username] = full_name

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
        font-size: 32px;
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

login_tab, signup_tab, = st.tabs(["Login", "SignUp"])

with login_tab:

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

with signup_tab:

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

    # Only show this field for Business Owners
    if account_type == "Business Owner":
        business_name = st.text_input(
            "Business Name",
            key="business_name"
        )

    if st.button("Sign Up", key="signup_button"):

        if new_password != confirm_password:
            st.error("Passwords do not match.")

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

