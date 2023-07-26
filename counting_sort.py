def countsort(arr):
  size = len(arr)
  output = [0]*size
  count=[0]*10

  for i in range(0,size):
    count[arr[i]]+=1
  for j in range(1,10):
    count[j]+=count[j-1]
  a=size-1
  while a>0:
    output[count[arr[a]-1]]=arr[a]
    count[arr[a]]-=1
    a-=1
  for k in range(0,size):
    arr[k]=output[k]
  

list = [5,3,4,2,6,9,1]
print(list)
countsort(list)
print(list)
