arr = []

num = int(input("enter the size of array: \n"))

print("enter the array elements")

for i in range(num):
    arr.append(int(input()))

for i in range (num - 1):
    for j in range (num - i - 1):
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]


print("array after bubble sort\n")
for i in range(num):
    print(arr[i],end = " ")