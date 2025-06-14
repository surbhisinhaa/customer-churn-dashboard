# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.columns = df.columns.str.replace(' ', '')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

st.title('Customer Churn Analysis Dashboard')

# Show dataset 
if st.checkbox('Show Raw Data'):
    st.write(df)

# Key Metrics
total_customers = df.shape[0]
churn_count = df[df['Churn'] == 'Yes'].shape[0]
churn_rate = (churn_count / total_customers) * 100

st.subheader('Key Metrics')
st.write(f'Total Customers: {total_customers}')
st.write(f'Total Churned: {churn_count}')
st.write(f'Churn Rate: {churn_rate:.2f}%')

# Filters
st.sidebar.header('Filter Customers')

# Contract Filter
contract_type = st.sidebar.multiselect('Select Contract Type', options=df['Contract'].unique(), default=df['Contract'].unique())

# Gender Filter
gender = st.sidebar.multiselect('Select Gender', options=df['gender'].unique(), default=df['gender'].unique())

# Payment Method Filter
payment_method = st.sidebar.multiselect('Select Payment Method', options=df['PaymentMethod'].unique(), default=df['PaymentMethod'].unique())

# Apply Filters
filtered_df = df[(df['Contract'].isin(contract_type)) & 
                 (df['gender'].isin(gender)) & 
                 (df['PaymentMethod'].isin(payment_method))]

st.subheader('Filtered Dataset')
st.write(filtered_df)

# Churn Distribution for Filtered Data
st.subheader('Churn Distribution')
fig, ax = plt.subplots()
sns.countplot(x='Churn', data=filtered_df, ax=ax)
st.pyplot(fig)

# Monthly Charges Distribution
st.subheader('Monthly Charges Distribution by Churn')
fig2, ax2 = plt.subplots()
sns.histplot(data=filtered_df, x='MonthlyCharges', hue='Churn', kde=True, ax=ax2)
st.pyplot(fig2)

