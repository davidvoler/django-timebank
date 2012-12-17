def long_pol(st,mp=0):
    if len(st)<2:
        return mp
    if len(st)<=mp:
        return mp
    l=len(st)
    h=l/2
    mod=l%2
    max_pol=mod
    j=0
    is_pol=True
    for i in range(h-1,-1,-1):
        j+=1
        if st[i]==st[l-i-1]:
            max_pol=mod+j*2
            #print st[i-1:l-i+mod]
        else:
            is_pol=False
            left=long_pol(st[1:],max_pol)
            right=long_pol(st[:l-1],max_pol)
            if left>right:
                return left
            else:
                return right
    if is_pol:
        print 'polindrome[%s] length[%d]'%(st,len(st))
    return max_pol

def long_pol1(st,lp=0):
    if lp>=len(st):
        print "longest polinome %d"%lp
        exit(0)
    if len(st)<2:
        return 0
    if st==st[::-1]:
        print 'pol=[%s] length=[%d]'%(st,len(st))
        return len(st)
        exit(0)
    else:
        left=long_pol1(st[1:])
        right=long_pol1(st[:len(st)-1])
    print "no polinom found"
    return 0

def long_pol2(st):
    sb=st
    for i in range(len(st)-2):
        sb_l=sb[i:]
        if sb_l==sb_l[::-1]:
            print sb_l
            break
        sb_r=sb[:i*(-1)]
        if sb_r==sb_r[::-1]:
            print sb_r
            break
        
        if st==st[i::-1]:
            print 'pol=[%s] length=[%d]'%(st,len(st))
            return len(st)


class Tower:
    def __init__(self,ls=None):
        if ls:
            self.ls=ls
        else:
            self.ls= []
    def can_add(self,n):
        if self.ls[-1:]>n:
            return False
        else:
            return True
    def add(self,n):
        if self.ls[-1:]<n:
            self.ls.append(n)
            return True
        else:
            return False
    def get_top(self):
        return self.ls[-1:]
    def remove_top(self):
        n=self.ls[-1:]
        self.ls.remove(n)
        return n
    def get_size(self):
        return len(self.ls)

def solution():
    target=Tower()
    mid=Tower()
    src=Tower([1,2,3,4])
    while target.get_size()<4:
        if mid.can_add(src.get_top()):
            mid.add(src.remove_top())
        if target.can_add(src.get_top):
            pass
                     
    

    

#hangman
words=['help','hell','bug','hale','gale']
s="h_l_" 
for w in words:
    if len(w)!=len(s):
        print '%s does\'t match'%w
    else:
        match=True
        for i in range(len(s)):
            if s[i]=='_':
                continue
            else:
                if s[i] != w[i]:
                    match=False
                    break
        if match:            
            print '%s matches'%w
        else:
            print '%s dosn\'t match'%w

#find extra
"""
# in the example (((((A+B))*C)) we should get (A+B)*C
find the elements
A+B is an element
*C is an element
for each element decide if it requires a () around it
A+B+C does not require how do we get this
number or VAR
operator



items=re.findall(r'\w*\[+,-,]\', str)
"""


s='(((((A+B))*C))?'
open_p=0
close_p=0
for i in range(s):
    if s[i]=='(':
        open_p+=1
    elif s[i]==')':
        if open_p<1:
            print "location %d is not needed"%i 
        else:
            open_p-=1
            

            
    else:
        pass
             