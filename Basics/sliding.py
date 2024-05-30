def sliding_window_moving_average(arr, window_size):
    n = len(arr)
    if window_size > n:
        return []

    # Compute the initial window sum
    window_sum = sum(arr[:window_size])
    result = [window_sum / window_size]

    # Slide the window over the array
    for i in range(window_size, n):
        # Update the window sum by adding the next element and removing the first element of the previous window
        window_sum += arr[i] - arr[i - window_size]
        result.append(window_sum / window_size)

    return result

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 3
print(sliding_window_moving_average(arr, window_size))