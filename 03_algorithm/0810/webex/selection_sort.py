def selection_sort(arr, N):
    for i in range(N): #N-1로도 가능
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)
    return arr
arr = [93, 3, 61, 52, 81, 6, 91]
N = len(arr)
selection_sort(arr, N)