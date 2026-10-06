arr=[1,2,3,"hello","good","bad"]
for i in range(len(arr)-1,-1,-1):
    if type(arr[i])==str:
        arr.pop(i)
print(arr)