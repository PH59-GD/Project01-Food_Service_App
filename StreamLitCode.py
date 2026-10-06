import streamlit as st

UD = {"JSmith": {"Password": {"1234": "John Smith"}}, } #Dictonary of customers
BD = {"TWells": {"Password": {"5678": {"Tom Wells": "Tom's Diner"}}}, } #Dictonary of Business Owners
BDN = {"TWells": "Tom Wells"} #Business Owner names
AD = {"PHammel": {"Password": {"1010": "Payton Hammel"}}, "BEthier": {"Password": {"1100": "Brian Ethier"}} } #Dictonary of Admins
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
        font-size: 32px;
        text-align: center;
        color: black;
    }

    .stTextInput label {
        font-family: Georgia;
        font-size: 18px;
    }

    .stButton button {
        font-family: Georgia;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="login-title">Login</div>',
    unsafe_allow_html=True
)

username = st.text_input("Username")

password = st.text_input("Password",
                         type = "password")

if st.button("Login"):
    LoginScr(username, password)
