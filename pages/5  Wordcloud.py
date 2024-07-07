import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords


df=pd.read_csv("datasets/streamlitdb/df_forwordcloud.csv")

#to have always the same airlines in the streamlit app:
df.drop(df[df['AIRLINENAME'] == "Qatar Airways"].index, inplace=True)
df.drop(df[df['AIRLINENAME'] == "China Southern Airlines"].index, inplace=True)

st.set_page_config(
     page_title="FJ WordCloud",
     page_icon=":small_airplane:",
     layout="centered",
     initial_sidebar_state="auto",
     
 )

# Create a Streamlit app with the following title
st.markdown("# *A picture is worth 1,000 words*")

# New Page 
st.subheader("What do travellers think about each airline?" ":thinking_face:")

# Allow the user to select an airline
airlines = df["AIRLINENAME"].unique()
selected_airline = st.selectbox("Please select an Airline", airlines)

# Filter the DataFrame based on the selected character
planes = df[df["AIRLINENAME"] == selected_airline]["TEXT"]

# Concatenate all lines
texto = " ".join(planes)

# Create a WordCloud with a specific image and stopwords
mask = "images/plane.png"
mask = np.array(Image.open("images/plane.png"))

nltk.download('stopwords')
stopwrd = nltk.corpus.stopwords.words('english')
new_stopwords = ['and','I','A','And','So','arnt','This','When','It','many','Many','so','cant', 'again','Yes','yes','No','no','These','these','customer service','service', 'customer', 'review', 'customer review', 'airline', 'airlines', 'flight', 'seat', 'seats',  'seat','customer review', '$', '#', '£','check-in', 'check in', 'fly','customer service','service', 'customer', 'review', 'airline', 'flight', 'seat', 'experience', 'BA', 'Delta', 'United', 'China', 'American', 'Frontier', 'British', 'Qatar', 'Spirit', 'Air Lines', 'Airlines', 'Airways','customer service','service', 'customer', 'review', 'airline', 'flight']
airline_stopwords = set(df['AIRLINENAME'].values)
country_stopwords = set(df['ORIGINCOUNTRY'].values)
airline_stopwords=list(airline_stopwords)
country_stopwords=list(country_stopwords)

stopwrd.extend(new_stopwords)
stopwrd.extend(airline_stopwords)
stopwrd=stopwrd+airline_stopwords+country_stopwords


wordcloud = WordCloud(stopwords=stopwrd, background_color="black", max_words=80, mask=mask, colormap="Dark2", contour_width=1, contour_color="white").generate(texto)

# Display the WordCloud
st.image(wordcloud.to_array(), use_column_width=True)