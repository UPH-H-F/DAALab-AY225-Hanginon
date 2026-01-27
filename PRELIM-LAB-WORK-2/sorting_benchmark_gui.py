import random
import time
import tkinter as tk
from tkinter import ttk, messagebox


# -------------------------------
# Sorting Algorithms
# -------------------------------

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# -------------------------------
# Utility Functions
# -------------------------------

def generate_dataset(size):
    return [random.randint(0, size * 10) for _ in range(size)]


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# -------------------------------
# GUI Logic
# -------------------------------

def run_sort():
    algorithm = algorithm_var.get()
    size_input = size_entry.get()

    try:
        size = int(size_input)
        if size <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Dataset size must be a positive integer.")
        return

    data = generate_dataset(size)
    data_copy = data.copy()

    if algorithm == "Bubble Sort":
        sort_function = bubble_sort
    elif algorithm == "Insertion Sort":
        sort_function = insertion_sort
    elif algorithm == "Merge Sort":
        sort_function = merge_sort
    else:
        messagebox.showerror("Error", "Please select an algorithm.")
        return

    start_time = time.perf_counter()
    sort_function(data_copy)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    verification = "SUCCESS" if is_sorted(data_copy) else "FAILED"

    result_text.set(
        f"Algorithm: {algorithm}\n"
        f"Dataset Size: {size}\n"
        f"Execution Time: {elapsed_time:.6f} seconds\n"
        f"Verification: {verification}"
    )


# -------------------------------
# GUI Setup
# -------------------------------

root = tk.Tk()
root.title("Sorting Algorithm Benchmark")
root.geometry("420x320")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

title_label = ttk.Label(
    main_frame,
    text="Comparative Analysis of Sorting Algorithms",
    font=("Segoe UI", 11, "bold"),
    anchor="center"
)
title_label.pack(pady=(0, 15))

algorithm_var = tk.StringVar()
algorithm_dropdown = ttk.Combobox(
    main_frame,
    textvariable=algorithm_var,
    state="readonly",
    values=["Bubble Sort", "Insertion Sort", "Merge Sort"]
)
algorithm_dropdown.pack(fill="x")
algorithm_dropdown.set("Bubble Sort")

size_label = ttk.Label(main_frame, text="Dataset Size:")
size_label.pack(pady=(15, 5))

size_entry = ttk.Entry(main_frame)
size_entry.pack(fill="x")
size_entry.insert(0, "10000")

run_button = ttk.Button(main_frame, text="Run Benchmark", command=run_sort)
run_button.pack(pady=15)

result_text = tk.StringVar()
result_label = ttk.Label(
    main_frame,
    textvariable=result_text,
    justify="left",
    wraplength=380
)
result_label.pack(pady=10)

root.mainloop()
