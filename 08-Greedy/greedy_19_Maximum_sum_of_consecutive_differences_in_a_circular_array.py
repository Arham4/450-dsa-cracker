def maxSum(self,arr):
    arr = sorted(arr)
    left_pointer = 0
    right_pointer = len(arr) - 1
    max_sum = 0
    while left_pointer < right_pointer:
        max_sum += abs(arr[left_pointer] - arr[right_pointer])
        left_pointer += 1
        right_pointer -= 1
    return max_sum * 2
