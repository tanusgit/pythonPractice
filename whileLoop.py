i = 0
while (i < 10):
      print i
      i = i + 1
      
      
      
def fib(n):
    n1 = 1
    n2 = 1
    i = 0
    while(i < n):
        print n1
        i = i+1
        temp = n2
        n2 = n1 + n2
        n1 = temp
        
 fib(5)
    
    

