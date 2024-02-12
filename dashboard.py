import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu


@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

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
    st.header(f"Dashboard Analisis Bike Sharing")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Analisis 1", "Analisis 2", "Analisis 3", "Analisis 4", "Analisis 5", "Analisis 6"])

    with tab1 :
        Analisis_1()
    with tab2 :
        Analisis_2()
    with tab3 :
        Analisis_3()
    with tab4 :
        Analisis_4()
    with tab5 :
        Analisis_5()
    with tab6 :
        Analisis_6()
