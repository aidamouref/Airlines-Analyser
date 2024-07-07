import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs


st.set_page_config(
     page_title="Flight Judge",
     page_icon=":airplane:",
     layout="centered",
     initial_sidebar_state="auto",
 )


st.title("The Flight Judge")
st.header("Is this flight worth it?")

cover = Image.open("images/front.jpg")
st.image(cover, use_column_width=True)

st.text ('''Ready for those amazing holidays you were planning and waiting so much? 
Maybe waiting for an important business trip that will boost your career? 
Planning a fairy tale getaway with your couple for a magic proposal?
         
Sounds amazing, right? so...you get at the airport with a big smile on yourface. 
Great! and suddenly...a rude member of the staff gets in your way and the smile 
in your face vanishes. 

Ok, that's fine! just an awkard moment. Smile again on your face :) 
You get in the plane, sit on your designed seat. The flight departs and problems 
just start:seat is just a piece of torture, cabin staff are unattentive and you 
would rather starve before eating that food.
         
When looking for a flight most people look for prices or times. 
However, many other items are key to get a wonderful or a nigthmare flight e
xperience. 
         
So, what if you could get that information in advance? 
would you rather save a few coins if you would know that your flight will ruin 
your day?
         
In 'Flight Judge' we believe in altruism and social justice. Hence we have 
designed a place were travellers can express their opinions about their flight 
experiences. 
         
You can also rate your onw flight and help future travellers! 
         
            *** LET US MAKE YOUR TRIP A NICE EXPERIENCE TO REMEMBER ***''') 




         

