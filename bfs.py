from collections import deque
class BFS:
    """start 0 0, goal 3 2"""

    def __init__(self):
        self.queue = deque()
        self.path = []
        self.adj = [
            [1, 2, 3],        # 0 connected to 1,2,3
            [0, 4, 5],        # 1 connected to 0,4,5
            [0, 5, 6],        # 2 connected to 0,5,6
            [0, 6],           # 3 connected to 0,6
            [1, 7],           # 4 connected to 1,7
            [1, 2, 7, 8],     # 5 connected to 1,2,7,8
            [2, 3, 8],        # 6 connected to 2,3,8
            [4, 5, 9],        # 7 connected to 4,5,9
            [5, 6, 9],        # 8 connected to 5,6,9
            [7, 8]            # 9 connected to 7,8
            ]

    def begin_algorithm(self):
        size = len(self.adj)
        if size <= 0:
            print("List is empty")
            return
        
        self.visited = [False] * size
        curr = 0

        """initalize the first node"""
        self.queue.append(curr)

        while len(self.queue) > 0:
            curr = self.queue.popleft()
            self.path.append(curr)
            self.visited[curr] = True

            for node in self.adj[curr]:
                if self.visited[node] == False:
                    self.queue.append(node)
                    self.visited[node] = True
                    
    def print_path(self):
        print("BFS Traversal: ", end=" ")
        for node in self.path:
            if node == self.path[len(self.path) - 1]:
                print(node)
            else:
                print(node, end=" - > ")
        
    













        
        




    

