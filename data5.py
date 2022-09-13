import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
# from wordcloud import WordCloud
# import plotly.express as px
# from add_data import db_execute_fetch
from sqlalchemy import create_engine

connections_path = "mysql+pymysql://root:tham1984%@localhost/Sales"
engine = create_engine(connections_path)


st.set_page_config(page_title="Day 5", layout="wide")

def loadData():
    with engine.connect() as conn:
        cleand_df = pd.read_sql_table('feutures', con=conn)
        return cleand_df


df = loadData()
st.dataframe(df[:10])