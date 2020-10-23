def add(p,q,r):
    return p*q*r
    
s = [10, 5, 2]
l = add(s[0],s[1],s[2])

p = add(*s)
print p
print l
