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

    st.write('Dataset ini adalah kumpulan data tentang penyewaan sepeda berbagi di Washington D.C., USA, selama dua tahun (2011 dan 2012). Data tersedia dalam format per jam dan per hari. Informasi yang tersedia meliputi tanggal, musim, tahun, bulan, jam, hari libur, hari kerja, kondisi cuaca, suhu, kelembapan, kecepatan angin, dan jumlah pengguna yang menyewa sepeda (baik pengguna casual maupun terdaftar), serta total jumlah sewa sepeda. Tujuan utama dataset ini adalah untuk prediksi jumlah sewa sepeda berdasarkan lingkungan dan musim, serta deteksi peristiwa atau anomali yang berkaitan dengan pola sewa sepeda.')

    day = pd.read_csv('dataset/day.csv')
    hour = pd.read_csv('dataset/hour.csv')

    st.write('Tabel Day')
    st.dataframe(day)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    st.write('Tabel Hour')
    st.dataframe(hour)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

def Analisis_1() :
    st.header("Pertanyaan 1")
    st.subheader('Bagaimana perbandingan jumlah Penyewaan sepeda antara tahun 2011 dan 2012?')
    st.caption('10122238 - Titan El Haqi')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    cnt2011 = pd.read_csv('dataset/titan-cnt2011.csv')
    cnt2012 = pd.read_csv('dataset/titan-cnt2012.csv')

    total2011 = cnt2011['cnt'].sum()
    total2012 = cnt2012['cnt'].sum()

    st.write('Tabel Jumlah Penyewaan Sepeda Tahun 2011')
    st.dataframe(cnt2011)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    st.write('Tabel Jumlah Penyewaan Sepeda Tahun 2012')
    st.dataframe(cnt2012)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    fig, ax = plt.subplots()
    ax.bar(['2011', '2012'], [total2011, total2012], color='green')
    ax.set_title('Grafik Perbandingan Jumlah Penyewa Sepeda, 2011 dan 2012')
    ax.set_ylabel('Jumlah Penyewa')
    ax.set_xlabel('Tahun')

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Grafik Perbandingan Jumlah Penyewa Sepeda, 2011 dan 2012") :
        st.write('Dilihat dari analisis pada dataset Bike Sharing, terdapat peningkatan jumlah penyewa dari tahun 2011 ke tahun 2012 sebanyak 64.87%. Hasil ini didapatkan dari mengambil selisih penyewa pada tahun 2011 dan 2012, kemudian dibagi dengan total penyewa pada tahun 2011.') 
    
def Analisis_2() :
    st.header("Pertanyaan 2")
    st.subheader('Apakah ada penurunan signifikan dalam penggunaan sepeda saat cuaca buruk?')
    st.caption('10122241 - Marsya Awliya Sabrina')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    percentage_reduction = pd.read_csv('dataset/marsya-percentage_reduction.csv')

    st.write('Tabel Percentage Reduction')
    st.dataframe(percentage_reduction)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Buat aplikasi Streamlit
    st.title('Persentase Penurunan Penggunaan Sepeda saat Cuaca Buruk')

    # Tampilkan plot menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(percentage_reduction, marker='o')
    ax.set_title('Persentase Penurunan Penggunaan Sepeda saat Cuaca Buruk')
    ax.set_xlabel('Jam (0-23)')
    ax.set_ylabel('Persentase Penurunan')
    ax.grid(True)

    # Tampilkan plot di aplikasi Streamlit
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Grafik Persentase Penurunan Penggunaan Sepeda saat Cuaca Buruk") :
        st.write('Berdasarkan analisis menggunakan dataset sepeda, tampaknya ada potensi penurunan signifikan dalam penggunaan sepeda saat cuaca buruk. Analisis dilakukan dengan membandingkan total rental sepeda untuk setiap jam pada kondisi cuaca buruk dengan total rental sepeda pada semua kondisi cuaca. Hasilnya dapat divisualisasikan dalam bentuk grafik persentase penurunan penggunaan sepeda pada berbagai jam. Kesimpulan akhirnya bergantung pada pola yang terlihat dalam grafik tersebut.') 

