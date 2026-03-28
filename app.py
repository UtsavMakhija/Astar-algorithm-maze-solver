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
#converting grid to a coloured dataframe for better visualisation
def color_grid(grid):
    color_map = {
        0: [255, 255, 255],  # white
        1: [0, 0, 0],        # black
        2: [173, 216, 230],  # light blue
        3: [0, 255, 0],      # green
        4: [255, 0, 0],      # red
        5: [255, 255, 0]     # yellow
    }

    image = np.zeros((grid.shape[0], grid.shape[1], 3), dtype=np.uint8)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            image[i, j] = color_map[grid[i, j]]

    return image
    
#session state
if 'grid' not in st.session_state:
    st.session_state.grid = create_grid()

grid = st.session_state.grid
start = (0 , 0)
end = (grid_size - 1 , grid_size - 1)

#controls
col1 , col2 = st.columns(2)

with col1:
    if st.button("GEMERATE MAZE"):
        st.session_state.grid = create_grid()

with col2:
    solve = st.button("SOLVE MAZE")

#speed controls

speed = st.slider("ANIMATION SPEED (lower = faster)" , 0.01 , 0.2 , 0.05)

placeholder = st.empty()

placeholder.dataframe(color_grid(grid))

if solve:
    path , visited = astar(grid.tolist() , start , end , placeholder , speed)

    st.success("SUCCESS : PATH FOUND")

    st.write("### 📊 Stats")
    st.write(f"Path Length: {len(path)}")
    st.write(f"Nodes Explored: {len(visited)}")
