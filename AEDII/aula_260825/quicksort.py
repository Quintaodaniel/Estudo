def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    pivot = arr.pop()
    lower = []
    greater = []

    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)
    return quicksort(lower) + [pivot] + quicksort(greater)