# BFS, IDS, metrics
# Gneral purpose seatch library
# doesn't know about wolves or goats
# only knows how to do BFS(breadth-first seatch), IDS(iterative deepening seatch)

# inputs(what states, actions,goal are)
# outputs: solution path, stats ( nodes generated, expanded, depth, cost, ect)



# Breaadth-First Tree Seatch (BFS) Algortithm

# Understand this and be able to draw it
# S0 or N 
# S = State ( config of your enviroemnt)
# N = node in the graph or tree( node has state, action to get there, refrence to partent node)
# Build tuple (state, action(to reach that state), parent node) Or just use a class (do the class makes it easier and mroe readable)


# Using graph
# Use an explored set data structure

# Build
# Action method
# transition method

# Use graph for assignment

# make into class(state, action, parent node)




from collections import deque
import domains.WFC as WFC


start = WFC.start_state
goal = WFC.goal_state

def bfs():

        # --- metrics ---
    nodes_expanded = 0               # times we pop a state from frontier and expand it
    nodes_generated = 0              # successors we generate & enqueue
    max_frontier_size = 0

    # init.                
    frontier = deque([start])   #quese of STATES
    visisted = {start}          # set of STATES
    parent = {start: None}      # backpointer: state -> parent state
    parent_action = {start: None}  # how we got to this state

    max_frontier_size = max(max_frontier_size, len(frontier))

    while frontier:          #Frontier is not empty
        state = frontier.popleft()          #pop first node off frontier and this becomes a state!
        nodes_expanded += 1


        if state == goal:                    #test if its the goal and break
            path_states = []                #reconstuct the path of states and actions   
            path_actions = []
            cur = state
            while cur is not None:
                path_states.append(cur)
                path_actions.append(parent_action[cur])
                cur = parent[cur]
            path_states.reverse()
            path_actions = path_actions[::-1][1:]      #drop the first none
        
            solution_depth = len(path_states) - 1
            solution_cost = solution_depth  # unit cost per step



            
            metrics = {
                "Nodes generated": nodes_generated,
                "Nodes expanded": nodes_expanded,
                "Maximum frontier size": max_frontier_size,
                "Solution depth": solution_depth,
                "Solution cost": solution_cost,
                "Visited states": len(visisted),
            }
            return (path_states, path_actions, metrics)
                                   

        for action in WFC.actions(state):             #list all possible actions

            s_prime = WFC.transition(state,action)          #shows what the new state would be if that action was taken
            if WFC.valid(s_prime) and s_prime not in visisted:         #if state is new
                visisted.add(s_prime)             # add state to visted
                parent[s_prime] = state            #add the path of the parent
                parent_action[s_prime] = action    
                frontier.append(s_prime)          #add action to the frontier
                nodes_generated += 1

            if len(frontier) > max_frontier_size:
                max_frontier_size = len(frontier)



    # no solution
    metrics = {
        "Nodes generated": nodes_generated,
        "Nodes expanded": nodes_expanded,
        "Maximum frontier size": max_frontier_size,
        "Solution depth": None,
        "Solution cost": None,
        "Visited states": len(visisted),
    }
    return (None, None, metrics)