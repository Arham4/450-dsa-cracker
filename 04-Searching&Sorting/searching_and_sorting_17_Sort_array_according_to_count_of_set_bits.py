def sortBySetBitCount(self, arr, n):␍
    counts = [[] for i in range(32)]␍
    for num in arr:␍
        bits = bin(num).count("1")␍
        counts[bits].append(num)␍
    result = []␍
    for i in range(len(counts) - 1, -1, -1):␍
        result.extend(counts[i])␍
    arr[:] = result␍
    return arr
