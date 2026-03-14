# USACO Python Practice

Collection of Python solutions written while working through USACO-style workshops. Problems are grouped by week/topic, plus an alphabetical extra practice section.

## Topics by week
- `Week 1 Simulation`: simulation fundamentals and magic trick-style problems.
- `Week 2 Big-O and Complete Search`: brute force + optimization analysis.
- `Week 3 Further Complete Search`: expanded search/DFS/BFS strategies.
- `Week 4 Sets and Maps, and Two Pointers`: hash-based lookups and sliding window techniques.
- `Week 5 Precomputation, Prefix Sums, and Queries`: prefix sums to speed up repeated queries.
- `Week 6 Practice Olympiad`: long-form multi-constraint problems.
- `Week 7 Greedy Algorithms`: greedy heuristics.
- `Week 8 Forced Decisions`: branching decisions with pruning.
- `Week 9 Wrestling with the Unknown`: puzzles and logic-style problems.
- `Week 10 Permutations and Puzzling Problems`: permutations, backtracking, and unusual constraints.
- `Week 11 Geometry`: geometry problems.
- `Week 12 Binary Search`: binary search and search-on-answer tricks.
- `Week 13 Final Practice Olympiad`: culminating problems that mix themes.

## Extra Practice
`Extra Practice/` is organized alphabetically (`A-B`, `C-D`, …) and mirrors the C++ repo structure. Each folder contains one or more problem scripts alongside supporting resources.

## Running solutions
From `Python Coding/usaco`, run any script; they typically expect custom-formatted stdin. Example:

```bash
python3 \"Week 1 Simulation/magic_trick.py\"          # uses hardcoded sample input or redirects
python3 \"Extra Practice/G-H/hps.py\" < input.txt
```

When a problem relies on file-based input, match the USACO prompt (e.g., `magic_trick.in`), then redirect it into the script.

## Notes
- Filenames generally match the problem title; inspect docstrings or comments for the exact input format.
- Feel free to copy solutions into new folders when experimenting with alternate approaches or optimizations.
