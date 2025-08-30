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
import domains.wfc as wfc


def bfs(start, goal):

        # --- metrics ---
    nodes_expanded = 0               # times we pop a state from frontier and expand it
    nodes_generated = 0              # successors we generate & enqueue
    max_frontier_size = 0

    # init.                
    frontier = deque([start])   #quese of STATES
    visited = {start}          # set of STATES
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
                "Visited states": len(visited),
            }
            return (path_states, path_actions, metrics)
                                   

        for action in wfc.actions(state):             #list all possible actions

            s_prime = wfc.transition(state,action)          #shows what the new state would be if that action was taken
            if wfc.valid(s_prime) and s_prime not in visited:         #if state is new
                visited.add(s_prime)             # add state to visted
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
        "Visited states": len(visited),
    }
    return (None, None, metrics)



def ids(start, goal, max_depth=10):        #How do you know what to set the depth to??

    # cumulative metrics across all depth limits
    nodes_expanded = 0
    nodes_generated = 0
    max_stack_size_overall = 0

    def dls(state, limit, path_states, path_actions, stats):

        stats["nodes_expanded"] += 1

        # goal test
        if state == goal:
            return True

        if limit == 0:
            return False  # cutoff

        # expand successors
        for action in wfc.actions(state):
            s_prime = wfc.transition(state, action)
            if wfc.valid(s_prime) and s_prime not in path_states:
                stats["nodes_generated"] += 1

                # take step
                path_states.append(s_prime)
                path_actions.append(action)

                # update "frontier" size for DFS (recursion stack depth)
                if len(path_states) > stats["max_stack_size"]:
                    stats["max_stack_size"] = len(path_states)

                found = dls(s_prime, limit - 1, path_states, path_actions, stats)
                if found:
                    return True

                # backtrack
                path_states.pop()
                path_actions.pop()

        return False

    # iterative deepening loop
    for depth_limit in range(0, max_depth + 1):
        # per-iteration stats (then we add to cumulative)
        stats = {
            "nodes_expanded": 0,
            "nodes_generated": 0,
            "max_stack_size": 1,  # start node on stack
        }

        path_states = [start]
        path_actions = []

        found = dls(start, depth_limit, path_states, path_actions, stats)

        # accumulate metrics
        nodes_expanded += stats["nodes_expanded"]
        nodes_generated += stats["nodes_generated"]
        max_stack_size_overall = max(max_stack_size_overall, stats["max_stack_size"])

        if found:
            solution_depth = len(path_states) - 1
            solution_cost = solution_depth  # unit step cost
            metrics = {
                "Nodes generated": nodes_generated,
                "Nodes expanded": nodes_expanded,
                "Maximum frontier size": max_stack_size_overall,  # for DFS, stack depth
                "Solution depth": solution_depth,
                "Solution cost": solution_cost,
            }
            return (path_states, path_actions, metrics)

    # no solution within max_depth
    metrics = {
        "Nodes generated": nodes_generated,
        "Nodes expanded": nodes_expanded,
        "Maximum frontier size": max_stack_size_overall,
        "Solution depth": None,
        "Solution cost": None,
    }
    return (None, None, metrics)


    
