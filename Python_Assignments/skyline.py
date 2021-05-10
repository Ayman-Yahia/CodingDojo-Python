def skyline(arr):
    newarr=[]
    for x in range (len(arr)):
        if arr[x]>0:
            newarr.append(arr[x])
            first=arr[x]
            y=x
            break
    max=arr[y]
    for x in range(y,len(arr)):
        if arr[x]>max:
            max=arr[x]
            m=x
    for x in range (y,m):
        if arr[x]<arr[x+1]:
            newarr.append(arr[x+1])
    print(newarr)
    return newarr
    skyline([-1,1,2,6,-1,5]