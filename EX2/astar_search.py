import heapq

# ---------------- A* GRAPH ----------------
graph = {}
heuristic = {}

# Add node with heuristic value
def add_node(node, h):
    if node not in graph:
        graph[node] = []
        heuristic[node] = h
        print("Node added successfully")
    else:
        print("Node already exists")

# Add weighted edge
def add_edge(u, v, cost):
    if u in graph and v in graph:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
        print("Edge added successfully")
    else:
        print("Invalid nodes")

# Display graph
def display_graph():
    print("\nGraph Representation:")
    for node in graph:
        print(node, "->", graph[node], "| h =", heuristic[node])

# A* Search with steps
def astar(start, goal):
    open_list = [(heuristic[start], 0, start)]  # (f, g, node)
    closed_set = set()
    step = 1

    print("\n--- A* SEARCH STEPS ---")

    while open_list:
        print(f"\nStep {step}")
        print("Open List:", open_list)
        print("Closed Set:", closed_set)

        f, g, current = heapq.heappop(open_list)
        print(f"Current Node: {current}, g={g}, h={heuristic[current]}, f={f}")

        if current == goal:
            print("\nGoal node found!")
            print("Total Cost:", g)
            return

        closed_set.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_set:
                continue

            new_g = g + cost
            new_f = new_g + heuristic[neighbor]

            heapq.heappush(open_list, (new_f, new_g, neighbor))
            print(f"Added {neighbor} with g={new_g}, h={heuristic[neighbor]}, f={new_f}")

        step += 1

    print("\nGoal node not reachable")

# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    h = int(input(f"Enter heuristic value for {node}: "))
    add_node(node, h)

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v, cost = input("Enter edge (u v cost): ").split()
    add_edge(u, v, int(cost))

display_graph()

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

if start in graph and goal in graph:
    astar(start, goal)
else:
    print("Start or goal node not present")