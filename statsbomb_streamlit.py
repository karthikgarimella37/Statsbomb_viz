import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from statsbombpy import sb
import streamlit as st


competitions = sb.competitions()
unique_competitions = competitions.competition_id.unique()

comp_option = st.selectbox("Which Competition do you want?",
                            unique_competitions)

st.write("Competition Selected: ", competitions[competitions.competition_id == comp_option].competition_name)