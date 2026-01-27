from sorts import bubble_sort, insertion_sort, merge_sort
from utils import generate_data, is_sorted, time_sort


def display_menu():
    print("\nSelect Algorithm:")
    print("[1] Bubble Sort")
    print("[2] Insertion Sort")
    print("[3] Merge Sort")


def get_algorithm(choice):
    if choice == "1":
        return bubble_sort, "Bubble Sort"
    elif choice == "2":
        return insertion_sort, "Insertion Sort"
    elif choice == "3":
        return merge_sort, "Merge Sort"
    else:
        return None, None


def main():
    print("=== Sorting Algorithm Benchmark Tool ===")

    while True:
        display_menu()
        choice = input("Enter choice (1-3): ").strip()
        sort_func, name = get_algorithm(choice)

        if not sort_func:
            print("Invalid selection.")
            continue

        try:
            size = int(input("Enter dataset size (e.g., 10000): "))
            if size <= 0:
                raise ValueError
        except ValueError:
            print("Invalid dataset size.")
            continue

        data = generate_data(size)
        data_copy = data.copy()  # ensure fair timing

        sorted_data, elapsed_time = time_sort(sort_func, data_copy)

        print(f"\nAlgorithm: {name}")
        print(f"Dataset size: {size}")
        print(f"Execution time: {elapsed_time:.6f} seconds")

        if is_sorted(sorted_data):
            print("Verification: SUCCESS — Array is sorted.")
        else:
            print("Verification: FAILED — Array is NOT sorted.")

        again = input("\nRun another test? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()
