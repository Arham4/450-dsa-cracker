def sortedMatrix(self,N,Mat):
    sorted_nums = sorted([n for y in Mat for n in y])
    sorted_matrix = []
    for i in range(N):
        sorted_matrix.append([])
        for y in range(len(Mat[i])):
            sorted_matrix[i].append(sorted_nums[i * N + y])
    return sorted_matrix
