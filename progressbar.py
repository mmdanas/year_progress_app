import streamlit as st
from streamlit_autorefresh import st_autorefresh
from PIL import Image
import time 
from datetime import datetime

st_autorefresh(interval=60 * 60 * 1000, key="dataframerefresh")
st.title("Who else is waiting for the New Year? :grimacing:")
st.markdown("![Alt Text](https://c.tenor.com/rec5dlPBK2cAAAAd/mr-bean-waiting.gif)")
url = 'https://c.tenor.com/rec5dlPBK2cAAAAd/mr-bean-waiting.gif'
##image = Image.open('img.gif')
#st.image(image)
def progress_calc():
    total =365
    day_of_year = datetime.now().timetuple().tm_yday
    floating_diff = round(float((day_of_year/total) * 100),2)
    diff = int((day_of_year/total) * 100)
    msg = "We have completed {} % of this year".format(floating_diff)
    st.header(msg)
    my_bar = st.progress(diff)
    emoji = ":runner: :runner: :runner::runner::runner::runner::runner::dancer::dancer::dancer::dancer:"
    st.header(emoji)
def balloons():
    st.balloons()
def snow():
    st.snow()


progress_calc() 
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.markdown("Don't ask me why I made this app?  :smirk_cat: !!! Because, why not? Yeah, it doesn't do much but in my defense, I was bored :see_no_evil: ")
if st.button('Click Here!!!'):
    balloons()
    st.markdown("Wasn't that fun?? :satisfied:")
    st.markdown("Now click the next button!! Go!!! :wink:")
if st.button("Go on, Click it!!"):
    snow()
        
    st.markdown("Did you enjoy?? :stuck_out_tongue_winking_eye: ")
    st.markdown("That's all for now!!! Okay!!! Byeee :wave:")
    
st.empty()
st.info('This page has a feature to auto refresh every hour! Progress bar keeps getting updated as we move forward')

st.button("Re-run")