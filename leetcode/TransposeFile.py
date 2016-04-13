# name age
# alice 21
# ryan 30
# Output the following:

# name alice ryan
# age 21 30
from __future__ import print_function

abc = ['a', 'b', 'c']
for i in abc:
    print (i, end='')

with open('file.txt','r') as f:
	lst = [x.split() for x in f]

print (lst)
print ('----------------------------')
print (zip(*lst))

for i in zip(*lst):
    for j in i:
    	print (j+'\t', end='')
    print ('\n')
