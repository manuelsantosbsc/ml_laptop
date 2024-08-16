
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

company = st.selectbox('Brand', df['Company'].unique())
company = st.selectbox('Brand', df['Company'].unique())
lap_type = st.selectbox("Type", df['TypeName'].unique())
ram = st.selectbox("Ram(in GB)",df['Ram'].unique())
weight = st.selectbox("Weight of the Laptop",df['Weight'].unique())
ghz = st.selectbox("CPU GHz", df['CPU_GHz'].unique())
touchscreen = st.selectbox("TouchScreen", ['No', 'Yes'])
ips = st.selectbox("IPS", ['No', 'Yes'])
inches = st.selectbox('Screen Size',df['Inches'].unique())
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox('CPU',df['Cpu_brand'].unique())
ssd = st.selectbox('SSD(in GB)',df['HDD_GB'].unique())
hdd = st.selectbox('HDD(in GB)',df['SSD_GB'].unique())
gpu = st.selectbox('GPU',df['Gpu_brand'].unique())
os = st.selectbox('OS',df['os'].unique())
screen_width=0
#Prediccion

if st.button('Predecir Precio'):
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == "Yes":
        ips = 1
    else:
        ips = 0
      
    screen_width = int(resolution.split('x')[0])
    input_data = pd.DataFrame([[ssd, ghz, ram, weight, ips, touchscreen, screen_width, hhd, inches]],
                          columns=['SSD_GB', 'Cpu_hgz', 'RAM', 'Weight', 'IPS', 'Touchscreen', 'screen_width', 'HHD_GB', 'Inches'])
    scaler = StandardScaler()
    input_scaled = scaler.fit_transform(input_data)

    # Realizar predicción
    prediction = modelo.predict(input_data )

    # Mostrar predicción
    st.write(f'Precio predecido: {prediction[0]:.2f} euros')

  
