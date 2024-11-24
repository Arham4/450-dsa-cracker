def threeWayPartition(self, array, a, b):
    partition_1 = []
    partition_2 = []
    partition_3 = []
    for num in array:
        if num < a:
            partition_1.append(num)
        elif num >= a and num <= b:
            partition_2.append(num)
        elif num > b:
            partition_3.append(num)
    array[:] = partition_1 + partition_2 + partition_3
    return array
