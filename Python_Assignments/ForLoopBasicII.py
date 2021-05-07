#1.
def Biggle(lis):
    for x in range(0,len(lis)):
        if lis[x]>0:
            lis[x]="big"
    return lis
#2.
def CountPositives(lis):
    count=0
    for x in range(0,len(lis)):
        if lis[x]>0:
            count+=1
    lis[len(lis)-1]=count
    return lis
#3.
def SumTotal(lis):
    sum=0
    for x in range(0,len(lis)):
        sum+=lis[x]
    return sum
#4.
def avg(lis):
    sum=0
    for x in range(0,len(lis)):
        sum+=lis[x]
    avg=sum/len(lis)
    return avg
#5.
def length(lis):
    print(len(lis))
#6.
def min(lis):
    min=lis[0]
    for x in range(0,len(lis)):
        if lis[x]>min:
            min=lis[x]
    print(min)
    return min 
#7.
def max(lis):
    max=lis[0]
    for x in range(0,len(lis)):
        if lis[x]>max:
            max=lis[x]
    return max 
#8.
def UltimateAnalysis(lis):
    Analysis={'sumTotal':0,'average':0,'minimum':0,'maximum':0,'length':0}
    sumtotal = 0
    average = 0
    minimum = lis[0]
    maximum = lis[0]
    length = len(lis)
    for x in range(len(lis)):
        if lis[x] > maximum:
            maximum = lis[x]
            sumtotal += lis[x]
        elif lis[x] < minimum:
            minimum = lis[x]
        sumtotal += lis[x]
    average = sumtotal/len(lis)
    Analysis['sumTotal'] = sumtotal
    Analysis['average'] = average
    Analysis['minimum'] = minimum 
    Analysis['maximum'] = maximum
    Analysis['length'] = length
    print (Analysis)
    return Analysis
#9.
def ReverseList(lis):
    temp=0
    for x in range(0,len(lis)//2):
        temp=lis[x]
        lis[x]=lis[len(lis)-1-x]
        lis[len(lis)-1-x]=temp
    return lis
