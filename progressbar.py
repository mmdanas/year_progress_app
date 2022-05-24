import streamlit as st
from streamlit_autorefresh import st_autorefresh
from PIL import Image
import time 
from datetime import datetime

st_autorefresh(interval=60 * 60 * 1000, key="dataframerefresh")

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
    st.title(msg)
    my_bar = st.progress(diff)

progress_calc() 
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")