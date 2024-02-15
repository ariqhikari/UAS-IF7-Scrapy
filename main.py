import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu


@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def Dataset() :
    st.header("Pengenalan Dataset")
def Analisis_1() :
    st.header("Ini Tab 1")
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