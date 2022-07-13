
def sorti(a,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if x==a[mid]:
            return mid
        elif x<a[mid]:
            return sorti(a,low,mid-1,x)
        else:
            return sorti(a,mid+1,high,x)
    return -1
a=[1,2,3,4,5,6]

x=4
result=sorti(a,0,len(a)-1,x)
print(result)

