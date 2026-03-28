# AI Maze Solver using A* Algorithm
## Project Overview
The AI Maze Solver is an interactive application that demonstrates how Artificial Intelligence can be used to find the shortest path in a maze. It uses the A* (A-Star) Search Algorithm, one of the most efficient pathfinding techniques, to navigate from a start point to an end point while avoiding obstacles.
The project also includes real-time visualization, allowing users to see how the algorithm explores the maze and reaches the solution step-by-step.
________________________________________
## Objectives
•	Demonstrate the practical use of AI search algorithms \
•	Visualize how pathfinding works in real time \
•	Build an interactive and beginner-friendly AI project \
•	Apply theoretical concepts to a real-world inspired problem
________________________________________
## How This Project Uses AI
1.	Uses Artificial Intelligence search techniques to make decisions at each step
2.	The algorithm evaluates multiple possible paths and chooses the most optimal one
3.	It mimics intelligent behavior by: \
o	Exploring efficiently instead of randomly \
o	Using heuristics to “predict” the best route
4.	Falls under the domain of: \
o	Search Algorithms in AI \
o	Pathfinding & Optimization Problems
________________________________________
## Algorithm Used: A* (A-Star)
### What is A*?
A* is a heuristic-based search algorithm that finds the shortest path between two points. \
Core Idea : 
It calculates a score for each node:
f(n) = g(n) + h(n) \
•	g(n) → Cost from start to current node \
•	h(n) → Estimated cost to reach goal (heuristic)
### Why A* is Used
•	Faster than uninformed search algorithms \
•	Guarantees shortest path (if heuristic is admissible) \
•	Widely used in real-world applications
________________________________________
## Features
1.  Random maze generation
2.  Color-coded visualization: \
o	White → Empty path \
o	Black → Walls \
o	Blue → Explored nodes \
o	Green → Start point \
o	Red → End point \
o	Yellow → Final path
3.  Step-by-step animation
4.  Adjustable grid size
5.  Adjustable animation speed
6.  Displays: \
o	Path length \
o	Nodes explored
7.  Regenerate maze functionality
________________________________________
## Technologies Used
•	Python → Core programming language \
•	Streamlit → UI and visualization \
•	NumPy → Grid and matrix operations \
•	Heapq → Priority queue implementation for A*
________________________________________
## How It Works (Step-by-Step)
1.	A random maze grid is generated 
2.	Start and end points are defined 
3.	A* algorithm begins exploring nodes 
4.	Each step: \
o	Evaluates neighbors \
o	Updates costs \
o	Chooses the best path
5.	Explored nodes are visualized in real-time 
6.	Once goal is reached: \
o	Shortest path is reconstructed \
o	Final path is displayed
________________________________________
## Real-World Applications
### Navigation Systems
•	Used in GPS apps like Google Maps
•	Finds shortest or fastest routes
### Robotics
•	Helps robots navigate obstacles in real environments
### Game Development
•	Used in NPC movement and pathfinding
### Delivery & Logistics
•	Optimizing delivery routes for efficiency
### Emergency Services
•	Finding fastest path for ambulances/fire trucks
________________________________________
## Future Enhancements
• Compare A* with other algorithms (BFS, DFS) \
• Add user-drawn maze input \
•	Convert into a playable game \
• Add performance comparison graphs \
• Diagonal movement support \
• Deploy as a web application \
• Integrate with real robot navigation systems
________________________________________
## How to Run the Project
1. Install Dependencies \
pip install streamlit numpy
2. Run the App \
streamlit run app.py
3. Open in Browser \
Automatically opens at: http://localhost:8501
________________________________________
## Key Learning Outcomes
•	Understanding of A* search algorithm \
•	Practical implementation of AI concepts \
•	Visualization of algorithm behavior \
•	Basics of building interactive Python apps
________________________________________
## Conclusion
This project successfully demonstrates how Artificial Intelligence can be applied to solve pathfinding problems efficiently. By combining theory with visualization, it provides a strong foundation for understanding more advanced AI systems used in real-world applications.
________________________________________
## Author
•	Utsav Makhija
