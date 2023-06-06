# ===== IMPORT LIBRARY =====
# for data wrangling
import pandas as pd
import numpy as np

# for web app
import streamlit as st

# etc
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
from io import BytesIO
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
from sklearn.cluster import KMeans
import pickle

# SET PAGE
st.set_page_config(page_title="PT Pharos Indonesia Web App", layout="wide")


@st.cache_resource
def load_model():
    filename = 'model_cluster.sav'
    model = pickle.load(open(filename, 'rb'))
    return model

model = load_model()

# SET HEADER
st.header('Analisis Data Penjualan Anda')
st.markdown('<hr>', unsafe_allow_html=True)

st.header('Upload File Excel')
st.markdown('<hr>', unsafe_allow_html=True)
# LOAD DUMMY DATA
data_dummy = pd.DataFrame({'TH_TranNum':['B1488AS000000125', 'B1488AS000000126'],
                           'TimeRecorded':['2022-02-17 11:00:00', '2022-02-18 11:00:00'],
                           'Procode':[123456, 987644],
                           'ProductName':['HANSAPLAST', 'ZWITSAL'],
                           'Procode SumQty':[5, 7],
                           'Procode SumValue':[25271, 28379],
                           'Procode SumVAT':[3940, 5761],
                           'VatPct':[5, 10]})

st.error("WARNING : PASTIKAN FILE EXCEL MEMILIKI FORMAT SEBAGAI BERIKUT!!! SEMAKIN BESAR DATA MAKA AKAN SEMAKIN LAMA DAN BERAT KOMPUTASINYA!!!")
# display dataframe
st.dataframe(data_dummy, use_container_width=True)

# list of expected column names and their corresponding data types
EXPECTED_COLUMNS = [
    ('TH_TranNum', object),
    ('TimeRecorded', object),
    ('Procode', float),
    ('ProductName', object),
    ('Procode SumQty', float),
    ('Procode SumValue', float),
    ('Procode SumVAT', float),
    ('VatPct', float)
]

try:
    # read the user uploaded Excel file
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])

    if uploaded_file is not None:
        # read the Excel file into a Pandas dataframe
        df = pd.read_excel(uploaded_file)

        # check if the dataframe has the expected columns and data types
        column_names = set(df.columns)
        expected_column_names = set([col[0] for col in EXPECTED_COLUMNS])
        if column_names != expected_column_names:
            raise ValueError(
                f"Column names do not match. Expected {expected_column_names}, but got {column_names}.")

        for col, dtype in EXPECTED_COLUMNS:
            if col in df.select_dtypes(include=[int, float]).columns:
                if not pd.api.types.is_integer_dtype(df[col]) and not pd.api.types.is_float_dtype(df[col]):
                    raise ValueError(
                        f"Column '{col}' has wrong data type. Expected {dtype}, but got {df[col].dtype}.")

        # if everything is OK, then preprocess
        df['TimeRecorded'] = pd.to_datetime(df['TimeRecorded'])
        # if everything is OK, display the dataframe
        st.dataframe(df, use_container_width=True)

        # analyze
        option = st.selectbox(
            'menu',
            ('Pilih Jenis Analisa', 'Association Rules', 'Clustering'), label_visibility="hidden")

        if option == 'Association Rules':
            # Group the products by transaction number and make a list of products for each transaction
            transactions = df.groupby(['TH_TranNum'])['ProductName'].apply(list).values.tolist()

            # Convert the list of products into a one-hot encoded matrix
            te = TransactionEncoder()
            te_ary = te.fit(transactions).transform(transactions)
            df_tr = pd.DataFrame(te_ary, columns=te.columns_)

            # Use FP-Growth to generate association rules
            frequent_itemsets = fpgrowth(df_tr, min_support=0.1, use_colnames=True)
            rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0)
            if len(frequent_itemsets) > 0:
                st.write(frequent_itemsets, use_container_width=True)
            if len(rules) > 0:
                st.write(rules, use_container_width=True)
        elif option == 'Clustering':
            X = df[['Procode SumQty', 'Procode SumValue', 'Procode SumVAT', 'VatPct']]
            ypred = model.predict(X)
            df_cluster = df.copy()
            df_cluster['Cluster'] = ypred
            df_cluster['Cluster'] = df_cluster['Cluster'].replace(0, 'Sangat Tidak Laku')
            df_cluster['Cluster'] = df_cluster['Cluster'].replace(1, 'Laku')
            df_cluster['Cluster'] = df_cluster['Cluster'].replace(2, 'Tidak Laku')
            df_cluster['Cluster'] = df_cluster['Cluster'].replace(3, 'Sangat Laku')
            st.dataframe(df_cluster, use_container_width=True)
            # output
            # create a BytesIO object to hold the Excel data
            excel_data = BytesIO()

            # write the DataFrame to the BytesIO object as an Excel file
            df_cluster.to_excel(excel_data, index=False)

            # create a download button for the Excel file
            button = st.download_button(
                label="Download file",
                data=excel_data.getvalue(),
                file_name="Hasil_Analisis_Cluster.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

    # throw exception error
except ValueError as e:
    st.warning(str(e))
except Exception as e:
    st.error(str(e))