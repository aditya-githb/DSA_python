def selection(arr):
	num = len(arr)
	for i in range(num-1):
		small_pos = i
		for j in range(i+1,num):
			if(arr[j]<arr[small_pos]):
				small_pos = j
		arr[i],arr[small_pos] = arr[small_pos],arr[i]




arr=[2,4,62,23,7,23,12]
print("Array before sort: ", arr)

selection(arr)
print("Array after sort: ", arr)
