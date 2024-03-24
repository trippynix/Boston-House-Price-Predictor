# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 00:31:23 2023

@author: deadl
"""

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


# Load the machine learning model
model = joblib.load('C:/Users/deadl/Downloads/Python/Boston House price/trained_model.sav')

# Load the Boston Housing dataset
boston = pd.read_csv('C:/Users/deadl/Downloads/Python/Boston House price/housing.csv', header = None, delimiter = r"\s+")
boston.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Add a sidebar for navigation
option = st.sidebar.selectbox(
    'Select an option:',
     ('Prediction', 'Dashboard'))

if option == 'Prediction':
    # Define the app layout
    st.title("Boston House Price Predictor")
    st.write("Enter the values for the following features to predict the house price:")

    # Define the input fields
    CRIM = st.number_input("CRIM")
    ZN = st.number_input("ZN")
    INDUS = st.number_input("INDUS")
    CHAS = st.selectbox("CHAS", [0, 1])
    NOX = st.number_input("NOX")
    RM = st.number_input("RM")
    AGE = st.number_input("AGE")
    DIS = st.number_input("DIS")
    RAD = st.number_input("RAD")
    TAX = st.number_input("TAX")
    PTRATIO = st.number_input("PTRATIO")
    B = st.number_input("B")
    LSTAT = st.number_input("LSTAT")
    
    # Define a submit button
    submit_button = st.button("Predict Price")
    
    # Define the prediction function
    def predict_price(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT):
        input_data = pd.DataFrame({
            "CRIM": [CRIM],
            "ZN": [ZN],
            "INDUS": [INDUS],
            "CHAS": [CHAS],
            "NOX": [NOX],
            "RM": [RM],
            "AGE": [AGE],
            "DIS": [DIS],
            "RAD": [RAD],
            "TAX": [TAX],
            "PTRATIO": [PTRATIO],
            "B": [B],
            "LSTAT": [LSTAT]
        })
        prediction = model.predict(input_data)
        return prediction[0]
    
    # Call the prediction function when the submit button is clicked
    if submit_button:
        prediction = predict_price(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT)
        st.write("The predicted house price is: ", prediction)

elif option == 'Dashboard':
    st.title('Dashboard')
    st.write('This is the dashboard section.')
    
    var_list = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

    # Create a dropdown list for selecting a variable
    variable = st.selectbox('Select a variable:', var_list)
   
   # Display a visualization based on the selected variable
    if variable == 'CRIM':
        st.write('## Relationship between CRIM and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='CRIM', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'ZN':
        st.write('## Relationship between ZN and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='ZN', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'INDUS':
        st.write('## Relationship between INDUS and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='INDUS', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'CHAS':
        st.write('## Relationship between CHAS and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='CHAS', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'NOX':
        st.write('## Relationship between NOX and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='NOX', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'RM':
        st.write('## Relationship between RM and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='RM', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'AGE':
        st.write('## Relationship between AGE and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='AGE', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'DIS':
        st.write('## Relationship between DIS and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='DIS', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'RAD':
        st.write('## Relationship between RAD and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='RAD', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'TAX':
        st.write('## Relationship between TAX and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='TAX', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'PTRATIO':
        st.write('## Relationship between PTRATIO and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='PTRATIO', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'B':
        st.write('## Relationship between B and MEDV')
        fig, ax = plt.subplots()
        sns.scatterplot(data=boston, x='B', y='MEDV', ax=ax)
        st.pyplot(fig)
    elif variable == 'LSTAT':
       st.write('## Relationship between LSTAT and MEDV')
       fig, ax = plt.subplots()
       sns.scatterplot(data=boston, x='LSTAT', y='MEDV', ax=ax)
       st.pyplot(fig)
    # Show a message if no variable is selected
    if variable not in var_list:
       st.warning('Please select a variable from the dropdown list.')    
       
       
       