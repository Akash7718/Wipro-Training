
#natural numbers

'''
num = int(input('Enter a number'))
sum = 0
for i in range(1, num+1):
    sum = sum + i**2
print ('sium of sqt of n numbers:', sum)
'''

#print * for n times

num = int(input('Enter a number'))
for _ in range(1,num+1):
    print('*',sep=' ',end='\t')

#OUTPUT = *	*	*	*	*

for _ in range(1,num+1):
    print('*',sep=' ',end='_______')

#OUTPUT = *_______*_______*_______*_______*_______

for _ in range(1,num+1):
    print('*','&',sep='$$$',end='\t')

#OUTPUT = *$$$&	*$$$&	*$$$&	*$$$&	*$$$&

