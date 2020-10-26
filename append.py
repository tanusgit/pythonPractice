p = [1, 9, 'apple', 3, 5]
p.append('orange')
print p
p.remove('apple')
print p
p[2] = 'banana' #changes apple to banana
print p
del p[2] # will delete the element in the 2nd position

