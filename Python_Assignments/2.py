def two_sums(arr,target):
    newarr=[]
    for x in range(len(arr)):
        for i in range(1,len(arr)):
            if arr[i]+arr[x]==target:
                newarr.append(x)
                newarr.append(i)
                print(newarr)
                return newarr
two_sums([3,2,4], 6)

