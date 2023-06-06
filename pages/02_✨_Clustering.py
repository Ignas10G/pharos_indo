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

# SET PAGE
st.set_page_config(page_title="PT Pharos Indonesia Web App", layout="wide")

# SET HEADER
st.header('Analisis Cluster dengan K-Means')
st.markdown('<hr>', unsafe_allow_html=True)

@st.cache_resource
def load_data():
    data_cluster = pd.read_excel('data/data_pharos_cluster.xlsx')
    data_cluster['month'] = data_cluster['month'].replace(2, 'Februari')
    data_cluster['month'] = data_cluster['month'].replace(3, 'Maret')
    data_cluster['month'] = data_cluster['month'].replace(4, 'April')
    return data_cluster

data_cluster = load_data()
filtered_df = dataframe_explorer(data_cluster, case=False)
st.dataframe(filtered_df, use_container_width=True)

excel_data = BytesIO()

# write the DataFrame to the BytesIO object as an Excel file
filtered_df.to_excel(excel_data, index=False)

# create a download button for the Excel file
button = st.download_button(
    label="Download file",
    data=excel_data.getvalue(),
    file_name="Hasil_Cluster.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    use_container_width=True
)

st.markdown('<hr>', unsafe_allow_html=True)

# PIE CHART PROPORSI CLUSTER
prop_cluster = filtered_df.groupby('Cluster')['Cluster'].count()
prop_cluster = pd.DataFrame(prop_cluster).rename(columns={'Cluster':'Jumlah'})
fig_pie_cluster = px.pie(prop_cluster,
                         values="Jumlah",
                         names=prop_cluster.index,
                         title="<b>Proporsi Jumlah Cluster</b>")
st.plotly_chart(fig_pie_cluster, use_container_width=True)

st.markdown('<hr>', unsafe_allow_html=True)

# ======================================== BULAN ====================================

# BAR CHART PERBANDINGAN RATA-RATA SUMQTY BERDASARKAN BULAN
avg_sumqty_bulan = filtered_df.groupby('month')['Procode SumQty'].mean()
avg_sumqty_bulan = pd.DataFrame(avg_sumqty_bulan).sort_values(by='Procode SumQty',
                                                                        ascending=False)

fig_avg_sumqty_bulan = px.bar(avg_sumqty_bulan,
                             x=avg_sumqty_bulan.index,
                             y="Procode SumQty",
                             title="<b>Rata-rata Total Kuantitas Produk per Bulan</b>",
                             labels={"month":'Bulan',
                                     "Procode SumQty":"Rata-rata Total Kuantitas Produk"},
                             color_discrete_sequence=["#0083B8"] * len(avg_sumqty_bulan),
                             template="plotly_white",
)
fig_avg_sumqty_bulan.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# BAR CHART PERBANDINGAN RATA-RATA SUMVAL BERDASARKAN BULAN
avg_sumval_bulan = filtered_df.groupby('month')['Procode SumValue'].mean()
avg_sumval_bulan = pd.DataFrame(avg_sumval_bulan).sort_values(by='Procode SumValue',
                                                                        ascending=False)

fig_avg_sumval_bulan = px.bar(avg_sumval_bulan,
                             x=avg_sumval_bulan.index,
                             y="Procode SumValue",
                             title="<b>Rata-rata Total Produk Terjual per Bulan</b>",
                             labels={"month":'Bulan',
                                     "Procode SumValue":"Rata-rata Total Produk Terjual"},
                             color_discrete_sequence=["#0083B8"] * len(avg_sumval_bulan),
                             template="plotly_white",
)
fig_avg_sumval_bulan.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# BAR CHART PERBANDINGAN RATA-RATA SUMVAT BERDASARKAN BULAN
avg_sumvat_bulan = filtered_df.groupby('month')['Procode SumVAT'].mean()
avg_sumvat_bulan = pd.DataFrame(avg_sumvat_bulan).sort_values(by='Procode SumVAT',
                                                                        ascending=False)

fig_avg_sumvat_bulan = px.bar(avg_sumvat_bulan,
                             x=avg_sumvat_bulan.index,
                             y="Procode SumVAT",
                             title="<b>Rata-rata Total PPN Produk per Bulan</b>",
                             labels={"month":'Bulan',
                                     "Procode SumVAT":"Rata-rata Total PPN Produk"},
                             color_discrete_sequence=["#0083B8"] * len(avg_sumvat_bulan),
                             template="plotly_white",
)
fig_avg_sumvat_bulan.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# BAR CHART PERBANDINGAN RATA-RATA SUMVAL BERDASARKAN BULAN
avg_vatpct_bulan = filtered_df.groupby('month')['VatPct'].mean()
avg_vatpct_bulan = pd.DataFrame(avg_vatpct_bulan).sort_values(by='VatPct',
                                                                        ascending=False)

