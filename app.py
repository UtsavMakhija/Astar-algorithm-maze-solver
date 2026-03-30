import streamlit as st
import numpy as np
import heapq
import time

st.set_page_config(layout="centered")
st.title("AI Maze Solver with A* Algorithm")

grid_size = 20
speed = 0.05

#creating maze
def create_grid():
    return np.random.choice([0,1], size=(grid_size, grid_size), p=[0.7,0.3])

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

#colours
def color_grid(grid, cell_size=20):
    color_map = {
        0: [255, 255, 255],  # empty
        1: [0, 0, 0],       # wall
        2: [173, 216, 230],   # explored
        3: [0, 255, 0],     # start
        4: [255, 0, 0],       # end
        5: [255, 255, 0]     # path
    }

    h, w = grid.shape
    image = np.zeros((h * cell_size, w * cell_size, 3), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            color = color_map[grid[i, j]]
            image[i*cell_size:(i+1)*cell_size,
                  j*cell_size:(j+1)*cell_size] = color

    return image

#A*
def astar(grid, start, end, placeholder):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)
        visited.add(current)

        # Visualization
        display = np.copy(grid)

        for (i,j) in visited:
            display[i][j] = 2

        display[start] = 3
        display[end] = 4

        placeholder.image(color_grid(display), width=500)
        time.sleep(speed)

        # Goal reached
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]

                display[current] = 5
                placeholder.image(color_grid(display), width=500)
                time.sleep(speed)

            return path[::-1], visited

        # Explore neighbors
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)

            if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return [], visited

#session state
if "grid" not in st.session_state:
    st.session_state.grid = create_grid()

grid = st.session_state.grid

start = (0,0)
end = (grid_size-1, grid_size-1)

#buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Generate New Maze"):
        st.session_state.grid = create_grid()

with col2:
    solve = st.button("Solve Maze")

#original maze
st.write("Original Maze")

initial_display = np.copy(grid)
initial_display[start] = 3
initial_display[end] = 4

st.image(color_grid(initial_display), width=500)

#animation
st.write("Solving Process")
placeholder = st.empty()

#solving the maze
if solve:
    path, visited = astar(grid.tolist(), start, end, placeholder)

    if path:
        st.success("Path Found!")
    else:
        st.error("No Path Found!")

    st.write("STATS")
    st.write(f"Path Length: {len(path)}")
    st.write(f"Nodes Explored: {len(visited)}")

#legend
st.write("""
### Legend:
White = Empty Cell  
Black = Wall  
Blue = Explored Nodes  
Green = Start Node  
Red = End Node  
Yellow = Final Optimal Path  
""")
