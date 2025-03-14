import streamlit as st

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Unauthorized access. Please log in.")
    st.stop()

st.title("CompApp: Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")
st.title("Composite Selector")
st.write("Click on the properties you want in your composite/polymer. Then fill in the blank spaces with the maximum or the minimum limits of the parameters you desire. The application will provide you a list of composites which are suitable for your project's requirements. You will also have a chance to compare these composites with total grades out of 100.")
