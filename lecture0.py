import sys 

class Node():
    def __init__(self, state, parent, action) -> None:
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self) -> None:
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
           #last element of the list
           node = self.frontier[-1]
           self.frontier = self.frontier[:-1]
           return node
        
class QueueFrontier(StackFrontier):
    def remove(self):
         if self.empty():
            raise Exception("empty frontier")
         else:
            #first element of the list
             node = self.frontier[0]
             self.frontier = self.frontier[1:]
             return node
         

class Maze():
    def __init__(self, filename) -> None:
        
        #read file and set height and width of the maze
        with open(filename, "r") as file:
            contents = file.read()

        # Defining start and end goal
        if contents.count("A") != 1:
            raise Exception("Maze must only have one starting point!")
        if contents.count("B") != 1:
            raise Exception("Maze must only have one ending point!")
        
        # determine height and width of maze
        contents  = contents.splitlines()
        # print(contents)
        self.height = len(contents)
        self.width = max(len(each) for each in contents) 

        #keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
        # print(self.walls)
    
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row-1, col)), 
            ("down", (row+1, col)), 
            ("right", (row, col+1)), 
            ("left", (row, col-1))
        ]
        result = []

        for action, (r, c) in candidates:
            print(action)       
            if 0 <= r < self.height and 0 <= c < self.width  and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result



m = Maze("maze1.txt")
m.neighbors((1,2))
