from typing import List, Callable

def insertion_sort(arr: List[float]) -> List[float]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(input_list: List[float], sorting_function: Callable[[List[float]], List[float]] = insertion_sort) -> List[float]:
    if len(input_list) == 0:
        return []
    
    # Find the maximum and minimum values in the list
    max_value = max(input_list)
    min_value = min(input_list)

    # Create dynamic buckets based on the range of input values
    bucket_range = (max_value - min_value) / len(input_list) if max_value != min_value else 1
    buckets_list = [[] for _ in range(len(input_list))]

    # Place elements into the corresponding buckets
    for value in input_list:
        index = int((value - min_value) / bucket_range)
        if index >= len(input_list):
            index = len(input_list) - 1
        buckets_list[index].append(value)

    # Sort each bucket and concatenate the result
    final_output = []
    for bucket in buckets_list:
        final_output.extend(sorting_function(bucket))

    return final_output

# Example Usage
if __name__ == "__main__":
    input_data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    sorted_data = bucket_sort(input_data)
    print("Sorted Output:", sorted_data)

# Unit Tests
def test_bucket_sort():
    assert bucket_sort([0.5, 0.1, 0.3, 0.2, 0.4]) == [0.1, 0.2, 0.3, 0.4, 0.5], "Test Case 1 Failed"
    assert bucket_sort([]) == [], "Test Case 2 Failed"
    assert bucket_sort([1]) == [1], "Test Case 3 Failed"
    assert bucket_sort([0.5, 0.5, 0.5]) == [0.5, 0.5, 0.5], "Test Case 4 Failed"
    assert bucket_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test Case 5 Failed"
    print("All test cases passed.")

# Uncomment the line below to run tests
# test_bucket_sort()
