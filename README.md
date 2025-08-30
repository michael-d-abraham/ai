# AI Search Algorithms - Wolf-Goat-Cabbage Puzzle

This project implements classic search algorithms (BFS and IDS) to solve the Wolf-Goat-Cabbage river crossing puzzle.

## What It Does

The Wolf-Goat-Cabbage puzzle is a classic river crossing problem where you must transport three items across a river using a boat that can carry only you plus one item. The constraints are:
- **Wolf and Goat**: Cannot be left alone together (wolf will eat goat)
- **Goat and Cabbage**: Cannot be left alone together (goat will eat cabbage)

## How to Run

```bash
# Run both algorithms on both test cases (default)
python run.py

# Run only BFS
python run.py --algo bfs

# Run only IDS  
python run.py --algo ids


## Test Cases

- **Case 1**: Start from `(0,0,0,0)` (all left) to `(1,1,1,1)` (all right)
- **Case 2**: Start from `(1,1,0,0)` (farmer+wolf right) to `(1,1,1,1)` (all right)

## Output

For each algorithm, you'll see:
- Solution path with actions and states
- Metrics: cost, depth, nodes generated/expanded, frontier size

## Files

- `run.py` - CLI interface and test runner
- `search_core.py` - BFS and IDS implementations  
- `domains/wfc.py` - Puzzle rules and state transitions
