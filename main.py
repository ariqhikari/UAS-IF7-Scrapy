import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt


@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def Dataset() :
    st.header("Pengenalan Dataset")
def Analisis_1() :
    st.header("Pertanyaan 1")
    st.subheader('Bagaimana perbandingan jumlah Penyewaan sepeda antara tahun 2011 dan 2012?')
    st.caption('10122238 - Titan El Haqi')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
def Analisis_2() :
    st.header("Pertanyaan 2")
    st.subheader('Apakah ada penurunan signifikan dalam penggunaan sepeda saat cuaca buruk?')
    st.caption('10122241 - Marsya Awliya Sabrina')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
def Analisis_3() :
    st.header("Pertanyaan 3")
    st.subheader('Apakah ada pengaruh hari libur terhadap jumlah sepeda yang disewa?')
    st.caption('10122254 - Ariq Hikari Hidayat')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
def Analisis_4() :
    st.header("Pertanyaan 4")
    st.subheader('Apa pengaruh faktor cuaca terhadap jumlah sewa sepeda harian?')
    st.caption('10122257 - M. Ghazy Al H. H.')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
def Analisis_5() :
    st.header("Ini Tab 5")
    day_df= pd.read_csv('dataset/adisya-day_df.csv')
    anomalies= pd.read_csv('dataset/adisya-anomalies.csv')
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    anomalies['dteday'] = pd.to_datetime(anomalies['dteday'])

    st.dataframe(day_df)
    st.dataframe(anomalies)
    

    st.title('Grafik Jumlah Penyewaan Sepeda')
    fig, ax = plt.subplots()
    ax.plot(day_df['dteday'], day_df['cnt'])
    ax.scatter(anomalies['dteday'], anomalies['cnt'], c='red')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah penyewaan sepeda')
    ax.tick_params(axis='x', rotation=90)
    ax.set_xticklabels([])  # Cara 1: Set label sumbu x menjadi daftar kosong

    st.pyplot(fig)

    st.header("Pertanyaan 5")
    st.subheader('Bagaimana cara mendeteksi peristiwa atau anomali dalam data penyewaan sepeda?')
    st.caption('10122260 - Adisya Ainun Fatihah')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
def Analisis_6() :
    st.header("Pertanyaan 6")
    st.subheader('Bagaimana distribusi waktu penyewaan sepeda?')
    st.caption('10122264 - Muhammad Naufal Ghifari')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    #Load Dataset
    daily_trend = pd.read_csv('dataset/naufal-daily_trend.csv')
    weekly_seasonal_trend = pd.read_csv('dataset/naufal-weekly_seasonal_trend.csv')

    #Pembuatan Tabel
    st.write('Tabel Penyewaan Sepeda Harian')
    st.dataframe(daily_trend.head())
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    #Membuat Judul
    st.subheader('Grafik Penyewaan Sepeda Harian')
    def main():
        # Baca dataset
        daily_trend = pd.read_csv('dataset/naufal-daily_trend.csv')

        # Visualisasi
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x='hr', y='cnt', data=daily_trend, ax=ax)
        plt.title('Distribusi Harian Penyewaan Sepeda')
        plt.xlabel('Jam')
        plt.ylabel('Rata-rata Jumlah Penyewa')
        st.pyplot(fig)

    if __name__ == "__main__":
        main()
    #Expander Grafik
    with st.expander("Penjelasan Grafik Penyewaan Sepeda Mingguan") :
        st.write('Terdapat peningkatan penyewaan pada jam-jam tertentu, khususnya selama periode sibuk pergi dan pulang kerja.') 

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    st.write('Tabel Penyewaan Sepeda Mingguan')
    st.dataframe(weekly_seasonal_trend.head())
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    #Membuat Judul
    st.subheader('Grafik Penyewaan Sepeda Mingguan')
    def draw_seasonal_plot(data):
        plt.figure(figsize=(14, 7))
        sns.lineplot(x='hr', y='cnt', hue='weekday', data=data, errorbar=None)
        plt.title('Distribusi Mingguan Penyewaan Sepeda (Berdasarkan Hari dalam Seminggu)')
        plt.xlabel('Jam')
        plt.ylabel('Rata-rata Jumlah Penyewa')
        plt.legend(title='Hari dalam Seminggu', loc='upper left', bbox_to_anchor=(1, 1))
        st.pyplot()

    #Memuat data
    weekly_seasonal_trend = pd.read_csv('dataset/naufal-weekly_seasonal_trend.csv')

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Tampilkan plot
    draw_seasonal_plot(weekly_seasonal_trend)
    #Expander Grafik
    with st.expander("Penjelasan Grafik Penyewaan Sepeda Mingguan") :
        st.write('Terdapat peningkatan penyewaan pada jam-jam tertentu, khususnya selama periode sibuk pergi dan pulang kerja.') 

with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Visualisasi Data Bike Sharing")
    dataset, analisis_1, analisis_2, analisis_3, analisis_4, analisis_5, analisis_6 = st.tabs(["Dataset", "#1 Titan El Haqi", "#2 Marsya Awliya Sabrina", "#3 Ariq Hikari Hidayat", "#4 M. Ghazy Al H. H.", "#5 Adisya Ainun Fatihah", "#6 Muhammad Naufal Ghifari"])

    with dataset :
        Dataset()
    with analisis_1 :
        Analisis_1()
    with analisis_2 :
        Analisis_2()
    with analisis_3 :
        Analisis_3()
    with analisis_4 :
        Analisis_4()
    with analisis_5 :
        Analisis_5()
    with analisis_6 :
        Analisis_6()