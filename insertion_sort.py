def insertion(arr):
  for i in range (1,len(arr)):
    j=i
    while arr[j-1]>arr[j] and j>0:
      arr[j-1],arr[j]=arr[j],arr[j-1]
      j=j-1

list = [5,3,4,2,6,9,1]
print(list)
insertion(list)
print(list)
