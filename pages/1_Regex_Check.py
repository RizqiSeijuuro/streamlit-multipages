import re
import streamlit as st

st.set_page_config(page_title="Regex Checker", page_icon="🌍")

st.header("Regex Checker")
st.subheader("Experiment with Regex Pattern")

regex_pattern = st.text_input(label="Regex Pattern:", value="")
input = st.text_input(label="Test it!", value="")



if (regex_pattern != "") & (input != ""):
    if re.match(regex_pattern, input) is not None:
        st.success('True')
    else:
        st.error('False')