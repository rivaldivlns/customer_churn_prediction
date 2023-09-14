import streamlit as st
import pandas as pd
import pickle
import ast
import numpy as np
import sklearn

def run():
    
    with open('model.pkl', 'rb') as file_1:
        model = pickle.load(file_1)  

    products_number = st.selectbox(label='Select your product number:', options=[1, 2, 3, 4])
    age = st.number_input(label='Select your age',min_value=18,max_value=91)
    active_member = st.selectbox(label="Select your status member", options=[0,1])
    balance = st.number_input(label='Select your balance',min_value=0.00,max_value=296710.00)
    gender = st.radio(label="Select your gender", options=["Male", "Female"])
    country = st.radio(label="Select your country", options=["Spain", "Germany", "France"])
    credit_score = st.number_input(label='Select your credit score',min_value=350,max_value=850)
    tenure = st.number_input(label='Select your tenure',min_value=0,max_value=10)

    data_inf = pd.DataFrame({
        'products_number' : products_number,
        'age' : age,
        'active_member' : active_member,
        'balance' : balance,
        'gender' : gender,
        'country': country,
        'credit_score': credit_score ,
        'tenure' : tenure
        }, index =[0])

    st.table(data_inf)
    
    if st.button(label='Predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = model.predict(data_inf)

        st.write(y_pred_inf[0])

        if y_pred_inf[0] == 0:
            st.write('Customer diprediksi akan loyal')
        else:
            st.write('Customer diprediksi akan churn')






