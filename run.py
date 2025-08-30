import search_core

def pretty_print_solution(path_states, path_actions):
    if path_states is None:
        print("No solution found.")
        return
    print("Solution path (state -> action):")
    for i, s in enumerate(path_states):
        arrow = f"  --{path_actions[i]}-->" if i < len(path_actions) else ""
        print(f"  {i:02d}: {s}{arrow}")
    print()

def pretty_print_metrics(metrics):
    print("=== Run Metrics ===")
    for k, v in metrics.items():
        print(f"{k}: {v}")

def main():
    # BFS
    print("=== Breadth-First Search (BFS) Results ===\n")
    bs, ba, bm = search_core.bfs()
    pretty_print_solution(bs, ba)
    pretty_print_metrics(bm)
    print("\n")

    # IDS
    print("=== Iterative Deepening Search (IDS) Results ===\n")
    is_, ia, im = search_core.ids()
    pretty_print_solution(is_, ia)
    pretty_print_metrics(im)

if __name__ == "__main__":
    main()
