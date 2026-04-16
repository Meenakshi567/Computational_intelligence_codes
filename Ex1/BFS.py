from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        self.bfs_traversal_order = []

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v):
        if u in self.graph and v in self.graph:
            if v not in self.graph[u]:
                self.graph[u].append(v)
                self.graph[v].append(u)

    def delete_node(self, node):
        if node in self.graph:
            self.graph.pop(node)
            for n in self.graph:
                if node in self.graph[n]:
                    self.graph[n].remove(node)
            print(f"Node {node} deleted.")
        else:
            print("Node not found.")

    def display_graph(self):
        print("\nGraph Representation:")
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    # Breadth First Search (Modified to print steps and store the order)
    def bfs(self, start, goal=None):
        self.bfs_traversal_order = []
        visited = set()
        queue = deque([(start, [start])]) # Stores (current_node, path_list)

        visited.add(start)
        print(f"\n--- Starting BFS from {start} ---")
        step_counter = 1

        while queue:
            current_node, path = queue.popleft()
            self.bfs_traversal_order.append(current_node) # Add to the order list

            print(f"\nStep {step_counter}: Dequeued Node: {current_node}")
            print(f"  Current Path: {path}")
            print(f"  Queue State (next to visit): {[item[0] for item in queue]}")
            print(f"  Visited Set: {visited}")

            if goal is not None and current_node == goal:
                print(f"\n{'='*40}")
                print(f"GOAL FOUND: Node {goal} reached in {step_counter} steps!")
                print(f"Final Path: {path}")
                self.print_bfs_order()
                print(f"{'='*40}")
                return path

            print(f"  Exploring neighbors of {current_node}: {self.graph.get(current_node, [])}")
            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    print(f"    -> Adding unvisited neighbor {neighbor} to queue and visited set.")
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))

            step_counter += 1

        # This block runs if the loop finishes without finding the goal
        if goal is not None:
            print(f"\nGoal node {goal} not reachable.")

        self.print_bfs_order()
        return None

    def print_bfs_order(self):
        """Helper function to print the stored BFS traversal order."""
        if self.bfs_traversal_order:
            print("\n" + "="*40)
            print(f"BFS Traversal Order: {' -> '.join(self.bfs_traversal_order)}")
            print("="*40)
        else:
            print("\nNo BFS traversal conducted yet.")

# --- Main Program Execution (Menu system remains the same) ---

g = Graph()
print("--- Initial Graph Setup ---")
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    g.add_node(node)

e = int(input("Enter number of edges: "))
for _ in range(e):
    u, v = input("Enter edge (u v): ").split()
    g.add_edge(u, v)
print("--- Setup Complete ---")

while True:
    print("\n--- MENU ---")
    print("1. Add Node")
    print("2. Delete Node")
    print("3. Display Graph")
    print("4. Add Edge")
    print("5. BFS Traversal (with order and path tracking)")
    print("6. Print Last BFS Order Only")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        node = input("Enter node to add: ")
        g.add_node(node)

    elif choice == 2:
        node = input("Enter node to delete: ")
        g.delete_node(node)

    elif choice == 3:
        g.display_graph()

    elif choice == 4:
        x,y = input("Enter edge (u v):").split()
        g.add_edge(x,y)

    elif choice == 5:
        start = input("Enter start node: ")
        goal = input("Enter goal node (leave blank to traverse all): ")
        if start in g.graph:
            g.bfs(start, goal if goal else None)
        else:
            print("Start node not present in the graph.")

    elif choice == 6:
        g.print_bfs_order()

    elif choice == 7:
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")