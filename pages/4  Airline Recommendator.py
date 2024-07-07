import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import codecs
from sklearn.neighbors import NearestNeighbors

df=pd.read_csv("datasets/streamlitdb/cleandf.csv")
df_forrecomm = pd.read_csv("datasets/streamlitdb/df_forrecomm.csv")

st.set_page_config(
     page_title="FJ Recommendator",
     page_icon=":small_airplane:",
     layout="centered",
     initial_sidebar_state="auto",
     
 )
grouped_ailines=df.groupby(['AIRLINENAME'])['REVIEW'].count().reset_index()


grouped_ailines = grouped_ailines[grouped_ailines['REVIEW'] > 2000] 
grouped_ailines.sort_values('REVIEW', ascending=False)



num=df[["AIRLINENAME", "ENTERTAINMENTRATING", "FOODRATING", "GROUNDSERVICERATING", "OVERALLSCORE", "SEATCOMFORTRATING", "SERVICERATING", "VALUERATING", "WIFIRATING"]]
num=num.drop_duplicates(subset=['AIRLINENAME'])

num.drop('AIRLINENAME', axis=1, inplace=True)
num.reset_index(drop=True, inplace=True)


def best_airline_recommender(user_input):
    
    test_data = grouped_ailines[grouped_ailines['AIRLINENAME'] == user_input]
    
    num_input = num.loc[test_data.index].values
               
# Calculate similarities (n_neighbors=6 for 5 recommendations) - NOT CONFUSE NN to KNN
    search = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(num) # kd_tree, brute, auto...
    _ , queried_indices = search.kneighbors(num_input) #kneighbors returns two arrays: one containing the distances from the query point to each of its nearest neighbors (which we discard here, hence _), and the other containing the indices of the nearest neighbors
                   
# Top 5 recommendations
    df_rec = df_forrecomm.loc[queried_indices[0][1:]] # This line uses the indices of the nearest neighbors obtained in the previous step to select the corresponding rows from the DataFrame data, excluding the first index (which corresponds to the input beer itself). The selected rows are stored in df_rec.
    df_rec = df_rec.sort_values(by=['OVERALLSCORE'], ascending=False)
    df_rec.index = range(1, 6)
    df_rec = df_rec[['AIRLINE','OVERALLSCORE']]
    df_rec['OVERALLSCORE']=df_rec['OVERALLSCORE'].round(1)
    st.subheader("Get recommendations for similar airles")
    return df_rec



user_input = st.selectbox('Select an airline:', grouped_ailines['AIRLINENAME'].unique())

if st.button("Recommend Airlines"):
    recommendations = best_airline_recommender(user_input)
    
    if recommendations is not None:
        st.write("You can try out these airlines:")
        st.table(recommendations)