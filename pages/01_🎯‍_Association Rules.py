# ===== IMPORT LIBRARY =====
# for data wrangling
import pandas as pd
import numpy as np

# for web app
import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly.express as px

# etc
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
from io import BytesIO
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

# SET PAGE
st.set_page_config(page_title="PT Pharos Indonesia Web App", layout="wide")

# SET HEADER
st.header('Asosiasi Rules dengan Apriori')
st.markdown('<hr>', unsafe_allow_html=True)

# LOAD DATA
option = st.selectbox(
        'menu',
        ('Pilih Bulan', 'Februari', 'Maret', 'April'), label_visibility="hidden")

data_apriori = pd.read_excel('data/data_pharos_indo.xlsx')
data_apriori = data_apriori[['month', 'TH_TranNum', 'ProductName']]

if option == 'Februari':
    data_month = data_apriori[data_apriori['month'] == 2]
    data_month['month'] = data_month['month'].replace(2, 'Februari')
    st.dataframe(data_month, use_container_width=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    # Group the products by transaction number and make a list of products for each transaction
    transactions = data_month.groupby(['TH_TranNum'])['ProductName'].apply(list).values.tolist()

    # Convert the list of products into a one-hot encoded matrix
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_tr = pd.DataFrame(te_ary, columns=te.columns_)

    # Use FP-Growth to generate association rules
    frequent_itemsets = apriori(df_tr, min_support=0.1, use_colnames=True)
    if len(frequent_itemsets) > 0:
        st.write(frequent_itemsets, use_container_width=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0)
        if len(rules) > 0:
                st.write(rules, use_container_width=True)

elif option == 'Maret':
    data_month = data_apriori[data_apriori['month'] == 3]
    data_month['month'] = data_month['month'].replace(3, 'Maret')
    st.dataframe(data_month, use_container_width=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    # Group the products by transaction number and make a list of products for each transaction
    transactions = data_month.groupby(['TH_TranNum'])['ProductName'].apply(list).values.tolist()

    # Convert the list of products into a one-hot encoded matrix
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_tr = pd.DataFrame(te_ary, columns=te.columns_)

    # Use FP-Growth to generate association rules
    frequent_itemsets = apriori(df_tr, min_support=0.1, use_colnames=True)
    if len(frequent_itemsets) > 0:
        st.write(frequent_itemsets, use_container_width=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0)
        if len(rules) > 0:
                st.write(rules, use_container_width=True)

elif option == 'April':
    data_month = data_apriori[data_apriori['month'] == 4]
    data_month['month'] = data_month['month'].replace(4, 'April')
    st.dataframe(data_month, use_container_width=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    # Group the products by transaction number and make a list of products for each transaction
    transactions = data_month.groupby(['TH_TranNum'])['ProductName'].apply(list).values.tolist()

    # Convert the list of products into a one-hot encoded matrix
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_tr = pd.DataFrame(te_ary, columns=te.columns_)

    # Use FP-Growth to generate association rules
    frequent_itemsets = apriori(df_tr, min_support=0.1, use_colnames=True)
    if len(frequent_itemsets) > 0:
        st.write(frequent_itemsets, use_container_width=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0)
        if len(rules) > 0:
                st.write(rules, use_container_width=True)
