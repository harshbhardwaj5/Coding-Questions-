# O(n) solution in Python3 for finding
# maximum sum of a subarray of size k


def maxSum(arr, n, k):

	# k must be greater
	if (n < k):
	
		print("Invalid")
		return -1
	
	res = 0
	for i in range(k):
		res += arr[i]

	# Compute sums of remaining windows by
	# removing first element of previous
	# window and adding last element of
	# current window.
	curr_sum = res
	for i in range(k, n):
	
		curr_sum += arr[i] - arr[i-k]
		res = max(res, curr_sum)

	return res


arr = [1,2,3,4,5]
k = 3
n = len(arr)
print(maxSum(arr, n, k))


