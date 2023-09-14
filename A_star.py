g = 0
def print_board(elements):
    for i in range(0, 9, 3):
        for e in elements[i:i+3]:
            if e != -1:
                print(e, end=" ")
            else:
                print("_", end=" ")
        print()
    print()

def solvable(start):
    count = 0
    for i in range(len(start)):
        for j in range(i+1, len(start)):
            if start[i] > start[j] and start[j] != -1:
                count += 1
    return count % 2 == 0

def heuristic(start, goal):
    total_distance = 0
    for i in range(len(start)):
        if start[i] != -1:
            distance = abs(goal.index(start[i]) - i)
            total_distance += distance

    return total_distance

def movetile(start,goal):
    emptyat= start.index(-1)
    row = emptyat//3
    col = emptyat%3
    t1,t2,t3,t4 = start[:],start[:],start[:],start[:]
    f1,f2,f3,f4 = 100,100,100,100

    if col -1 >=0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col+1<3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 <3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row-1>=0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2,f3,f4)

    if f1==min_heuristic:
        moveleft(start, emptyat)
    elif f2==min_heuristic:
        moveright(start, emptyat)
    elif f3==min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)

def solve_eight(start, goal):
    global g
    g+=1
    movetile(start,goal)
    print_board(start)
    f = heuristic(start,goal)
    if start == goal:
        print("Solved in {} moves".format(g))
        return

    solve_eight(start,goal)

def moveleft(start,position):
    start[position],start[position-1]= start[position-1],start[position]

def moveright(start,position):
    start[position],start[position+1]= start[position+1],start[position]

def moveup(start,position):
    start[position],start[position-3]= start[position-3],start[position]

def movedown(start,position):
    start[position],start[position+3]= start[position+3],start[position]

def main():
    start = []
    goal = []
    print("Enter the start state (Enter -1 for empty):")
    for i in range(9):
        start.append(int(input()))

    print("Enter the goal state (Enter -1 for empty):")
    for i in range(9):
        goal.append(int(input()))

    print_board(start)

    if solvable(start):
        solve_eight(start, goal)
    else:
        print("Not possible to solve")

if __name__ == '__main__':
    main()
    
-------------------------------------------------------------------------------------------    
  
output :
Enter the start state (Enter -1 for empty):
1
4
-1
3
2
5
7
6
8
Enter the goal state (Enter -1 for empty):
1
4
5
3
2
8
7
6
-1
1 4 _ 
3 2 5 
7 6 8 

1 4 5 
3 2 _ 
7 6 8 

1 4 5 
3 2 8 
7 6 _ 

Solved in 2 moves