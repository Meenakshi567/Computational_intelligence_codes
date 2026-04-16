# ---------------- DFS GRAPH ----------------
graph = {}

def add_node(node):
    if node not in graph:
        graph[node] = []
        print("Node added successfully")
    else:
        print("Node already exists")

def add_edge(u, v):
    if u in graph and v in graph:
        graph[u].append(v)
        graph[v].append(u)
        print("Edge added successfully")
    else:
        print("Invalid nodes")

def delete_node(node):
    if node in graph:
        graph.pop(node)
        for n in graph:
            if node in graph[n]:
                graph[n].remove(node)
        print("Node deleted successfully")
    else:
        print("Node not found")

def display_graph():
    print("\nGraph Representation:")
    for node in graph:
        print(node, "->", graph[node])

def dfs(start, goal):
    visited = set()
    stack = [start]
    traversal_order = [] # To store the path taken
    step = 1

    print("\n--- DFS STEPS ---")

    while stack:
        current = stack.pop()

        if current not in visited:
            print(f"\nStep {step}")
            print("Stack:", stack + [current]) # Show stack before pop for clarity
            print("Visited:", visited)
            print("Current Node:", current)

            visited.add(current)
            traversal_order.append(current)

            if current == goal:
                print("\nGoal node found!")
                print("DFS Traversal Order:", " -> ".join(traversal_order))
                return

            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    print(f"Pushed {neighbor} to stack")
            step += 1

    print("\nGoal node not reachable")
    print("DFS Traversal Order:", " -> ".join(traversal_order))

# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter number of nodes: "))
for _ in range(n):
    add_node(input("Enter node: "))

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v = input("Enter edge (u v): ").split()
    add_edge(u, v)

while True:
    print("\n--- MENU ---")
    print("1. Add Node")
    print("2. Delete Node")
    print("3. Display Graph")
    print("4. DFS Traversal with Steps")
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
            dfs(start, goal)
        else:
            print("Start or goal node not present")
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")