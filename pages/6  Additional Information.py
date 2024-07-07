import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import codecs
from IPython.core.display import display, HTML

st.set_page_config(
     page_title="FJ Recommendator",
     page_icon=":small_airplane:",
     layout="wide",
     initial_sidebar_state="expanded",
     
 )


#add a video about first experience in airports
st.title("Additional Information")
st.subheader("Tips for first-time travellers")

video_url = "https://www.youtube.com/watch?v=z7I1xHcUsQA"
st.video(video_url)



