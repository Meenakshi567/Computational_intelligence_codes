import heapq

# ---------------- UCS GRAPH ----------------
graph = {}

# Add node
def add_node(node):
    if node not in graph:
        graph[node] = []
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

# Delete node
def delete_node(node):
    if node in graph:
        graph.pop(node)
        for n in graph:
            graph[n] = [(v, c) for v, c in graph[n] if v != node]
        print("Node deleted successfully")
    else:
        print("Node not found")

# Display graph
def display_graph():
    print("\nGraph Representation:")
    for node in graph:
        print(node, "->", graph[node])

# UCS with steps and Optimal Path
def ucs(start, goal):
    visited = {} # Stores the minimum cost to reach a node
    pq = [(0, start, [])] # (cost, current_node, path_taken)
    step = 1

    print("\n--- UCS STEPS ---")

    while pq:
        cost, current, path = heapq.heappop(pq)

        # New path including the current node
        new_path = path + [current]

        print(f"\nStep {step}")
        print("Priority Queue (Cost, Node):", [(c, n) for c, n, p in pq])
        print("Current Node:", current, "| Current Cost:", cost)

        if current == goal:
            print("\nGoal node found!")
            print("Total Cost:", cost)
            print("Optimal Path:", " -> ".join(new_path))
            return

        if current not in visited or cost < visited[current]:
            visited[current] = cost
            for neighbor, edge_cost in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + edge_cost, neighbor, new_path))
                    print(f"Pushed {neighbor} to PQ with total cost {cost + edge_cost}")

        step += 1

    print("\nGoal node not reachable")

# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter number of nodes: "))
for _ in range(n):
    add_node(input("Enter node: "))

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v, cost = input("Enter edge (u v cost): ").split()
    add_edge(u, v, int(cost))

while True:
    print("\n--- MENU ---")
    print("1. Add Node")
    print("2. Delete Node")
    print("3. Display Graph")
    print("4. Uniform Cost Search with Steps")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_node(input("Enter node: "))
    elif choice == 2:
        delete_node(input("Enter node to delete: "))
    elif choice == 3:
        display_graph()
    elif choice == 4:
        start = input("Enter start node: ")
        goal = input("Enter goal node: ")
        if start in graph and goal in graph:
            ucs(start, goal)
        else:
            print("Start or goal node not present")
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")