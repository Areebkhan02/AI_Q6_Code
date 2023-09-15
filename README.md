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

Imp points to consider: 
1) Whoever is using this code, its important that you pay attention to the main.py file since it will be the only file that you need to interact with. In the main.py file if you want to run the code for 8 puzzle solver than uncomment the line 8 ("from board import Board") and its important that you comment out line 11 ("from Board_15 import Board"). Then run the file as mentioed above.
2) If you want to run the file for 15 puzzel solver then uncomment the line 11 ("from Board_15 import Board") and comment out line 8 ("from board import Board"). Then run the file as mentioned above
3) For the 15 puzzle solver even for less complex configurations it will take a lot of time or a gpu if you want to do it quickly. Dfs especially will take alot more time than bfs or iddfs
4) There are also invalid initial states so keep in mind that you enter a valid initial state or else BFS will throw error and DFS, IDDFS will run in loop and just heat up the system.
