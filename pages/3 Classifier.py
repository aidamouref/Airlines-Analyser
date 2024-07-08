import streamlit as st
import pandas as pd
import joblib


# Load the sentiment data
sentimentdf = pd.read_csv("datasets/streamlitdb/df_forwordcloud.csv")

st.set_page_config(
     page_title="FJ Reviews",
     page_icon=":small_airplane:",
     layout="centered",
     initial_sidebar_state="auto",
     
 )

df=pd.read_csv("datasets/streamlitdb/cleandf.csv")
df_forclassif = pd.read_csv("datasets/streamlitdb/df_forclassif.csv")

# Sidebar input for flight values
st.sidebar.header("Input Your Flight Values")
my_flight_values = [
    st.sidebar.slider("Entertainment", 0, 5, 3),
    st.sidebar.slider("Food", 0, 5, 3),
    st.sidebar.slider("Ground Service", 0, 5, 5),
    st.sidebar.slider("Seat Comfort", 0, 5, 5),
    st.sidebar.slider("Cabin Service", 0, 5, 5),
    st.sidebar.slider("Value for Money", 0, 5, 4),
    st.sidebar.slider("Wi-Fi", 0, 5, 2)
]

loaded_rf = joblib.load("models/random_forest_class.joblib")

data=df[["ENTERTAINMENTRATING", "FOODRATING", "GROUNDSERVICERATING", "SEATCOMFORTRATING", "SERVICERATING", "VALUERATING", "WIFIRATING"]]

# Assuming my_flight_values and X.columns are already defined
my_flight_df = pd.DataFrame(data=[my_flight_values], columns=data.columns)

# Make prediction
predicted_score = round(loaded_rf.predict(my_flight_df)[0])
st.write(f"The Overall Score of this airline is {predicted_score} according to your ratings!")

# Calculate the average overall score for each airline
df1 = df.groupby(['AIRLINENAME'])['OVERALLSCORE'].mean().reset_index()
df1.set_index('AIRLINENAME', inplace=True)

# Check if the predicted score matches any overall score in the dataset
if predicted_score in df['OVERALLSCORE'].values:
    df2=df1[df1.OVERALLSCORE==predicted_score]
    df2=df2.sort_values(by="OVERALLSCORE", ascending=False)
    st.write(df2.head())

if predicted_score<5:
    st.image("images/transilvania.gif")
elif predicted_score==5:
    st.image("images/mediumflight.gif")
else:
    st.image("images/recommend.gif")
    
