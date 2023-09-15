import sys
import numpy as np
import time  # Import the time module for time measurement
import psutil

from astar import AStar
from bfs import BFS
from board import Board
from dfs import DFS
from iddfs import IDDFS
#from Board_15 import Board


####################################################


###############################################################


def main():
    p = Board(np.array(eval(sys.argv[2])))
    alg = sys.argv[1]
    
    if alg == 'bfs':
        s = BFS(p)
    elif alg == 'ids':
        s = IDDFS(p)
    elif alg == 'dfs':
        s = DFS(p)
    elif alg == 'ast':
        s = AStar(p)
    else:
        print("Invalid input, continuing through A*")
        s = AStar(p)
    print("here")
    s.solve()
    print("here_2")

    file = open(f'{alg}_output1.txt', 'w')

    file.write('path_to_goal: ' + str(s.path) + '\n')
    file.write('cost_of_path: ' + str(len(s.path)) + '\n')
    file.write('nodes_expanded: ' + str(s.nodes_expanded) + '\n')
    file.write('nodes_explored: ' + str(len(s.explored_nodes)) + '\n')
    file.write('search_depth: ' + str(s.solution.depth) + '\n')
    file.write('max_search_depth: ' + str(s.max_depth) + '\n')
   
    # Platform-independent code for measuring running time using the time module

    process = psutil.Process()
    start_memory = process.memory_info().rss

    start_time = time.process_time()
    print("here_3")
    s.solve()
    print("here_4")
    end_time = time.process_time()
    running_time = end_time - start_time

    end_memory = process.memory_info().rss
    memory_consumption = (end_memory - start_memory) / (1024 ** 2)  # Convert to MB


    file.write('running_time: ' + str(running_time) + '\n')
    file.write('memory_consumption: ' + str(memory_consumption) + ' MB\n')

    # You can use platform-independent methods to get memory usage if needed

    file.close()

if __name__ == "__main__":
    main()
