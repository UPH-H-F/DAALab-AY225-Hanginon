import time
import os
import sys
import argparse
from typing import List, Tuple, Optional

# ============================================
# CONFIGURATION OPTIONS
# ============================================
DEFAULT_INPUT_FILE = 'dataset.txt'
DEFAULT_OUTPUT_FILE = 'sorted_output.txt'
PROGRESS_THRESHOLD = 1000  # Show progress bar for lists larger than this
SAMPLE_SIZE = 20  # Number of items to show in sample preview


def bubble_sort_descending(arr: List[int], show_stats: bool = False) -> Tuple[List[int], dict]:
    """
    Sorts a list in descending order using Bubble Sort.
    
    Args:
        arr: List of integers to sort
        show_stats: If True, track comparison and swap statistics
        
    Returns:
        Tuple of (sorted list, statistics dictionary)
    """
    n = len(arr)
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'passes': 0,
        'early_termination': False
    }
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        stats['passes'] += 1
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            stats['comparisons'] += 1
            
            # Change '>' to '<' for Descending Order
            if arr[j] < arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                stats['swaps'] += 1
        
        # Show progress for large datasets
        if n > PROGRESS_THRESHOLD and (i + 1) % max(1, n // 20) == 0:
            progress = ((i + 1) / n) * 100
            print(f"\rProgress: {progress:.1f}% complete...", end='', flush=True)
                
        # If no swaps occurred, the array is already sorted
        if not swapped:
            stats['early_termination'] = True
            stats['passes_saved'] = n - i - 1
            break
    
    if n > PROGRESS_THRESHOLD:
        print()  # New line after progress bar
        
    return arr, stats


def bubble_sort_ascending(arr: List[int], show_stats: bool = False) -> Tuple[List[int], dict]:
    """
    Sorts a list in ascending order using Bubble Sort.
    
    Args:
        arr: List of integers to sort
        show_stats: If True, track comparison and swap statistics
        
    Returns:
        Tuple of (sorted list, statistics dictionary)
    """
    n = len(arr)
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'passes': 0,
        'early_termination': False
    }
    
    for i in range(n):
        swapped = False
        stats['passes'] += 1
        
        for j in range(0, n - i - 1):
            stats['comparisons'] += 1
            
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                stats['swaps'] += 1
        
        # Show progress for large datasets
        if n > PROGRESS_THRESHOLD and (i + 1) % max(1, n // 20) == 0:
            progress = ((i + 1) / n) * 100
            print(f"\rProgress: {progress:.1f}% complete...", end='', flush=True)
                
        if not swapped:
            stats['early_termination'] = True
            stats['passes_saved'] = n - i - 1
            break
    
    if n > PROGRESS_THRESHOLD:
        print()
        
    return arr, stats


def calculate_statistics(numbers: List[int]) -> dict:
    """Calculate basic statistics about the dataset."""
    if not numbers:
        return {}
    
    return {
        'min': min(numbers),
        'max': max(numbers),
        'range': max(numbers) - min(numbers),
        'unique_count': len(set(numbers)),
        'duplicate_count': len(numbers) - len(set(numbers))
    }


def format_number(num: int) -> str:
    """Format number with commas for readability."""
    return f"{num:,}"


def display_sample(numbers: List[int], sample_size: int = SAMPLE_SIZE) -> None:
    """Display a sample of the sorted numbers instead of all."""
    n = len(numbers)
    if n <= sample_size * 2:
        print(numbers)
    else:
        print(f"First {sample_size} items: {numbers[:sample_size]}")
        print(f"...")
        print(f"Last {sample_size} items: {numbers[-sample_size:]}")


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Sort numbers from a file using Bubble Sort algorithm.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python bubblesort_improved.py                    # Use default dataset.txt
  python bubblesort_improved.py -i mydata.txt      # Custom input file
  python bubblesort_improved.py -a                 # Sort in ascending order
  python bubblesort_improved.py --stats            # Show algorithm statistics
  python bubblesort_improved.py --sample           # Show sample instead of full output
        """
    )
    
    parser.add_argument('-i', '--input', 
                        default=DEFAULT_INPUT_FILE,
                        help=f'Input file name (default: {DEFAULT_INPUT_FILE})')
    
    parser.add_argument('-o', '--output',
                        default=DEFAULT_OUTPUT_FILE,
                        help=f'Output file name (default: {DEFAULT_OUTPUT_FILE})')
    
    parser.add_argument('-a', '--ascending',
                        action='store_true',
                        help='Sort in ascending order (default: descending)')
    
    parser.add_argument('--stats',
                        action='store_true',
                        help='Show algorithm statistics (comparisons, swaps, etc.)')
    
    parser.add_argument('--sample',
                        action='store_true',
                        help='Show sample of results instead of full output')
    
    parser.add_argument('--no-save',
                        action='store_true',
                        help='Do not save results to output file')
    
    parser.add_argument('--remove-duplicates',
                        action='store_true',
                        help='Remove duplicate numbers before sorting')
    
    return parser.parse_args()


def main():
    """
    Main function that orchestrates the file reading, sorting, and output display.
    """
    # Parse command-line arguments
    args = parse_arguments()
    
    # Get the directory where this script is currently located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Build full file paths
    input_path = os.path.join(script_dir, args.input)
    output_path = os.path.join(script_dir, args.output)
    
    # Check if file exists
    if not os.path.exists(input_path):
        print(f"Error: '{input_path}' not found.")
        print(f"Please make sure '{args.input}' is in the same folder as this script.")
        print(f"Current directory: {script_dir}")
        return 1

    print(f"Reading {args.input}...")
    
    try:
        # Read all lines from the file
        with open(input_path, 'r') as f:
            # Convert each non-empty line to an integer
            numbers = [int(line.strip()) for line in f if line.strip()]
        
        if not numbers:
            print("Error: The file is empty or contains no valid numbers.")
            return 1
            
        print(f"Successfully loaded {format_number(len(numbers))} numbers.")
        
        # Calculate pre-sort statistics
        pre_stats = calculate_statistics(numbers)
        
        if pre_stats:
            print(f"Range: {format_number(pre_stats['min'])} to {format_number(pre_stats['max'])}")
            if pre_stats['duplicate_count'] > 0:
                print(f"Duplicates found: {format_number(pre_stats['duplicate_count'])}")
        
        # Remove duplicates if requested
        if args.remove_duplicates and pre_stats['duplicate_count'] > 0:
            original_count = len(numbers)
            numbers = list(set(numbers))
            print(f"Removed {format_number(original_count - len(numbers))} duplicates.")
        
        # Create a copy to preserve original
        numbers_to_sort = numbers.copy()
        
        sort_order = "ascending" if args.ascending else "descending"
        print(f"Sorting in {sort_order} order... (This may take a moment for large datasets)")
        
        # Measure time and sort
        start_time = time.time()
        
        if args.ascending:
            sorted_numbers, algo_stats = bubble_sort_ascending(numbers_to_sort, show_stats=args.stats)
        else:
            sorted_numbers, algo_stats = bubble_sort_descending(numbers_to_sort, show_stats=args.stats)
        
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Display Results
        print("\n" + "=" * 50)
        print("RESULTS")
        print("=" * 50)
        print(f"Total Numbers Sorted: {format_number(len(sorted_numbers))}")
        print(f"Sort Order: {sort_order.capitalize()}")
        
        # Show algorithm statistics if requested
        if args.stats:
            print("\n--- Algorithm Statistics ---")
            print(f"Comparisons: {format_number(algo_stats['comparisons'])}")
            print(f"Swaps: {format_number(algo_stats['swaps'])}")
            print(f"Passes: {format_number(algo_stats['passes'])}")
            if algo_stats['early_termination']:
                print(f"Early termination: Yes (saved {algo_stats['passes_saved']} passes)")
            else:
                print("Early termination: No")
        
        # Display sorted data
        print(f"\nSorted Data ({sort_order.capitalize()}):")
        if args.sample and len(sorted_numbers) > SAMPLE_SIZE * 2:
            display_sample(sorted_numbers, SAMPLE_SIZE)
        else:
            print(sorted_numbers)
        
        # Display time at the end for easy visibility
        print(f"\nTime Taken: {time_taken:.6f} seconds")
        
        # Show performance note for large datasets
        if len(sorted_numbers) > 10000:
            theoretical_time = (len(sorted_numbers) ** 2) / 1000000
            print(f"Note: Bubble Sort has O(n²) complexity. For {format_number(len(sorted_numbers))} items,")
            print(f"      consider using Python's built-in sort() for better performance.")
        
        # Save to file unless --no-save flag is used
        if not args.no_save:
            with open(output_path, 'w') as out_f:
                for num in sorted_numbers:
                    out_f.write(f"{num}\n")
            print(f"\nSorted results saved to: '{args.output}'")
        
        print("=" * 50)
        return 0

    except ValueError as e:
        print(f"Error: The file contains non-numeric data. Please check {args.input}.")
        print(f"Details: {e}")
        return 1
    except PermissionError:
        print(f"Error: Permission denied when accessing files.")
        print("Please check file permissions.")
        return 1
    except IOError as e:
        print(f"Error: Could not read/write files.")
        print(f"Details: {e}")
        return 1
    except MemoryError:
        print("Error: Not enough memory to process this dataset.")
        print("Try with a smaller file or use a more efficient sorting algorithm.")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
