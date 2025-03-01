import streamlit as st
from langchain_helper import generate_restaurant_name_and_items  # ✅ Import the function

# Streamlit App Title
st.title("Restaurant Name & Menu Generator")

# Sidebar dropdown for cuisine selection
cuisine = st.sidebar.selectbox("Pick a cuisine", ["Indian", "Chinese", "Italian", "Mexican", "Arabic"])

# When a cuisine is selected, generate restaurant name & menu
if cuisine:
    response = generate_restaurant_name_and_items(cuisine)  # ✅ Correct function call

    # Display Restaurant Name
    st.header(response['restaurant_name'].strip())

    # Display Menu Items as a list
    menu_items = response['menu_items'].strip().split(',')
    st.write("**Menu items:**")
    for item in menu_items:
        st.write("-", item.strip())  # Ensure clean formatting
