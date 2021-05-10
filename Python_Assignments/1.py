def skyline(arr):
    m=0
    newarr=[]
    new=[]
    max=arr[0]
    for x in range(len(arr)):
        if arr[x]>max:
            max=arr[x]
            m=x
    for x in range(len(arr)):
        if 
    for x in range(len(arr)):
        if arr[0]==max:
            new.append(arr[x])
            print(new)
            return new
    
    for x in range (m):
        if arr[x]<arr[x+1]:
            newarr.append(arr[x+1])
            print(newarr)
            return newarr

    
skyline([3,5,3,8,1])