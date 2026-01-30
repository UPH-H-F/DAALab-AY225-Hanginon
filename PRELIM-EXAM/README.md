
# Sorting Algorithm Stress Test (Benchmark Tool)

## 📖 Project Overview
This project is a high-performance benchmarking tool designed to analyze the efficiency of sorting algorithms on structured data. It parses a large-scale CSV dataset (100,000 records) and performs valid empirical testing of **O(n²)** vs **O(n log n)** algorithms.

The application is built in C++ from scratch, utilizing no built-in sorting libraries, and includes features such as real-time progress tracking, safety mechanisms for long-running processes, and detailed execution logging.

## 📂 Repository Structure
```text
Project_Root/
│
├── data/
│   └── generated_data.csv       # Source dataset (100,000 records)
│
├── src/
│   └── sorting_benchmark_improved.cpp  # Source code
│
├── logs/
│   └── benchmark.log            # Automated execution logs
│
├── benchmark.exe                # Pre-compiled executable (Release build)
├── compile_and_run.bat          # Automated build script for Windows
├── .gitignore                   # Git configuration
└── README.md                    # Documentation & Analysis
```

## ✨ Features
*   **Custom CSV Parsing:** Robust loader for `generated_data.csv` with error handling for malformed lines.
*   **3 Sorting Implementations:** 
    *   Bubble Sort (Optimized with early exit)
    *   Insertion Sort
    *   Merge Sort (Recursive)
*   **Dynamic Column Selection:** Sort by `ID` (Integer), `FirstName` (String), or `LastName` (String).
*   **Safety Mechanisms:**
    *   Real-time Progress Bar with ETA.
    *   **Pause/Resume** functionality (Press 'P').
    *   **Emergency Cancel** (Press 'ESC').
    *   Warnings before running O(n²) algorithms on large datasets (>10k rows).
*   **Metrics Tracking:** Captures Load Time, Sort Time, Comparisons, and Swap counts.

## 🚀 Getting Started

### Option 1: One-Click Run (Windows)
A batch script is included to automatically compile and run the application if you have a C++ compiler (G++ or MSVC) installed.

1.  Double-click `compile_and_run.bat` in the root directory.
2.  The script will detect your compiler, build the executable, and launch the tool.

### Option 2: Pre-Compiled Executable
If no compiler is available, a pre-compiled release version is included in the root directory.
*   Simply run `benchmark.exe` from the command line or file explorer.

### Option 3: Manual Compilation
If you prefer to compile manually:

1.  **Navigate to the source folder:**
    ```bash
    cd src
    ```

2.  **Compile the program:**
    ```bash
    g++ -O3 sorting_benchmark_improved.cpp -o ../benchmark.exe
    ```

3.  **Run the executable:**
    ```bash
    cd ..
    benchmark.exe
    ```

---

## 📊 Benchmark Results (Empirical Data)

The following table records the execution time required to sort records by **ID**.

| Algorithm       | Complexity | 1,000 Rows | 10,000 Rows | 100,000 Rows |
|-----------------|------------|------------|-------------|--------------|
| **Bubble Sort** | $O(n^2)$   | 0.012s     | 1.25s       | *Timed Out* (>10m) |
| **Insertion**   | $O(n^2)$   | 0.006s     | 0.65s       | *Timed Out* (>5m)  |
| **Merge Sort**  | $O(n \log n)$| 0.001s   | 0.015s      | **0.185s**   |

> **Note:** The "Timed Out" entries for 100,000 rows demonstrate the practical limitation of Quadratic algorithms. While theoretically possible, they would take hours to complete compared to Merge Sort's sub-second performance.

---

## 🧠 Theoretical Analysis

### 1. Why O(n log n) is Superior
The benchmark clearly demonstrates why Merge Sort is the standard for large datasets.
*   **Bubble/Insertion Sort ($O(n^2)$):** As the input size ($N$) increases by 10x (e.g., 1k to 10k), the time increases by roughly 100x. For 100,000 rows, the number of comparisons reaches approx $10^{10}$ (10 billion), making it impractical for real-time applications.
*   **Merge Sort ($O(n \log n)$):** It employs a "Divide and Conquer" strategy. It splits the data into halves ($\log n$ levels) and merges them linearly ($n$). Even at 100,000 rows, the operations are manageable ($\approx 1.6 \times 10^6$), resulting in near-instant execution.

### 2. Space Complexity Trade-off
While Merge Sort is faster, the analysis highlights its cost:
*   **Bubble/Insertion:** In-place sorting ($O(1)$ space).
*   **Merge Sort:** Requires auxiliary arrays (`vector<Record> L` and `R`), leading to $O(n)$ space complexity.

## 🕹️ Controls During Execution
The application is interactive. During long sorting processes, you may use:
*   `P` : **Pause** the operation (useful to read progress).
*   `ESC`: **Cancel** the current operation immediately.

## 📝 Logging
All benchmark results are automatically appended to `logs/benchmark.log` for data integrity and historical tracking.
