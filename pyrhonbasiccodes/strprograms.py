class strprograms:
    def __init__(self,a):
        self.a=a
        print(a[:2])
        c=a.count('a')
        print(c)
        #for i in a:
         #0   print(i)

    def strreverse(self,a):
        self.a=a
        rev=''.join(reversed(self.a))
        return  rev
    def senreverse(self,a):
        self.a=a
        spliword=a.split(' ')
        print(spliword)
        splword=a.split('/')
        print(splword)
        rev=' '.join(reversed(spliword))
        return rev
    def strcount(self,a):
        self.a=a
        ch='a'
        count=0
        for i in a:
            if i in 'a':
                count+=1
        return count





strobject=strprograms("bhadra")
strrevresult=strobject.strreverse("veera")
print(strrevresult)
print(strobject.senreverse("I/ am very/ good"))
print(strobject.strcount("aabbccaa"))

