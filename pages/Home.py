import streamlit as st

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in.")
    st.stop() 

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Composite Selector"])

st.title(f"Welcome, {st.session_state['username']}!")

if selection == "Composite Selector":
    st.switch_page("pages/Composite Selector.py")
