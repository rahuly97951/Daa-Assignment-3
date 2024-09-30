def find_max_min(arr, low, high):
    
    if low == high:
        return arr[low], arr[low]  
    
    
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[high], arr[low]  
        else:
            return arr[low], arr[high]  

    
    mid = (low + high) // 2
    
    
    max1, min1 = find_max_min(arr, low, mid)
    max2, min2 = find_max_min(arr, mid + 1, high)
    
    
    return max(max1, max2), min(min1, min2)

# Example usage
arr = [100, 3, 200, 1, 50, 90, 2]
max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
print("Maximum element is:", max_val)
print("Minimum element is:", min_val)
