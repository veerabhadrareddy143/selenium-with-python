import math


class basicprograms:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("construster")
        list1=[1,1,1,2,3,4,5,6,6,7]
        print(list1)
        r=set(list1)
        print(r)
    def factorial(self,a):
        self.a=a
        return 1 if (a==1 or a==0) else a * object.factorial(a-1);
        #return math.factorial(a)

    def armstrong(self, b):
        self.b=b
        p=len(str(b))
        s=b
        sum=0
        while(b!=0):
            r=b%10
            sum=sum+pow(r,p)
            b=b//10
        if s==sum:
            return "true"
        else:
            return "false"
    def prime(self,a):
        self.a=a
        if a>1:
            for i in range(2,int(a/2)+1):
                if (a%i)==0:
                    return "not a prime"
                    break
            else:
                return "prime number"
        else:
            return "not a prime number"
    def primebt(self,a,b):
        self.a=a
        self.b=b
        list=[]
        for i in range(a,b):
            if i>1:
                for num in range(2,i):
                    if(i%num)==0:
                        break
                else:
                    list.append(i)
        return list
    def fibbonacci(self,a):
        self.a=a
        num1=0
        num2=1
        list=[]
        if a<0:
            return "invalid"
        elif a==0:
            return num1
        elif a==1:
            return num2
        elif a>2:
            for i in range(2,a):
                t=num1+num2
                num1=num2
                num2=t
                list.append(num2)
            return list




"""
        if(a<0):
            return 0
        elif(a==1 or a==0):
            return 1
        else:
            fact=1
            while(a>1):
                fact*=a
                a-=1
            return  fact

"""


object=basicprograms(4,5)
result=object.factorial(5)
print(result)
armresult=object.armstrong(153)
print(armresult)
primeresult=object.prime(11)
print(primeresult)
primebtresult=object.primebt(2,15)
print(primebtresult)
fiboresult=object.fibbonacci(9)
print(fiboresult)