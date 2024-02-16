import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def distribusi_waktu(daily_trend, weekly_seasonal_trend):
    #Memperbaiki tipe data 
    daily_trend['dteday'] = pd.to_datetime(daily_trend['dteday'])
    weekly_seasonal_trend['dteday'] = pd.to_datetime(weekly_seasonal_trend['dteday'])

    #Grafik Penyewaan Harian
    daily_trend = pd.DataFrame({
        'Jam' : [0, 5, 10, 15, 20],
        'Jumlah Rata-Rata Penyewa' : [0, 100, 200, 300, 400]
    })

    #Perkembangan Pengiriman
    st.subheader("Grafik Penyewaan Sepeda Harian")
    st.dataframe(daily_trend)

    # Buat bar chart
    label = daily_trend['Jam']
    data = daily_trend['Jumlah Rata-Rata Penyewa']

    fig, ax = plt.subplots()
    ax.bar(label, data)
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Rata-Rata Penyewa')

    #Menambahkan Label Pada Setiap Bar
    for i in range (len(label)) :
        ax.text(label[i], data[i], str(data[i]), ha='center', va='bottom' )

    #Rotasi Label 45 derajat
    plt.xticks(rotation=45)                    
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Grafik Penyewaan Sepeda Harian") :
        st.write('Terdapat peningkatan penyewaan pada jam-jam tertentu, khususnya selama periode sibuk pergi dan pulang kerja.') 
        
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    #Grafik Penyewaan Musiman
    weekly_seasonal_trend = pd.DataFrame({
        'Jam' : [0, 5, 10, 15, 20],
        'Jumlah Rata-Rata Penyewa' : [0, 100, 200, 300, 400]
    })

    #Perkembangan Pengiriman
    st.subheader("Grafik Penyewaan Sepeda Musiman")
    st.dataframe(weekly_seasonal_trend)

    # Buat bar chart
    label = weekly_seasonal_trend['Jam']
    data = weekly_seasonal_trend['Jumlah Rata-Rata Penyewa']

    fig, ax = plt.subplots()
    ax.bar(label, data)
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Rata-Rata Penyewa')

    #Menambahkan Label Pada Setiap Bar
    for i in range (len(label)) :
        ax.text(label[i], data[i], str(data[i]), ha='center', va='bottom' )

    #Rotasi Label 45 derajat
    plt.xticks(rotation=45)                    
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Grafik Penyewaan Sepeda Musiman") :
        st.write('Terdapat peningkatan penyewaan pada jam-jam tertentu, khususnya selama periode sibuk pergi dan pulang kerja.')
    

def Dataset() :
    st.header("Pengenalan Dataset")
def Analisis_1() :
    st.header("Ini Tab 1")
    def main():
        st.title('Distribusi Harian Peminjaman Sepeda')
        # Baca dataset
        daily_trend = pd.read_csv('dataset/naufal-daily_trend.csv')

        st.write('Data yang dibaca dari file:')
        st.write(daily_trend.head())

        # Visualisasi
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x='hr', y='cnt', data=daily_trend, ax=ax, marker='o')
        plt.title('Distribusi Harian Peminjaman Sepeda')
        plt.xlabel('Jam')
        plt.ylabel('Rata-rata Jumlah Peminjam')
        st.pyplot(fig)

    if __name__ == "__main__":
        main()
def Analisis_2() :
    st.header("Ini Tab 2")
def Analisis_3() :
    st.header("Ini Tab 3")
def Analisis_4() :
    st.header("Ini Tab 4")
def Analisis_5() :
    st.header("Ini Tab 5")
    def draw_seasonal_plot(data):
        plt.figure(figsize=(14, 7))
        sns.lineplot(x='hr', y='cnt', hue='weekday', data=data, errorbar=None)
        plt.title('Distribusi Musiman Penyewaan Sepeda (Berdasarkan Hari dalam Seminggu)')
        plt.xlabel('Jam')
        plt.ylabel('Rata-rata Jumlah Penyewaan')
        plt.legend(title='Hari dalam Seminggu', loc='upper left', bbox_to_anchor=(1, 1))
        st.pyplot()

    # Memuat data
    # Misalkan weekly_seasonal_trend adalah DataFrame yang berisi data musiman
    weekly_seasonal_trend = pd.read_csv('dataset/naufal-weekly_seasonal_trend.csv')  # Ganti dengan lokasi file CSV Anda

    # Tampilkan judul aplikasi
    st.title('Visualisasi Musiman Penyewaan Sepeda')

    # Tampilkan plot
    draw_seasonal_plot(weekly_seasonal_trend)
def Analisis_6() :
    st.header("Pertanyaan 6")
    st.subheader('Bagaimana Distribusi Waktu Peminjaman Sepeda?')
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
        sns.lineplot(x='hr', y='cnt', data=daily_trend, ax=ax, marker='o')
        plt.title('Distribusi Harian Peminjaman Sepeda')
        plt.xlabel('Jam')
        plt.ylabel('Rata-rata Jumlah Peminjam')
        st.pyplot(fig)

    if __name__ == "__main__":
        main()
    #Expander Grafik
    with st.expander("Penjelasan Grafik Penyewaan Sepeda Musiman") :
        st.write('Terdapat peningkatan penyewaan pada jam-jam tertentu, khususnya selama periode sibuk pergi dan pulang kerja.') 

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    st.write('Tabel Penyewaan Sepeda Musiman')
    st.dataframe(weekly_seasonal_trend.head())
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    #Membuat Judul
    st.subheader('Grafik Penyewaan Sepeda Musiman')
    def draw_seasonal_plot(data):
        plt.figure(figsize=(14, 7))
        sns.lineplot(x='hr', y='cnt', hue='weekday', data=data, errorbar=None)
        plt.title('Distribusi Musiman Penyewaan Sepeda (Berdasarkan Hari dalam Seminggu)')
        plt.xlabel('Jam')
        plt.ylabel('Rata-rata Jumlah Penyewaan')
        plt.legend(title='Hari dalam Seminggu', loc='upper left', bbox_to_anchor=(1, 1))
        st.pyplot()

    # Memuat data
    # Misalkan weekly_seasonal_trend adalah DataFrame yang berisi data musiman
    weekly_seasonal_trend = pd.read_csv('dataset/naufal-weekly_seasonal_trend.csv')  # Ganti dengan lokasi file CSV Anda

    # Tampilkan plot
    draw_seasonal_plot(weekly_seasonal_trend)
    #Expander Grafik
    with st.expander("Penjelasan Grafik Penyewaan Sepeda Musiman") :
        st.write('Terdapat peningkatan penyewaan pada jam-jam tertentu, khususnya selama periode sibuk pergi dan pulang kerja.') 

with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Visualisasi Data Bike Sharing")
    dataset, analisis_1, analisis_2, analisis_3, analisis_4, analisis_5, analisis_6 = st.tabs(["Dataset", "#1 Titan El Haqi", "#2 Marsya Awliya Sabrina", "#3 Ariq Hikari Hidayat", "#4 10122257 - M. Ghazy Al H. H.", "#5 10122260 - Adisya Ainun Fatihah", "#6 Muhammad Naufal Ghifari"])

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