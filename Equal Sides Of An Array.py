def find_even_index(arr):
    
    for i in range(len(arr)):
        x = 0
        y = 0
        for q in arr[:i]:
            x += q
        for z in arr[i+1:]:
            y += z
        if x == y:
            return i
    return -1
