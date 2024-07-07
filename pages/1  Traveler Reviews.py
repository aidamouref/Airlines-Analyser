import streamlit as st
import pandas as pd



# Load the sentiment data
sentimentdf = pd.read_csv("datasets/streamlitdb/df_forwordcloud.csv")
#to have always the same airlines in the streamlit app:
sentimentdf.drop(sentimentdf[sentimentdf['AIRLINENAME'] == "Qatar Airways"].index, inplace=True)
sentimentdf.drop(sentimentdf[sentimentdf['AIRLINENAME'] == "China Southern Airlines"].index, inplace=True)

st.set_page_config(
     page_title="FJ Reviews",
     page_icon=":small_airplane:",
     layout="centered",
     initial_sidebar_state="auto",
     
 )

# Create a Streamlit app with the following title

# New Page 
st.header("Flight Reviews")
st.markdown("_Let us show you the good ...and the not so good_")

airlines = sentimentdf["AIRLINENAME"].unique()
with st.sidebar:
    selection = st.radio(':airplane: Please select an Airline:', airlines)
    
    
# Filter dataframe based on positive and negative sentiment analysis and get a positive and negative review by airline
neg_sentiment_df = sentimentdf[sentimentdf['SENTIMENT'] == -1]
pos_sentiment_df = sentimentdf[sentimentdf['SENTIMENT'] == 1]

col1, col2 = st.columns(2)

# Function to get a random review

def get_random_review(df, airline, sentiment):
    airline_df = df[df['AIRLINENAME'] == airline]
    if len(airline_df) > 0:
        random_sentence = airline_df['TITLE'].sample(n=1).iloc[0].lower()
    else:
        random_sentence = f"No {sentiment} reviews"
    return random_sentence


# Display information for each airline
def display_reviews(airline):
    with col1:
        
        countpos = pos_sentiment_df[pos_sentiment_df['AIRLINENAME'] == airline].shape[0]
        countneg = neg_sentiment_df[neg_sentiment_df['AIRLINENAME'] == airline].shape[0]
        
            # Get random positive review
        random_sentences_pos = get_random_review(pos_sentiment_df, airline, "positive")
        st.subheader(":smiling_face_with_3_hearts:")
        st.write(random_sentences_pos)
        
        # Get random negative review
        
        random_sentences_neg = get_random_review(neg_sentiment_df, airline, "negative")
        st.subheader(":face_with_spiral_eyes:")
        st.write(random_sentences_neg)

    with col2:
        st. markdown(f"#### {airline} Summary")
        st.write(f"**Number of positive reviews:**  _{countpos}_")
        st.write(f"**Number of negative reviews:**  _{countneg}_")
        st.write ("**Veredict:**")
        if countpos>countneg:
            st.image("images/goodflight.gif")
        elif countpos==countneg:
            st.image("images/mediumflight.gif")
        else:
            st.image("images/badflight.gif")

# Add a button to get a new set of random reviews
if st.button("**Get a sample review**"):
    display_reviews(selection)
    



