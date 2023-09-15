# 8-puzzle and 15-puzzle solve 
puzzle solver using BFS, DFS, IDDFS algorithm

*It is assumed that goal state is:*
    
     0 1 2
     3 4 5
     6 7 8
     
#### Usage
You can run `main.py` with the name of algorithm - which is `bfs`, or `dfs`, or `ids` for iterative deepening dfs - as the first argument and initial state as the second one:

```
python main.py ids [1,0,2,3,4,5,6,7,8]
python main.py ids [1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
```

Solution and details will be saved to ```{alg-name}_output.txt```.
