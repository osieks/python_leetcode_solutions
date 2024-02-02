import math
def binary_search(data,x):
    L = 0
    R = len(data)-1
    while L <= R:
        mid = math.floor((L+R)/2)
        #print(L,mid,R)
        if data[mid]<x:
            L=mid+1
        elif data[mid]>x:
            R=mid-1
        elif data[mid]==x:
            #print(data[L]," ",mid)
            return [data[L],mid]
        else:
            break
    return [None,None]
