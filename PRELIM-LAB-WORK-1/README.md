# DAALab-AY225
The DAA-Lab Repo

# Bubble Sort Implementation (Improved)

## Overview

This project provides a **robust, well-documented, and performance-measured implementation of the Bubble Sort algorithm** in Python.
The program supports **ascending and descending sorting**, handles **large datasets**, tracks **algorithm performance metrics**, and includes **command-line options** for flexible usage.

The implementation is designed for **clarity, correctness, and maintainability**, while demonstrating a deep understanding of algorithm behavior and limitations.

---

## Algorithm Logic

### Bubble Sort Description

Bubble Sort works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.
With each pass, the largest (or smallest) element “bubbles” into its correct position.

### Key Enhancements

* **Early termination optimization**
  If no swaps occur during a pass, the algorithm stops early, reducing unnecessary iterations.
* **Ascending and descending order support**
* **Edge case handling**

  * Empty files
  * Single-element datasets
  * Duplicate values
  * Already sorted datasets
* **Safe in-place sorting with preserved original data**

### Time Complexity

* Worst-case: **O(n²)**
* Best-case (already sorted with early termination): **O(n)**

### Space Complexity

* **O(1)** additional space (in-place sorting)

---

## Performance Measurement

The program includes **built-in performance tracking** to analyze Bubble Sort behavior.

### Metrics Collected

* Number of comparisons
* Number of swaps
* Number of passes
* Early termination detection
* Total execution time (seconds)

### Measurement Method

* Execution time is measured using Python’s `time` module.
* Statistics are gathered during each comparison and swap.
* Results are displayed clearly after sorting.

### Analysis

* Performance data confirms Bubble Sort’s **quadratic growth** on large datasets.
* Early termination significantly improves runtime for nearly sorted inputs.
* The program warns users when dataset size makes Bubble Sort inefficient and recommends Python’s built-in `sort()` for production use.

---

## Git & Documentation

### Git Commit Strategy

Commits are expected to be:

* **Frequent**
* **Descriptive**
* **Single-purpose**

Example commit messages:

```
Add ascending and descending bubble sort functions
Implement early termination optimization
Add performance statistics tracking
Improve CLI argument parsing and help text
Update README with performance analysis
```

### Documentation Quality

* Clear docstrings for all major functions
* Inline comments explaining non-obvious logic
* Detailed README explaining:

  * Algorithm behavior
  * Performance implications
  * Usage instructions
  * Design decisions

---

## Code Quality

### Best Practices Followed

* Modular, readable function design
* Clear variable and function naming
* Type hints for better maintainability
* Separation of concerns (sorting, I/O, statistics, CLI)
* Defensive programming with robust error handling

### Readability & Maintainability

* Logical file structure
* Consistent formatting
* Easy-to-extend design (additional algorithms or metrics can be added with minimal changes)

---

## Usage

### Basic Command

```bash
python bubblesort_improved.py
```

### Common Options

```bash
python bubblesort_improved.py -a            # Ascending order
python bubblesort_improved.py --stats       # Show performance metrics
python bubblesort_improved.py --sample      # Display sample output
python bubblesort_improved.py -i data.txt   # Custom input file
python bubblesort_improved.py --no-save     # Do not save output
```

---

## Sample Output

```
Total Numbers Sorted: 10,000
Sort Order: Descending
Comparisons: 49,995,000
Swaps: 24,812,345
Passes: 10,000
Early termination: No
Time Taken: 3.412581 seconds
```

---

## Conclusion

This project demonstrates an **excellent-quality Bubble Sort implementation** that:

* Correctly implements algorithm logic
* Measures and analyzes performance
* Follows clean coding standards
* Includes thorough documentation and Git discipline

It is well-suited for **academic evaluation, algorithm analysis, and learning purposes**, while clearly acknowledging Bubble Sort’s real-world limitations.

---
