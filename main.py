import streamlit as st
import pandas as pd
import matplotlib as plt
import matplotlib.pylab as plt
from streamlit_option_menu import option_menu



@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def Dataset() :
    st.header("Pengenalan Dataset")
def Analisis_1() :
    #Dataset
    dteday_cnt = pd.read_csv('dataset/titan-dteday_cnt.csv')
    #Extra
    st.header("Pertanyaan 1")
    st.subheader("Seperti apa perbandingan jumlah peminjaman sepeda antara tahun 2011 dan 2012?")
    st.caption("10122238 - Titan El Haqi")
    st.dataframe(dteday_cnt.head())
    st.subheader("Jumlah peminjam sepeda pada tahun 2011 dan 2012")
    #Seleksi data 2011 dan 2012
    cnt2011 = dteday_cnt[dteday_cnt['dteday'].str[:4] == '2011']
    cnt2012 = dteday_cnt[dteday_cnt['dteday'].str[:4] == '2012']
    #Totalkan
    total2011 = cnt2011['cnt'].sum()
    total2012 = cnt2012['cnt'].sum()
    #Data untuk ditampilkan
    data = {'Year': ['2011', '2012'], 'Total Rentals': [total2011, total2012]}
    df = pd.DataFrame(data)
    #Tampilkan pada chart
    st.bar_chart(df.set_index('Year'))
    #Menampilkan jumlah dan kesimpulan  
    st.write('Jumlah penyewa pada tahun 2011:', total2011)
    st.write('Jumlah penyewa pada tahun 2012:', total2012)
    
    with st.expander("Kesimpulan") :
        st.write("Dilihat dari analisis pada dataset Bike Sharing, terdapat peningkatan jumlah penyewa dari tahun 2011 ke tahun 2012 sebanyak 64.87%. Hasil ini didapatkan dari mengambil selisih penyewa pada tahun 2011 dan 2012, kemudian dibagi dengan total penyewa pada tahun 2011.")
    
    
    
def Analisis_2() :
    st.header("Ini Tab 2")
def Analisis_3() :
    st.header("Ini Tab 3")
def Analisis_4() :
    st.header("Ini Tab 4")
def Analisis_5() :
    st.header("Ini Tab 5")
def Analisis_6() :
    st.header("Ini Tab 6")

with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Visualisasi Data Bike Sharing")
    dataset, analisis_1, analisis_2, analisis_3, analisis_4, analisis_5, analisis_6 = st.tabs(["Dataset", "Analisis 1", "Analisis 2", "Analisis 3", "Analisis 4", "Analisis 5", "Analisis 6"])

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