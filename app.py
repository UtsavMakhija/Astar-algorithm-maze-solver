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
def astar(grid , start , end , placeholder , speed):
    open_list = []
    heapq.heappush(open_list , (0 , start))

    came_from = {}
    g_cost = {start : 0}
    visited = set()

    while open_list:
        _ , current = heapq.heappop(open_list)
        visited.add(current)

        #updating the visualisation
        display = np.copy(grid)
        for (i , j) in visited:
            display[i][j] = 2
            display[start] = 3
            display[end] = 4

            placeholder.dataframe(color_grid(display))

            time.sleep(speed)

            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]

                    display[current] = 5
                    placeholder.dataframe(color_grid(display))
                    time.sleep(speed)
                return path[::-1] , visited
            
            for dx , dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                neighbour = (current[0]+dx , current[1]+dy)

                if 0 <= neighbour[0] < grid_size and 0 <= neighbour[1] < grid_size:
                    if grid[neighbour[0]][neighbour[1]] == 1:
                        continue
                    new_cost = g_cost[current] + 1

                    if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                        g_cost[neighbour] = new_cost
                        f_cost = new_cost + heuristic(neighbour , end)
                        heapq.heappush(open_list , (f_cost , neighbour))
                        came_from[neighbour] = current

    return [] , visited