def Analisis_3() :
    st.header("Pertanyaan 3")
    st.subheader('Apakah ada pengaruh hari libur terhadap jumlah sepeda yang disewa?')
    st.caption('10122254 - Ariq Hikari Hidayat')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    holiday_data= pd.read_csv('dataset/ariq-holiday_data.csv')
    non_holiday_data= pd.read_csv('dataset/ariq-non_holiday_data.csv')

    st.write('Tabel Holiday')
    st.dataframe(holiday_data)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    st.write('Tabel Non Holiday')
    st.dataframe(non_holiday_data)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    avg_rental_holiday = holiday_data['cnt'].mean()
    avg_rental_non_holiday = non_holiday_data['cnt'].mean()

    # Plot
    fig, ax = plt.subplots()
    ax.bar(['Weekend', 'Weekday'], [avg_rental_holiday, avg_rental_non_holiday])
    ax.set_title('Grafik Rata-rata Penyewaan Sepeda pada Hari Libur vs Non-Libur')
    ax.set_ylabel('Jumlah Rata-Rata Penyewaan Sepeda')

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Grafik Rata-rata Penyewaan Sepeda pada Hari Libur vs Non-Libur") :
        st.write('Berdasarkan analisis data, terdapat perbedaan yang signifikan dalam rata-rata jumlah sepeda yang disewa antara hari libur dan bukan hari libur. Visualisasi menunjukkan bahwa rata-rata peminjaman sepeda lebih tinggi pada hari-hari yang bukan hari libur. Oleh karena itu, dapat disimpulkan bahwa hari libur memiliki pengaruh terhadap pola peminjaman sepeda, dengan potensi menurunnya permintaan pada hari libur dibandingkan dengan hari-hari biasa.') 

def Analisis_4() :
    st.header("Pertanyaan 4")
    st.subheader('Apa pengaruh faktor cuaca terhadap jumlah sewa sepeda harian?')
    st.caption('10122257 - M. Ghazy Al H. H.')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    average_rentals_by_weather = pd.read_csv('dataset/ghazy-average_rentals_by_weather.csv')

    st.write('Tabel Average Rentals by Weather')
    st.dataframe(average_rentals_by_weather)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Tampilkan plot menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(average_rentals_by_weather['weathersit'], average_rentals_by_weather['cnt'], color='skyblue')
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Rata-rata Jumlah Sewa Sepeda')
    ax.tick_params(axis='x', rotation=90)

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Grafik Rata-rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca") :
        st.write('Kondisi cuaca berpengaruh pada jumlah sewa sepeda harian, dan kondisi cuaca yang lebih baik cenderung meningkatkan jumlah sewa sepeda. Namun, cuaca sedang memiliki variasi yang lebih besar dalam jumlah sewa.') 

def Analisis_5() :
    st.header("Pertanyaan 5")
    st.subheader('Bagaimana cara mendeteksi peristiwa atau anomali dalam data penyewaan sepeda?')
    st.caption('10122260 - Adisya Ainun Fatihah')
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
    
    day_df= pd.read_csv('dataset/adisya-day_df.csv')
    anomalies= pd.read_csv('dataset/adisya-anomalies.csv')

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    anomalies['dteday'] = pd.to_datetime(anomalies['dteday'])

    st.write('Tabel Day')
    st.dataframe(day_df)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    st.write('Tabel Anomalies')
    st.dataframe(anomalies)
    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
    
    st.title('Grafik Jumlah Penyewaan Sepeda')
    fig, ax = plt.subplots()
    ax.plot(day_df['dteday'], day_df['cnt'])
    ax.scatter(anomalies['dteday'], anomalies['cnt'], c='red')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah penyewaan sepeda')
    ax.tick_params(axis='x', rotation=90)
    ax.set_xticklabels([])  # Cara 1: Set label sumbu x menjadi daftar kosong

    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Grafik Jumlah Penyewaan Sepeda") :
        st.write('Peristiwa atau anomali dalam data penyewaan sepeda dapat dideteksi menggunakan berbagai teknik, seperti metode statistik, algoritma pembelajaran mesin, atau algoritma pembelajaran tidak terbimbing. Salah satu metode sederhana dan mudah diterapkan adalah dengan menggunakan standar deviasi bergulir. Standar deviasi bergulir adalah rata-rata dari standar deviasi dari serangkaian data dalam periode waktu tertentu. Standar deviasi bergulir dapat digunakan untuk melacak perubahan dalam variabilitas data dari waktu ke waktu, dan untuk mengidentifikasi anomali.') 

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