fig_avg_vatpct_bulan = px.bar(avg_vatpct_bulan,
                             x=avg_vatpct_bulan.index,
                             y="VatPct",
                             title="<b>Rata-rata Persentase PPN per Bulan</b>",
                             labels={"month":'Bulan',
                                     "VatPct":"Persentase PPN"},
                             color_discrete_sequence=["#0083B8"] * len(avg_vatpct_bulan),
                             template="plotly_white",
)
fig_avg_vatpct_bulan.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# ======================================== CLUSTER ====================================

# BAR CHART PERBANDINGAN RATA-RATA SUMQTY BERDASARKAN CLUSTER
avg_sumqty_cluster = filtered_df.groupby('Cluster')['Procode SumQty'].mean()
avg_sumqty_cluster = pd.DataFrame(avg_sumqty_cluster).sort_values(by='Procode SumQty',
                                                                        ascending=False)

fig_avg_sumqty_cluster = px.bar(avg_sumqty_cluster,
                             x=avg_sumqty_cluster.index,
                             y="Procode SumQty",
                             title="<b>Rata-rata Total Kuantitas Produk per Cluster</b>",
                             labels={"Cluster":'Cluster',
                                     "Procode SumQty":"Rata-rata Total Kuantitas Produk"},
                             color_discrete_sequence=["#0083B8"] * len(avg_sumqty_cluster),
                             template="plotly_white",
)
fig_avg_sumqty_cluster.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# BAR CHART PERBANDINGAN RATA-RATA SUMVAL BERDASARKAN CLUSTER
avg_sumval_cluster = filtered_df.groupby('Cluster')['Procode SumValue'].mean()
avg_sumval_cluster = pd.DataFrame(avg_sumval_cluster).sort_values(by='Procode SumValue',
                                                                        ascending=False)

fig_avg_sumval_cluster = px.bar(avg_sumval_cluster,
                             x=avg_sumval_cluster.index,
                             y="Procode SumValue",
                             title="<b>Rata-rata Total Produk Terjual per Cluster</b>",
                             labels={"Cluster":'Cluster',
                                     "Procode SumValue":"Rata-rata Total Produk Terjual"},
                             color_discrete_sequence=["#0083B8"] * len(avg_sumval_cluster),
                             template="plotly_white",
)
fig_avg_sumval_cluster.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# BAR CHART PERBANDINGAN RATA-RATA SUMVAT BERDASARKAN CLUSTER
avg_sumvat_cluster = filtered_df.groupby('Cluster')['Procode SumVAT'].mean()
avg_sumvat_cluster = pd.DataFrame(avg_sumvat_cluster).sort_values(by='Procode SumVAT',
                                                                        ascending=False)

fig_avg_sumvat_cluster = px.bar(avg_sumvat_cluster,
                             x=avg_sumvat_cluster.index,
                             y="Procode SumVAT",
                             title="<b>Rata-rata Total PPN Produk per Cluster</b>",
                             labels={"Cluster":'Cluster',
                                     "Procode SumVAT":"Rata-rata Total PPN Produk"},
                             color_discrete_sequence=["#0083B8"] * len(avg_sumvat_cluster),
                             template="plotly_white",
)
fig_avg_sumvat_cluster.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# BAR CHART PERBANDINGAN RATA-RATA SUMVAL BERDASARKAN CLUSTER
avg_vatpct_cluster = filtered_df.groupby('Cluster')['VatPct'].mean()
avg_vatpct_cluster = pd.DataFrame(avg_vatpct_cluster).sort_values(by='VatPct',
                                                                        ascending=False)

fig_avg_vatpct_cluster = px.bar(avg_vatpct_cluster,
                             x=avg_vatpct_cluster.index,
                             y="VatPct",
                             title="<b>Rata-rata Persentase PPN per Cluster</b>",
                             labels={"Cluster":'Cluster',
                                     "VatPct":"Persentase PPN"},
                             color_discrete_sequence=["#0083B8"] * len(avg_vatpct_cluster),
                             template="plotly_white",
)
fig_avg_vatpct_cluster.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# DASHBOARD
left_column_chart_row1, right_column_chart_row1 = st.columns(2)
left_column_chart_row1.plotly_chart(fig_avg_sumqty_bulan, use_container_width=True)
right_column_chart_row1.plotly_chart(fig_avg_sumval_bulan, use_container_width=True)

left_column_chart_row2, right_column_chart_row2 = st.columns(2)
left_column_chart_row2.plotly_chart(fig_avg_sumvat_bulan, use_container_width=True)
right_column_chart_row2.plotly_chart(fig_avg_vatpct_bulan, use_container_width=True)

st.markdown('<hr>', unsafe_allow_html=True)

left_column_chart_row3, right_column_chart_row3 = st.columns(2)
left_column_chart_row3.plotly_chart(fig_avg_sumqty_cluster, use_container_width=True)
right_column_chart_row3.plotly_chart(fig_avg_sumval_cluster, use_container_width=True)

left_column_chart_row4, right_column_chart_row4 = st.columns(2)
left_column_chart_row4.plotly_chart(fig_avg_sumvat_cluster, use_container_width=True)
right_column_chart_row4.plotly_chart(fig_avg_vatpct_cluster, use_container_width=True)