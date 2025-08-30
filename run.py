#argparse entry point

# reads your command=line arguments (--domain wfx --algo bfs)
# loads the right domain 
# calls the right algortith from seatch_core.py
# Prints out rsults



import search_core

def pretty_print_solution(path_states, path_actions):
    if path_states is None:
        print("No solution found.")
        return

    print("Solution path (state -> action):")
    for i, s in enumerate(path_states):
        if i < len(path_actions):
            print(f"  {i:02d}: {s}  --{path_actions[i]}-->")
        else:
            print(f"  {i:02d}: {s}")
    print()

def pretty_print_metrics(metrics):
    print("=== Run Metrics ===")
    for k, v in metrics.items():
        print(f"{k}: {v}")

def main():
    # Run BFS
    path_states, path_actions, metrics = search_core.bfs()

    # --- Print header ---
    print("=== Breadth-First Search (BFS) Results ===\n")

    # Print solution and metrics
    pretty_print_solution(path_states, path_actions)
    pretty_print_metrics(metrics)

if __name__ == "__main__":
    main()
