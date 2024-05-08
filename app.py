import streamlit as st
import numpy as np
import streamlit.components.v1 as stc
from PIL import Image 


# Tampilkan gambar dengan lebar penuh dan tinggi 200px
st.markdown(
    """
    <style>
    .full-width-img {
        width: 100%;
        height: 200px; 
        object-fit: cover; 
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    '<img class="full-width-img" src="https://resources.news.e.abb.com/images/2023/1/23/0/ABB_Pure_Harvest_smart_farm.jpg">',
    unsafe_allow_html=True
)

# Atur gaya untuk teks judul
st.markdown(
    """
    <style>
    .text {
        font-size: 30px;
        color: green;
        font-family: Century Gothic, Futura, sans-serif;
    }
    .input-text {
        font-size: 16px;
        color: black;
        font-family: Arial, sans-serif;
    }
    </style>
    """
    , unsafe_allow_html=True
)

# Tampilkan judul
st.markdown('<h1 class="text">Smart GreenHouse Using Fuzzy Logic</h1>', unsafe_allow_html=True)

# Tampilkan teks "Input" dengan warna hitam
st.markdown('<span class="input-text">Input Variable</span>', unsafe_allow_html=True)

# Membuat dua kolom untuk input
col1, col2 = st.columns(2)

# Kolom pertama
with col1:
#temperature
    def very_low_temp(x):
        if x <= -10:
            return 1
        elif -10 < x < 2:
            return (1 - (x + 10) / 2)
        else:
            return 0

    def low_temp(x):
        if 0 <= x <= 7:
            return (x-0) / 7
        elif 7 < x < 14:
            return (1 - (x - 7) / 7)
        else:
            return 0
    
    def medium_temp(x):
        if 10 <= x <= 18:
            return (x - 10) / 8
        elif 18 < x < 26:
            return (1 - (x - 18) / 8)
        else:
            return 0
        
    def high_temp(x):
        if 20 <= x <= 29:
            return (x - 20) / 9
        elif 20 < x < 29:
            return (1 - (x - 20) / 9)
        else:
            return 0
        
    def very_high_temp(x):
        if 30 <= x <= 38:
            return (x - 30) / 8
        elif 38 < x <= 50:
            return 1
        else:
            return 0
        
    # Define other membership functions (medium, high, very high) similarly...

    # Get user input for temperature
    temperature_input = st.number_input('Enter Temperature (°C)', -10.0, 50.0, step=1.0)

    # Calculate membership values for each category
    temperatureVeryLow = very_low_temp(temperature_input)
    temperatureLow = low_temp(temperature_input)
    temperatureMedium = medium_temp(temperature_input)
    temperatureHigh = high_temp(temperature_input)
    temperatureVeryHigh = very_high_temp(temperature_input)
    # Calculate other membership values (medium, high, very high) similarly...

    # Display membership values for each category
    st.write(f"`Very Low: {temperatureVeryLow}`" + "  " + f"`Low: {temperatureLow}`"+ "  " + f"`Medium: {temperatureMedium}`"+ "  " + f"`High: {temperatureHigh}`"+ "  " + f"`Very High: {temperatureVeryHigh}`", font='Arial')
    # Display other membership values (medium, high, very high) similarly...


#Humidity
    def very_low_humd(x):
        if x <= 0:
            return 1
        elif 0 < x < 20:
            return (1 - (x - 0) / 20)
        else:
            return 0

    def low_humd(x):
        if 10 <= x <= 25:
            return (x-10) / 15
        elif 25 < x < 40:
            return (1 - (x - 25) / 15)
        else:
            return 0
    
    def medium_humd(x):
        if 30 <= x <= 45:
            return (x - 30) / 15
        elif 45 < x < 60:
            return (1 - (x - 45) / 15)
        else:
            return 0
        
    def high_humd(x):
        if 50 <= x <= 66:
            return (x - 50) / 16
        elif 66 < x < 82:
            return (1 - (x - 66) / 16)
        else:
            return 0
        
    def very_high_humd(x):
        if 72 <= x <= 82:
            return (x - 72) / 10
        elif 82 < x <= 100:
            return 1
        else:
            return 0
        
    # Define other membership functions (medium, high, very high) similarly...

    # Get user input for temperature
    humidity_input = st.number_input('Enter Humidity (%)', 0.0, 100.0, step=1.0)

    # Calculate membership values for each category
    humidityVeryLow = very_low_humd(humidity_input)
    humidityLow = low_humd(humidity_input)
    humidityMedium = medium_humd(humidity_input)
    humidityHigh = high_humd(humidity_input)
    humidityVeryHigh = very_high_humd(humidity_input)
    # Calculate other membership values (medium, high, very high) similarly...

    # Display membership values for each category
    st.write(f"`Very Low: {humidityVeryLow}`" + "  " + f"`Low: {humidityLow}`"+ "  " + f"`Medium: {humidityMedium}`"+ "  " + f"`High: {humidityHigh}`"+ "  " + f"`Very High: {humidityVeryHigh}`", font='Arial')
    # Display other membership values (medium, high, very high) similarly...

# Kolom kedua
with col2:
#Soil Moisture
    def very_low_soilmoisture(x):
        if x <= 0:
            return 1
        elif 0 < x < 20:
            return (1 - (x - 0) / 20)
        else:
            return 0

    def low_soilmoisture(x):
        if 10 <= x <= 25:
            return (x-10) / 15
        elif 25 < x < 40:
            return (1 - (x - 25) / 15)
        else:
            return 0
    
    def medium_soilmoisture(x):
        if 30 <= x <= 45:
            return (x - 30) / 15
        elif 45 < x < 60:
            return (1 - (x - 45) / 15)
        else:
            return 0
        
    def high_soilmoisture(x):
        if 50 <= x <= 66:
            return (x - 50) / 16
        elif 66 < x < 82:
            return (1 - (x - 66) / 16)
        else:
            return 0
        
    def very_high_soilmoisture(x):
        if 72 <= x <= 82:
            return (x - 72) / 10
        elif 82 < x <= 100:
            return 1
        else:
            return 0
        
    # Define other membership functions (medium, high, very high) similarly...

    # Get user input for temperature
    soilmoisture_input = st.number_input('Enter Soil Moisture (%)', 0.0, 100.0, step=1.0)

    # Calculate membership values for each category
    soilmoistureVeryLow = very_low_soilmoisture(soilmoisture_input)
    soilmoistureLow = low_soilmoisture(soilmoisture_input)
    soilmoistureMedium = medium_soilmoisture(soilmoisture_input)
    soilmoistureHigh = high_soilmoisture(soilmoisture_input)
    soilmoistureVeryHigh = very_high_soilmoisture(soilmoisture_input)
    # Calculate other membership values (medium, high, very high) similarly...

    # Display membership values for each category
    st.write(f"`Very Low: {soilmoistureVeryLow}`" + "  " + f"`Low: {soilmoistureLow}`"+ "  " + f"`Medium: {soilmoistureMedium}`"+ "  " + f"`High: {soilmoistureHigh}`"+ "  " + f"`Very High: {soilmoistureVeryHigh}`", font='Arial')
    # Display other membership values (medium, high, very high) similarly...

#Light Intensity
    def very_low_lightintensity(x):
        if x <= 0:
            return 1
        elif 0 < x < 0.3:
            return (1 - (x - 0) / 0.3)
        else:
            return 0

    def low_lightintensity(x):
        if 0.3 <= x <= 0.6:
            return (x-0.3) / 0.3
        elif 0.6 < x < 0.8:
            return (1 - (x - 0.6) / 0.2)
        else:
            return 0
    
    def medium_lightintensity(x):
        if 0.7 <= x <= 1:
            return (x - 0.7) / 0.3
        elif 1 < x < 1.2:
            return (1 - (x - 1) / 1.2)
        else:
            return 0
        
    def high_lightintensity(x):
        if 1 <= x <= 1.33:
            return (x - 1) / 0.33
        elif 1.33 < x < 1.65:
            return (1 - (x - 1.33) / 0.32)
        else:
            return 0
        
    def very_high_lightintensity(x):
        if 1.6 <= x <= 1.65:
            return (x - 1.6) / 0.05
        elif 1.65 < x <= 2:
            return 1
        else:
            return 0
        
    # Define other membership functions (medium, high, very high) similarly...

    # Get user input for temperature
    lightintensity_input = st.number_input('Enter Light Intensity (10⁴ lux)', 0.0, 2.0, step=0.01)

    # Calculate membership values for each category
    lightintensityVeryLow = very_low_lightintensity(lightintensity_input)
    lightintensityLow = low_lightintensity(lightintensity_input)
    lightintensityMedium = medium_lightintensity(lightintensity_input)
    lightintensityHigh = high_lightintensity(lightintensity_input)
    lightintensityVeryHigh = very_high_lightintensity(lightintensity_input)
    # Calculate other membership values (medium, high, very high) similarly...

    # Display membership values for each category
    st.write(f"`Very Low: {lightintensityVeryLow}`" + "  " + f"`Low: {lightintensityLow}`"+ "  " + f"`Medium: {lightintensityMedium}`"+ "  " + f"`High: {lightintensityHigh}`"+ "  " + f"`Very High: {lightintensityVeryHigh}`", font='Arial')
    # Display other membership values (medium, high, very high) similarly...

##-------------------------Define the Rules----------------------------------##
Rule_1_heatingVeryHigh = np.fmin(temperatureVeryLow, humidityVeryLow)
Rule_2_heatingVeryHigh = np.fmin(temperatureVeryLow, humidityLow)
Rule_3_heatingHigh = np.fmin(temperatureVeryLow, humidityMedium)
Rule_4_heatingHigh = np.fmin(temperatureVeryLow, humidityHigh)
Rule_5_heatingHigh = np.fmin(temperatureVeryLow, humidityVeryHigh)
Rule_6_heatingHigh = np.fmin(temperatureLow, humidityVeryLow)
Rule_7_heatingHigh = np.fmin(temperatureLow, humidityLow)
Rule_8_heatingHigh = np.fmin(temperatureLow, humidityMedium)
Rule_9_heatingMedium = np.fmin(temperatureLow, humidityHigh)
Rule_10_heatingMedium = np.fmin(temperatureLow, humidityVeryHigh)
Rule_11_heatingMedium = np.fmin(temperatureMedium, humidityVeryLow)
Rule_12_heatingMedium = np.fmin(temperatureMedium, humidityLow)
Rule_13_heatingMedium = np.fmin(temperatureMedium, humidityMedium)
Rule_14_heatingMedium = np.fmin(temperatureMedium, humidityHigh)
Rule_15_heatingLow = np.fmin(temperatureMedium, humidityVeryHigh)
Rule_16_heatingLow = np.fmin(temperatureHigh, humidityVeryLow)
Rule_17_heatingLow = np.fmin(temperatureHigh, humidityLow)
Rule_18_heatingLow = np.fmin(temperatureHigh, humidityMedium)
Rule_19_heatingLow = np.fmin(temperatureHigh, humidityHigh)
Rule_20_heatingLow = np.fmin(temperatureHigh, humidityVeryHigh)
Rule_21_heatingVeryLow = np.fmin(temperatureVeryHigh, humidityVeryLow)
Rule_22_heatingVeryLow = np.fmin(temperatureVeryHigh, humidityLow)
Rule_23_heatingVeryLow = np.fmin(temperatureVeryHigh, humidityMedium)
Rule_24_heatingVeryLow = np.fmin(temperatureVeryHigh, humidityHigh)
Rule_25_heatingVeryLow = np.fmin(temperatureVeryHigh, humidityVeryHigh)
Rule_26_coolingVeryLow = np.fmin(temperatureVeryLow, humidityVeryLow)
Rule_27_coolingVeryLow = np.fmin(temperatureVeryLow, humidityLow)
Rule_28_coolingVeryLow = np.fmin(temperatureVeryLow, humidityMedium)
Rule_29_coolingVeryLow = np.fmin(temperatureVeryLow, humidityHigh)
Rule_30_coolingVeryLow = np.fmin(temperatureVeryLow, humidityVeryHigh)
Rule_31_coolingLow = np.fmin(temperatureLow, humidityVeryLow)
Rule_32_coolingLow = np.fmin(temperatureLow, humidityLow)
Rule_33_coolingLow = np.fmin(temperatureLow, humidityMedium)
Rule_34_coolingLow = np.fmin(temperatureLow, humidityHigh)
Rule_35_coolingLow = np.fmin(temperatureLow, humidityVeryHigh)
Rule_36_coolingLow = np.fmin(temperatureMedium, humidityVeryLow)
Rule_37_coolingMedium = np.fmin(temperatureMedium, humidityLow)
Rule_38_coolingMedium = np.fmin(temperatureMedium, humidityMedium)
Rule_39_coolingMedium = np.fmin(temperatureMedium, humidityHigh)
Rule_40_coolingMedium = np.fmin(temperatureMedium, humidityVeryHigh)
Rule_41_coolingMedium = np.fmin(temperatureHigh, humidityVeryLow)
Rule_42_coolingMedium = np.fmin(temperatureHigh, humidityLow)
Rule_43_coolingHigh = np.fmin(temperatureHigh, humidityMedium)
Rule_44_coolingHigh = np.fmin(temperatureHigh, humidityHigh)
Rule_45_coolingHigh = np.fmin(temperatureHigh, humidityVeryHigh)
Rule_46_coolingHigh = np.fmin(temperatureVeryHigh, humidityVeryLow)
Rule_47_coolingHigh = np.fmin(temperatureVeryHigh, humidityLow)
Rule_48_coolingHigh = np.fmin(temperatureVeryHigh, humidityMedium)
Rule_49_coolingVeryHigh = np.fmin(temperatureVeryHigh, humidityHigh)
Rule_50_coolingVeryHigh = np.fmin(temperatureVeryHigh, humidityVeryHigh)
Rule_51_irrigationVeryHigh = np.fmin(soilmoistureVeryLow, humidityVeryLow)
Rule_52_irrigationHigh = np.fmin(soilmoistureVeryLow, humidityLow)
Rule_53_irrigationHigh = np.fmin(soilmoistureVeryLow, humidityMedium)
Rule_54_irrigationMedium = np.fmin(soilmoistureVeryLow, humidityHigh)
Rule_55_irrigationVeryLow = np.fmin(soilmoistureVeryLow, humidityVeryHigh)
Rule_56_irrigationVeryHigh = np.fmin(soilmoistureLow, humidityVeryLow)
Rule_57_irrigationHigh = np.fmin(soilmoistureLow, humidityLow)
Rule_58_irrigationMedium = np.fmin(soilmoistureLow, humidityMedium)
Rule_59_irrigationMedium = np.fmin(soilmoistureLow, humidityHigh)
Rule_60_irrigationLow = np.fmin(soilmoistureLow, humidityVeryHigh)
Rule_61_irrigationHigh = np.fmin(soilmoistureMedium, humidityVeryLow)
Rule_62_irrigationHigh = np.fmin(soilmoistureMedium, humidityLow)
Rule_63_irrigationMedium = np.fmin(soilmoistureMedium, humidityMedium)
Rule_64_irrigationMedium = np.fmin(soilmoistureMedium, humidityHigh)
Rule_65_irrigationMedium = np.fmin(soilmoistureMedium, humidityVeryHigh)
Rule_66_irrigationHigh = np.fmin(soilmoistureHigh, humidityVeryLow)
Rule_67_irrigationMedium = np.fmin(soilmoistureHigh, humidityLow)
Rule_68_irrigationMedium = np.fmin(soilmoistureHigh, humidityMedium)
Rule_69_irrigationLow = np.fmin(soilmoistureHigh, humidityHigh)
Rule_70_irrigationVeryLow = np.fmin(soilmoistureHigh, humidityVeryHigh)
Rule_71_irrigationMedium = np.fmin(soilmoistureVeryHigh, humidityVeryLow)
Rule_72_irrigationMedium = np.fmin(soilmoistureVeryHigh, humidityLow)
Rule_73_irrigationLow = np.fmin(soilmoistureVeryHigh, humidityMedium)
Rule_74_irrigationLow = np.fmin(soilmoistureVeryHigh, humidityHigh)
Rule_75_irrigationVeryLow = np.fmin(soilmoistureVeryHigh, humidityVeryHigh)
Rule_76_shadingVeryLow = np.fmin(temperatureVeryLow, lightintensityVeryLow)
Rule_77_shadingVeryLow = np.fmin(temperatureVeryLow, lightintensityLow)
Rule_78_shadingLow = np.fmin(temperatureVeryLow, lightintensityMedium)
Rule_79_shadingMedium = np.fmin(temperatureVeryLow, lightintensityHigh)
Rule_80_shadingMedium = np.fmin(temperatureVeryLow, lightintensityVeryHigh)
Rule_81_shadingVeryLow = np.fmin(temperatureLow, lightintensityVeryLow)
Rule_82_shadingLow = np.fmin(temperatureLow, lightintensityLow)
Rule_83_shadingLow = np.fmin(temperatureLow, lightintensityMedium)
Rule_84_shadingMedium = np.fmin(temperatureLow, lightintensityHigh)
Rule_85_shadingHigh = np.fmin(temperatureLow, lightintensityVeryHigh)
Rule_86_shadingVeryLow = np.fmin(temperatureMedium, lightintensityVeryLow)
Rule_87_shadingLow = np.fmin(temperatureMedium, lightintensityLow)
Rule_88_shadingMedium = np.fmin(temperatureMedium, lightintensityMedium)
Rule_89_shadingMedium = np.fmin(temperatureMedium, lightintensityHigh)
Rule_90_shadingHigh = np.fmin(temperatureMedium, lightintensityVeryHigh)
Rule_91_shadingLow = np.fmin(temperatureHigh, lightintensityVeryLow)
Rule_92_shadingLow = np.fmin(temperatureHigh, lightintensityLow)
Rule_93_shadingMedium = np.fmin(temperatureHigh, lightintensityMedium)
Rule_94_shadingHigh = np.fmin(temperatureHigh, lightintensityHigh)
Rule_95_shadingHigh = np.fmin(temperatureHigh, lightintensityVeryHigh)
Rule_96_shadingLow = np.fmin(temperatureVeryHigh, lightintensityVeryLow)
Rule_97_shadingMedium = np.fmin(temperatureVeryHigh, lightintensityLow)
Rule_98_shadingMedium = np.fmin(temperatureVeryHigh, lightintensityMedium)
Rule_99_shadingHigh = np.fmin(temperatureVeryHigh, lightintensityHigh)
Rule_100_shadingVeryHigh = np.fmin(temperatureVeryHigh, lightintensityVeryHigh)

##-------------------------Formula to Calculate----------------------------------##

#Formula to Calculate Heating
def centeroid_tria(x1,x2,x3):

  x = round((x1 + x2 + x3) / 3, 2)
  return x

def centeroid_rect(x1 ,x2 ):
  center = (x1+x2)/2
  return center

c_HVL_tri=centeroid_tria(1.9, 1.9, 2)
c_HVL_rect=centeroid_rect(0, 1.9)
area_HVL_tri=.5*1*(2-1.9)
print('area_HVL_tri' ,area_HVL_tri)
area_HVL_rect=1*(1.9)
print('area_HVL_rect' ,area_HVL_rect)

Heating_VL=(((c_HVL_tri*area_HVL_tri)+(c_HVL_rect*area_HVL_rect))//(area_HVL_tri+area_HVL_rect))
print(Heating_VL)

c_HL_tri=centeroid_tria(1.9, 3, 4)
area_HL_tri=.5*1*(4-1.9)
print('area_HL_tri' ,area_HL_tri)

Heating_L=(c_HL_tri)
print(Heating_L)

c_HM_tri=centeroid_tria(3, 4.5, 6)
area_HM_tri=.5*1*(6-3)
print('area_HM_tri' ,area_HM_tri)

Heating_M=(c_HM_tri)
print(Heating_M)

c_HH_tri=centeroid_tria(5, 6.5, 8)
area_HH_tri=.5*1*(8-5)
print('area_HH_tri' ,area_HH_tri)

Heating_H=(c_HH_tri)
print(Heating_H)

c_HVH_tri=centeroid_tria(7, 8, 8)
c_HVH_rect=centeroid_rect(8, 10)
area_HVH_tri=.5*1*(8-7)
print('area_HVH_tri' ,area_HVH_tri)
area_HVH_rect=1*(2)
print('area_HVH_rect' ,area_HVH_rect)

Heating_VH=(((c_HVH_tri*area_HVH_tri)+(c_HVH_rect*area_HVH_rect))//(area_HVH_tri+area_HVH_rect))
print(Heating_VH)

#Formula to Calculate Cooling
def centeroid_tria(x1,x2,x3):

  x = round((x1 + x2 + x3) / 3, 2)
  return x

def centeroid_rect(x1 ,x2 ):
  center = (x1+x2)/2
  return center

c_CVL_tri=centeroid_tria(2.5, 2.5, 5)
c_CVL_rect=centeroid_rect(0, 2.5)
area_CVL_tri=.5*1*(5-2.5)
print('area_CVL_tri' ,area_CVL_tri)
area_CVL_rect=1*(2.5)
print('area_CVL_rect' ,area_CVL_rect)

Cooling_VL=(((c_CVL_tri*area_CVL_tri)+(c_CVL_rect*area_CVL_rect))//(area_CVL_tri+area_CVL_rect))
print(Cooling_VL)

c_CL_tri=centeroid_tria(0, 6.3, 12.5)
area_CL_tri=.5*1*(12.5-0)
print('area_CL_tri' ,area_CL_tri)

Cooling_L=(c_CL_tri)
print(Cooling_L)

c_CM_tri=centeroid_tria(10, 12.5, 15)
area_CM_tri=.5*1*(15-10)
print('area_CM_tri' ,area_CM_tri)

Cooling_M=(c_CM_tri)
print(Cooling_M)

c_CH_tri=centeroid_tria(14, 17, 20)
area_CH_tri=.5*1*(20-14)
print('area_CH_tri' ,area_CH_tri)

Cooling_H=(c_CH_tri)
print(Cooling_H)

c_CVH_tri=centeroid_tria(18, 20, 20)
c_CVH_rect=centeroid_rect(20, 25)
area_CVH_tri=.5*1*(25-20)
print('area_CVH_tri' ,area_CVH_tri)
area_CVH_rect=1*(5)
print('area_CVH_rect' ,area_CVH_rect)

Cooling_VH=(((c_CVH_tri*area_CVH_tri)+(c_CVH_rect*area_CVH_rect))//(area_CVH_tri+area_CVH_rect))
print(Cooling_VH)

#Formula to Calculate Irrigation
def centeroid_tria(x1,x2,x3):

  x = round((x1 + x2 + x3) / 3, 2)
  return x

def centeroid_rect(x1 ,x2 ):
  center = (x1+x2)/2
  return center

c_IVL_tri=centeroid_tria(2, 2, 10)
c_IVL_rect=centeroid_rect(0, 2)
area_IVL_tri=.5*1*(10-2)
print('area_IVL_tri' ,area_IVL_tri)
area_IVL_rect=1*(2)
print('area_IVL_rect' ,area_IVL_rect)

Irrigation_VL=(((c_IVL_tri*area_IVL_tri)+(c_IVL_rect*area_IVL_rect))//(area_IVL_tri+area_IVL_rect))
print(Irrigation_VL)

c_IL_tri=centeroid_tria(0, 8, 20)
area_IL_tri=.5*1*(20-0)
print('area_IL_tri' ,area_IL_tri)

Irrigation_L=(c_IL_tri)
print(Irrigation_L)

c_IM_tri=centeroid_tria(11, 20, 30)
area_IM_tri=.5*1*(30-11)
print('area_IM_tri' ,area_IM_tri)

Irrigation_M=(c_IM_tri)
print(Irrigation_M)

c_IH_tri=centeroid_tria(21, 30, 40)
area_IH_tri=.5*1*(40-21)
print('area_IH_tri' ,area_IH_tri)

Irrigation_H=(c_IH_tri)
print(Irrigation_H)

c_IVH_tri=centeroid_tria(32, 40, 40)
c_IVH_rect=centeroid_rect(40, 45)
area_IVH_tri=.5*1*(40-32)
print('area_IVH_tri' ,area_IVH_tri)
area_IVH_rect=1*(45-40)
print('area_IVH_rect' ,area_IVH_rect)

Irrigation_VH=(((c_IVH_tri*area_IVH_tri)+(c_IVH_rect*area_IVH_rect))//(area_IVH_tri+area_IVH_rect))
print(Irrigation_VH)

#Formula to Calculate Shading
def centeroid_tria(x1,x2,x3):

  x = round((x1 + x2 + x3) / 3, 2)
  return x

def centeroid_rect(x1 ,x2 ):
  center = (x1+x2)/2
  return center

c_SVL_tri=centeroid_tria(20, 20, 40)
c_SVL_rect=centeroid_rect(0, 20)
area_SVL_tri=.5*1*(40-20)
print('area_SVL_tri' ,area_SVL_tri)
area_SVL_rect=1*(20)
print('area_SVL_rect' ,area_SVL_rect)

Shading_VL=(((c_SVL_tri*area_SVL_tri)+(c_SVL_rect*area_SVL_rect))//(area_SVL_tri+area_SVL_rect))
print(Shading_VL)

c_SL_tri=centeroid_tria(0, 60, 120)
area_SL_tri=.5*1*(120-0)
print('area_SL_tri' ,area_SL_tri)

Shading_L=(c_SL_tri)
print(Shading_L)

c_SM_tri=centeroid_tria(100, 140, 180)
area_SM_tri=.5*1*(180-100)
print('area_SM_tri' ,area_SM_tri)

Shading_M=(c_SM_tri)
print(Shading_M)

c_SH_tri=centeroid_tria(150, 173, 195)
area_SH_tri=.5*1*(195-150)
print('area_SH_tri' ,area_SH_tri)

Shading_H=(c_SH_tri)
print(Shading_H)

c_SVH_tri=centeroid_tria(190, 190, 195)
c_SVH_rect=centeroid_rect(195, 250)
area_SVH_tri=.5*1*(195-190)
print('area_SVH_tri' ,area_SVH_tri)
area_SVH_rect=1*(250-195)
print('area_SVH_rect' ,area_SVH_rect)

Shading_VH=(((c_SVH_tri*area_SVH_tri)+(c_SVH_rect*area_SVH_rect))//(area_SVH_tri+area_SVH_rect))
print(Shading_VH)

##----------------------------------Defuzzification-----------------------------##
#Defuzzification of Heating
output_XX_heating = (
    (Heating_VH*Rule_1_heatingVeryHigh)+
    (Heating_VH*Rule_2_heatingVeryHigh)+
    (Heating_H*Rule_3_heatingHigh)+
    (Heating_H*Rule_4_heatingHigh)+
    (Heating_H*Rule_5_heatingHigh)+
    (Heating_H*Rule_6_heatingHigh)+
    (Heating_H*Rule_7_heatingHigh)+
    (Heating_H*Rule_8_heatingHigh)+
    (Heating_M*Rule_9_heatingMedium)+
    (Heating_M*Rule_10_heatingMedium)+
    (Heating_M*Rule_11_heatingMedium)+
    (Heating_M*Rule_12_heatingMedium)+
    (Heating_M*Rule_13_heatingMedium)+
    (Heating_M*Rule_14_heatingMedium)+
    (Heating_L*Rule_15_heatingLow)+
    (Heating_L*Rule_16_heatingLow)+
    (Heating_L*Rule_17_heatingLow)+
    (Heating_L*Rule_18_heatingLow)+
    (Heating_L*Rule_19_heatingLow)+
    (Heating_L*Rule_20_heatingLow)+
    (Heating_VL*Rule_21_heatingVeryLow)+
    (Heating_VL*Rule_22_heatingVeryLow)+
    (Heating_VL*Rule_23_heatingVeryLow)+
    (Heating_VL*Rule_24_heatingVeryLow)+
    (Heating_VL*Rule_25_heatingVeryLow))
output_YY_heating = Rule_1_heatingVeryHigh + Rule_2_heatingVeryHigh + Rule_3_heatingHigh + Rule_4_heatingHigh + Rule_5_heatingHigh + Rule_6_heatingHigh + Rule_7_heatingHigh + Rule_8_heatingHigh + Rule_9_heatingMedium + Rule_10_heatingMedium + Rule_11_heatingMedium + Rule_12_heatingMedium + Rule_13_heatingMedium + Rule_14_heatingMedium + Rule_15_heatingLow + Rule_16_heatingLow + Rule_17_heatingLow + Rule_18_heatingLow + Rule_19_heatingLow + Rule_20_heatingLow + Rule_21_heatingVeryLow + Rule_22_heatingVeryLow + Rule_23_heatingVeryLow + Rule_24_heatingVeryLow + Rule_25_heatingVeryLow
output_heating = output_XX_heating/output_YY_heating

#Defuzzification of Cooling
output_XX_cooling = (
    (Cooling_VL*Rule_26_coolingVeryLow)+
    (Cooling_VL*Rule_27_coolingVeryLow)+
    (Cooling_VL*Rule_28_coolingVeryLow)+
    (Cooling_VL*Rule_29_coolingVeryLow)+
    (Cooling_VL*Rule_30_coolingVeryLow)+
    (Cooling_L*Rule_31_coolingLow)+
    (Cooling_L*Rule_32_coolingLow)+
    (Cooling_L*Rule_33_coolingLow)+
    (Cooling_L*Rule_34_coolingLow)+
    (Cooling_L*Rule_35_coolingLow)+
    (Cooling_L*Rule_36_coolingLow)+
    (Cooling_M*Rule_37_coolingMedium)+
    (Cooling_M*Rule_38_coolingMedium)+
    (Cooling_M*Rule_39_coolingMedium)+
    (Cooling_M*Rule_40_coolingMedium)+
    (Cooling_M*Rule_41_coolingMedium)+
    (Cooling_M*Rule_42_coolingMedium)+
    (Cooling_H*Rule_43_coolingHigh)+
    (Cooling_H*Rule_44_coolingHigh)+
    (Cooling_H*Rule_45_coolingHigh)+
    (Cooling_H*Rule_46_coolingHigh)+
    (Cooling_H*Rule_47_coolingHigh)+
    (Cooling_H*Rule_48_coolingHigh)+
    (Cooling_VH*Rule_49_coolingVeryHigh)+
    (Cooling_VH*Rule_50_coolingVeryHigh)
    )
output_YY_cooling = Rule_26_coolingVeryLow + Rule_27_coolingVeryLow + Rule_28_coolingVeryLow + Rule_29_coolingVeryLow + Rule_30_coolingVeryLow + Rule_31_coolingLow + Rule_32_coolingLow + Rule_33_coolingLow + Rule_34_coolingLow + Rule_35_coolingLow + Rule_36_coolingLow + Rule_37_coolingMedium + Rule_38_coolingMedium + Rule_39_coolingMedium + Rule_40_coolingMedium + Rule_41_coolingMedium + Rule_42_coolingMedium + Rule_43_coolingHigh + Rule_44_coolingHigh + Rule_45_coolingHigh + Rule_46_coolingHigh + Rule_47_coolingHigh + Rule_48_coolingHigh + Rule_49_coolingVeryHigh + Rule_50_coolingVeryHigh
output_cooling = output_XX_cooling/output_YY_cooling

#Defuzzification of Irrigation
output_XX_irrigation = (
    (Irrigation_VH*Rule_51_irrigationVeryHigh)+
    (Irrigation_H*Rule_52_irrigationHigh)+
    (Irrigation_H*Rule_53_irrigationHigh)+
    (Irrigation_M*Rule_54_irrigationMedium)+
    (Irrigation_VL*Rule_55_irrigationVeryLow)+
    (Irrigation_VH*Rule_56_irrigationVeryHigh)+
    (Irrigation_H*Rule_57_irrigationHigh)+
    (Irrigation_M*Rule_58_irrigationMedium)+
    (Irrigation_M*Rule_59_irrigationMedium)+
    (Irrigation_L*Rule_60_irrigationLow)+
    (Irrigation_H*Rule_61_irrigationHigh)+
    (Irrigation_H*Rule_62_irrigationHigh)+
    (Irrigation_M*Rule_63_irrigationMedium)+
    (Irrigation_M*Rule_64_irrigationMedium)+
    (Irrigation_M*Rule_65_irrigationMedium)+
    (Irrigation_H*Rule_66_irrigationHigh)+
    (Irrigation_M*Rule_67_irrigationMedium)+
    (Irrigation_M*Rule_68_irrigationMedium)+
    (Irrigation_L*Rule_69_irrigationLow)+
    (Irrigation_VL*Rule_70_irrigationVeryLow)+
    (Irrigation_M*Rule_71_irrigationMedium)+
    (Irrigation_M*Rule_72_irrigationMedium)+
    (Irrigation_L*Rule_73_irrigationLow)+
    (Irrigation_L*Rule_74_irrigationLow)+
    (Irrigation_VL*Rule_75_irrigationVeryLow))
output_YY_irrigation = Rule_51_irrigationVeryHigh + Rule_52_irrigationHigh + Rule_53_irrigationHigh + Rule_54_irrigationMedium + Rule_55_irrigationVeryLow + Rule_56_irrigationVeryHigh + Rule_57_irrigationHigh + Rule_58_irrigationMedium + Rule_59_irrigationMedium + Rule_60_irrigationLow + Rule_61_irrigationHigh + Rule_62_irrigationHigh + Rule_63_irrigationMedium + Rule_64_irrigationMedium + Rule_65_irrigationMedium + Rule_66_irrigationHigh + Rule_67_irrigationMedium + Rule_68_irrigationMedium + Rule_69_irrigationLow + Rule_70_irrigationVeryLow + Rule_71_irrigationMedium + Rule_72_irrigationMedium + Rule_73_irrigationLow + Rule_74_irrigationLow + Rule_75_irrigationVeryLow
output_irrigation = output_XX_irrigation/output_YY_irrigation

#Defuzzification of Shading
output_XX_shading = (
    (Shading_VL * Rule_76_shadingVeryLow) +
    (Shading_VL * Rule_77_shadingVeryLow) +
    (Shading_L * Rule_78_shadingLow) +
    (Shading_M * Rule_79_shadingMedium) +
    (Shading_M * Rule_80_shadingMedium) +
    (Shading_VL * Rule_81_shadingVeryLow) +
    (Shading_L * Rule_82_shadingLow) +
    (Shading_L * Rule_83_shadingLow) +
    (Shading_M * Rule_84_shadingMedium) +
    (Shading_H * Rule_85_shadingHigh) +
    (Shading_VL * Rule_86_shadingVeryLow) +
    (Shading_L * Rule_87_shadingLow) +
    (Shading_M * Rule_88_shadingMedium) +
    (Shading_M * Rule_89_shadingMedium) +
    (Shading_H * Rule_90_shadingHigh) +
    (Shading_L * Rule_91_shadingLow) +
    (Shading_L * Rule_92_shadingLow) +
    (Shading_M * Rule_93_shadingMedium) +
    (Shading_H * Rule_94_shadingHigh) +
    (Shading_H * Rule_95_shadingHigh) +
    (Shading_L * Rule_96_shadingLow) +
    (Shading_M * Rule_97_shadingMedium) +
    (Shading_M * Rule_98_shadingMedium) +
    (Shading_H * Rule_99_shadingHigh) +
    (Shading_H * Rule_100_shadingVeryHigh)
)

output_YY_shading = (
    Rule_76_shadingVeryLow + Rule_77_shadingVeryLow + Rule_78_shadingLow +
    Rule_79_shadingMedium + Rule_80_shadingMedium + Rule_81_shadingVeryLow +
    Rule_82_shadingLow + Rule_83_shadingLow + Rule_84_shadingMedium +
    Rule_85_shadingHigh + Rule_86_shadingVeryLow + Rule_87_shadingLow +
    Rule_88_shadingMedium + Rule_89_shadingMedium + Rule_90_shadingHigh +
    Rule_91_shadingLow + Rule_92_shadingLow + Rule_93_shadingMedium +
    Rule_94_shadingHigh + Rule_95_shadingHigh + Rule_96_shadingLow +
    Rule_97_shadingMedium + Rule_98_shadingMedium + Rule_99_shadingHigh +
    Rule_100_shadingVeryHigh
)

output_shading = output_XX_shading / output_YY_shading
##----------------------------------Process-------------------------------------##
if st.button('Process'):
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info(f'Heating Output = {output_heating:.2f} W')
        st.write("Status : ⚡ On" if output_heating > 3.7 else "Status : ❌ Off")

        st.info(f'Irrigation Output = {output_irrigation:.2f} L')
        st.write("Status : ⚡ On" if output_irrigation > 8.9 else "Status : ❌ Off")     

    with col2:
        st.info(f'Cooling Output = {output_cooling:.2f} Micron')
        st.write("Status : ⚡ On" if output_cooling > 12 else "Status : ❌ Off")

        st.info(f'Shading Output = {output_shading:.2f} cm')
        st.write("Status : ⚡ On" if output_shading > 100 else "Status : ❌ Off")
