import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['date','Category','Amount','Description'])

def add_expense(date,category,amount,description):
    new_expense = pd.DataFrame([[date,category,amount,description]], columns=st.session_state.expenses.columns)
    st.session_state.expenses = pd.concat([st.session_state.expenses,new_expense], ignore_index=True)




st.title("Expenses Trecker")
with st.sidebar:
    st.header('Add Expense')
    date = st.date_input("Date")
    category = st.selectbox('Category',['food', 'transport','Entertainment','Utilities','other'])
    amount = st.number_input('Amount',min_value=0.0, format="%.2f")
    description = st.text_input('Descripition')
    if st.button('Add'):
        add_expense(date,category,amount,description)
        st.success("Expense Added ! ")
    st.header


