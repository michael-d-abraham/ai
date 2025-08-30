import search_core

def pretty_print_solution(path_states, path_actions):
    if path_states is None:
        print("No solution found.\n")
        return
    print("Path:")
    for i, s in enumerate(path_states):
        if i < len(path_actions):
            print(f"  {i+1}) {path_actions[i]}   {s} -> {path_states[i+1]}")
        else:
            print(f"  {i+1}) {s}")
    print()

def print_summary(domain, algo, metrics):
    print(f"Domain: {domain} | Algorithm: {algo}")
    print(f"Solution cost: {metrics['Solution cost']} | Depth: {metrics['Solution depth']}")
    print(f"Nodes generated: {metrics['Nodes generated']} | Nodes expanded: {metrics['Nodes expanded']} | Max frontier: {metrics['Maximum frontier size']}\n")

def run_one_case(case_title, start_state, goal_state):
    domain = "WGC"
    print(f"=== {case_title} ===\n")

    # BFS
    bs, ba, bm = search_core.bfs(start_state, goal_state)
    print_summary(domain, "BFS", bm)
    pretty_print_solution(bs, ba)

    # IDS
    is_, ia, im = search_core.ids(start_state, goal_state)
    print_summary(domain, "IDS", im)
    pretty_print_solution(is_, ia)

def main():
    # Case 1: Normal
    run_one_case("Case 1 (Normal)", (0,0,0,0), (1,1,1,1))

    # Case 2: variation (goat already on right)
    run_one_case("Case 2 (goat starts on right)", (1,1,0,0), (1,1,1,1))



if __name__ == "__main__":
    main()
