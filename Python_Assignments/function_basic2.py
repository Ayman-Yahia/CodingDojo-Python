#1.
def countdown(num):
    count=[]
    for x in range(num,-1,-1):
        count.append(x)
    return count
#2.
def PrintandReturn(lis):
    print(lis[0])
    return(lis[1])
#3.
def FirstPlusLength(N):
    print(N[len(N)-1]+N[0])
#4.
def valuesgreaterthansecond(list):
    if len(list)<=2:
        return False
    newlist=[]
    N=list[2]
    count=0
    for x in range(0,len(list)):
        if list[x]>=N:
            count+=1
            newlist.append(list[x])
    print(count)
    return newlist
#5.
def ThisLength(a,b):
    lis=[]
    for x in range (1,a+1):
        lis.append(b)
    return lis



