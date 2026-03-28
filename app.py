import numpy as np
import streamlit as st
import time
import heapq
import pandas as pd

st.set_page_config(layout = 'centered')
st.title("AI MAZE SOLVER USING A* ALGORITHM")

grid_size = 10

# creating a random maze
def create_grid():
    return np.random.choice([0 , 1] , size = (grid_size , grid_size) , p = [0.7 , 0.3])

# defining the heuristic function
def heuristic(a , b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
