import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.PNG")

with col2:
    st.title("Ihor Korniienko")

    content = """Results-driven Data Analyst with over 6 years of experience in leveraging advanced analytical 
    capabilities and providing actionable insights in fast-paced environments. Proficient in Python, with a strong 
    foundation in object-oriented programming principles to develop scalable data solutions. Expertise in 
    Databricks SQL for data modeling and querying large datasets efficiently. Adept at visualizing data trends and 
    patterns to support strategic decision-making. Excellent communication skills with a proven ability to collaborate 
    with cross-functional teams to drive business improvements....
    """
    st.info(content)

content2 = """Here are some of the apps I have developed using Python. Don't hesitate to reach out!"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")