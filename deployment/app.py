import streamlit as st
import prediction, eda

# Set page title and icon
st.set_page_config(page_title="Rivaldi Valensia Application", page_icon="📊")

# Create sidebar navigation
st.sidebar.title("Menu")
selected_page = st.sidebar.radio("Select Page", ("Homepage", "Exploratory Data Analysis", "Prediction"))

# Halaman Beranda
if selected_page == "Homepage":
    st.title("Welcome to Application of Exploration Data Analysis and Model Machine Learning")
    st.write("Made by Rivaldi Valensia")
    st.write("Please select page on a sidebar")

# Halaman EDA
elif selected_page == "Exploratory Data Analysis":
    eda.run()

# Halaman Model
elif selected_page == "Prediction":
    prediction.run()

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("If you have any questions, please hit me up on:")
st.sidebar.markdown("[GitHub](https://github.com/rivaldivlns)")