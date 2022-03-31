def list_partitions(n):
    
    thisset = set()
    arr = [0]*n
    def partitions(n, arr, index):
        #print(n, arr, index)
        if (n == 0):
            arr_copy = arr[:]
            arr_copy.sort(reverse=True)
            t = tuple(arr_copy)
            if (t in thisset):
                return
            thisset.add(t)
            return
        if (n < 0):
            return
        for i in range(n+1):
            if n - i - 1 < 0:
                break
            arr[index] = i+1
            partitions(n - i - 1, arr, index+1)
            arr[index] = 0
    partitions(n, arr, 0)
    return thisset

def composition_count(n):
    return len(list_partitions(n))
