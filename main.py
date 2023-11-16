import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
df_day = pd.read_csv('dataset/day.csv')
df_hour = pd.read_csv('dataset/hour.csv')

# Drop unnecessary columns
df_day.drop(['dteday','instant','season','yr','mnth','weekday','workingday','weathersit','temp','atemp','hum', 'windspeed', 'casual', 'registered'], axis=1, inplace=True)
df_hour.drop(['instant','dteday','season','yr','mnth','hr','holiday','weekday','workingday','temp','atemp','hum','windspeed','casual','registered'], axis=1, inplace=True)

# Sidebar
st.sidebar.title("Proyek Analisis Data - Hour.csv dan Day.csv")
st.sidebar.write("Nama: Moh. Abied Rabbani")
st.sidebar.write("Email: abiedrabbani90@gmail.com")
st.sidebar.write("Id Dicoding: Moh. Abied Rabbani")

# Data Wrangling
st.title("Data Wrangling")

# Show DataFrames
st.header("Dataframe Hari")
st.write(df_day)

st.header("Dataframe Jam")
st.write(df_hour)

# Exploratory Data Analysis (EDA)
st.title("Exploratory Data Analysis (EDA)")

# Jumlah Penyewaan Sepeda pada Hari Libur dan Hari Kerja
st.header("Jumlah Penyewaan Sepeda pada Hari Libur dan Hari Kerja")
rentals_per_day_type = df_day.groupby('holiday')['cnt'].sum()
st.bar_chart(rentals_per_day_type)

# Korelasi antara Weathersit dan Jumlah Penyewaan Sepeda
st.header("Korelasi antara Weathersit dan Jumlah Penyewaan Sepeda")
corr_numerical = df_hour.corr('pearson')[['weathersit','cnt']].sort_values(by='weathersit', ascending=False)

# Menampilkan heatmap dengan pyplot
plt.figure(figsize=(8, 5))
sns.heatmap(corr_numerical, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot()

# Conclusion
st.title("Conclusion")
st.write("- Jumlah penyewaan sepeda pada hari kerja lebih banyak dari pada hari libur.")
st.write("- Hasil korelasi menunjukkan adanya hubungan yang signifikan antara kondisi cuaca dan jumlah sepeda yang disewa.")
