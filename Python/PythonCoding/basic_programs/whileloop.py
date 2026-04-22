"""
22-04-2026
Learning while loop statement
"""

#natural numbers printing

'''
num =  int(input('Enter a number'))
value = 1

while value <= num:
    print(value)
    value += 1
'''

#Amstrong number

num =  input('Enter a number')
length = len(num)
sum = 0
nm = int(num)
comp=nm
while nm > 0:
    rem = nm % 10
    sum = sum + rem**length
    nm = nm // 10
if comp == sum:
    print ("Amstrong no")
else:
    print ("not an Amstrong no")
