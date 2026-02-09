import heapq

# using max Heap

def kth_smallest_Max(arr, k):
    max_heap = []
    for num in arr:
        heapq.heappush(max_heap, -num)  # ---------O(k)
        if len(max_heap) > k:
            heapq.heappop(max_heap) # -----------------O(Log k)
        print(max_heap)

    value = - heapq.heappop(max_heap)

    return value # -------------------------overall   O(k)+O((N−k)logk)= O(Nlogk)


#Using min_Heap

def kth_smallest_Min(arr, k):
    heapq.heapify(arr) # ------------------------------ Convert to min heap is O(N)
    for _ in range(k-1):
        heapq.heappop(arr) # --------------Pop k elements from the heap (each pop takes O(log N)) → O(k log N)
    return heapq.heappop(arr) # =------------------------------ otal Complexity: O(N)+O(klogN)=  O(N+klogN)

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"The {k}rd smallest element using Max Heap is: {kth_smallest_Max(arr, k)}")

print(f"The {k}rd smallest element using Min Heap is: {kth_smallest_Min(arr, k)}")