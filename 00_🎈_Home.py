# ===== IMPORT LIBRARY =====
# for data wrangling
import pandas as pd
import numpy as np

# for web app
import streamlit as st

# ===== SET PAGE =====
st.set_page_config(page_title="PT Pharos Indonesia Web App", layout="centered")

# ===== DEVELOP FRONT-END =====
# SET HEADER PAGE
st.markdown('<div style="text-align: justify; font-size:300%; line-height: 150%; margin-top: -55px;"> <b><br>Web App Analisis Data Penjualan PT Pharos Indonesia </b> </div>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

# SET DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> PT Pharos Indonesia adalah perusahaan yang berfokus pada industri penjualan khususnya pada sekotr kesehatan dan farmasi. Sebagai salah satu pemain utama di sektor ini, Pharos Indonesia terlibat dalam berbagai kegiatan seperti distribusi, pemasaran, dan penjualan produk-produk kesehatan dan farmasi. Perusahaan ini memiliki jaringan distribusi yang luas di seluruh Indonesia dan berkomitmen untuk memberikan produk berkualitas tinggi kepada pelanggan mereka.</div>',
            unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Web App Analisis Data Penjualan PT Pharos Indonesia merupakan aplikasi berbasis web yang dirancang khusus untuk memproses dan menganalisis data penjualan perusahaan secara terintegrasi. Aplikasi ini menyediakan antarmuka yang intuitif dan mudah digunakan, memungkinkan pengguna untuk mengakses informasi yang relevan dengan cepat dan efisien.</div>',
            unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Web App Analisis Data Penjualan PT Pharos Indonesia memiliki tiga fungsi utama yang memberikan nilai tambah bagi perusahaan. Pertama, dengan menggunakan algoritma Apriori, aplikasi ini dapat menganalisis pola penjualan dan mengidentifikasi asosiasi antara produk, memungkinkan PT Pharos Indonesia untuk mengoptimalkan strategi penjualan berdasarkan hubungan yang erat antara produk tertentu. Kedua, dengan algoritma K-means, web app ini dapat melakukan segmentasi pelanggan berdasarkan perilaku pembelian, memungkinkan perusahaan untuk mengembangkan strategi pemasaran yang lebih cermat dan menyesuaikan pendekatan mereka untuk mencapai segmen pelanggan yang berbeda. Terakhir, melalui visualisasi data yang interaktif, aplikasi ini membantu pengguna memahami data penjualan dengan lebih baik, melalui grafik, diagram, dan visualisasi lainnya, yang memungkinkan perusahaan untuk membuat perbandingan, mengidentifikasi tren, dan mengambil keputusan yang didukung oleh informasi yang jelas dan mudah dipahami.</div>',
            unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Dengan memanfaatkan algoritma Apriori dan K-means, Web App Analisis Data Penjualan PT Pharos Indonesia bertujuan untuk meningkatkan pemahaman perusahaan tentang perilaku pelanggan, mengoptimalkan strategi penjualan, dan mengambil keputusan yang lebih cerdas berdasarkan analisis data yang mendalam. </div>',
            unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)