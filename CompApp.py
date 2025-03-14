import streamlit as st

USER_CREDENTIALS = {"baranariban": "0v6260", "sertacaltinok": "0v6260", "zeynepegeuysal": "0v6260", "ahmetcangunaydin": "0v6260", "halilibrahimerol": "0v6260", "tubakahveci": "0v6260", "umutcangulletutan": "0v6260", "yigitcancavdarli": "0v6260"}

st.title("CompApp: Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password", key="password_input")
    
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.rerun()  # Updated function
        else:
            st.error("Invalid username or password")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    # Redirect to the Home page after login
    st.switch_page("pages/Home.py")
