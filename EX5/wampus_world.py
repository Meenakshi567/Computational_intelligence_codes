class WumpusWorld:
    def __init__(self, size, wumpus_pos, gold_pos, pits_list):
        self.size = size
        self.agent = [0, 0]
        self.wumpus = wumpus_pos
        self.gold = gold_pos
        self.pits = pits_list
        self.score = 0
        self.has_gold = False
        self.wumpus_alive = True

    def valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def move_up(self): self.move(-1, 0)
    def move_down(self): self.move(1, 0)
    def move_left(self): self.move(0, -1)
    def move_right(self): self.move(0, 1)

    def move(self, dx, dy):
        nx, ny = self.agent[0] + dx, self.agent[1] + dy
        if not self.valid(nx, ny):
            print("Hit wall!")
            return
        self.agent = [nx, ny]
        self.score -= 1
        if self.agent in self.pits:
            print("Fell into PIT! Game Over"); self.score -= 1000; exit()
        if self.agent == self.wumpus and self.wumpus_alive:
            print("Killed by Wumpus! Game Over"); self.score -= 1000; exit()

    def grab(self):
        if self.agent == self.gold:
            print("Gold grabbed!"); self.has_gold = True; self.score += 1000
            print(f"Score : {self.score}\nHurray You won!"); exit()
        else: print("No gold here")

    def shoot(self):
        if self.agent == self.wumpus:
            print("Wumpus killed!"); self.wumpus_alive = False; self.score += 100
        else: print("Arrow missed!"); self.score -= 10

    def percepts(self):
        x, y = self.agent
        stench = breeze = glitter = False
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if self.valid(nx, ny):
                if [nx, ny] == self.wumpus and self.wumpus_alive: stench = True
                if [nx, ny] in self.pits: breeze = True
        if self.agent == self.gold and not self.has_gold: glitter = True
        print(f"\nPercepts: Stench: {stench}, Breeze: {breeze}, Glitter: {glitter}")

    def display(self):
        print("\nGRID:")
        for i in range(self.size):
            for j in range(self.size):
                pos = [i, j]
                if pos == self.agent: print("A", end=" ")
                elif pos == self.wumpus and self.wumpus_alive: print("W", end=" ")
                elif pos in self.pits: print("P", end=" ")
                elif pos == self.gold and not self.has_gold: print("G", end=" ")
                else: print(".", end=" ")
            print()
        print("Score:", self.score)

# --- SETUP PHASE ---
size = int(input("Enter grid size (e.g., 4 for 4x4): "))

print("\nInitial Empty Grid:")
for _ in range(size):
    print(". " * size)

def get_pos(prompt):
    return list(map(int, input(f"Enter {prompt} coordinates (row col): ").split()))

w_pos = get_pos("Wumpus")
g_pos = get_pos("Gold")
num_pits = int(input("Enter number of pits: "))
p_list = [get_pos(f"Pit {i+1}") for i in range(num_pits)]

world = WumpusWorld(size, w_pos, g_pos, p_list)

# --- GAME LOOP ---
while True:
    world.display()
    world.percepts()
    print("\n1.UP 2.DOWN 3.LEFT 4.RIGHT 5.Grab 6.Shoot 7.Exit")
    choice = input("Choice: ")
    if choice == "1": world.move_up()
    elif choice == "2": world.move_down()
    elif choice == "3": world.move_left()
    elif choice == "4": world.move_right()
    elif choice == "5": world.grab()
    elif choice == "6": world.shoot()
    elif choice == "7": break