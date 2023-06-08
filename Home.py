import streamlit as st

st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        )

st.write(f'# Welcome to Rizqiansyah\'s Streamlit Multipages! 👋')

st.sidebar.success("Select an apps above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    
    **👈 Select an apps from the sidebar** to see some apps
    created by RIMM Data Team!
    """
    )