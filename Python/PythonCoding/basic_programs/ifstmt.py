"""
Date: 22-4-2026
Desc: learning various if statement formats
"""
#greater between 2
'''
num1 = int(input('Enter a number'))
num2 = int(input('Enter another number'))
if num1 == num2:
    print ('Both are equal.')
elif num1 > num2:
    print (num1,'is greater.')
else:
    print (num2,'is greater.')
'''


#greater between 3

'''
num1 = int(input('Enter 1st number'))
num2 = int(input('Enter 2nd number'))
num3 = int(input('Enter 3rd number'))
if num1 == num2 and num2 == num3:
    print('all values are equal')
elif num1 > num2 and num1 > num3:
    print(num1,'is greater')
elif num2 > num1 and num2 > num3:
    print(num2,'is greater')
elif num3 > num1 and num3 > num2:
    print(num3,'is greater')
'''

# weekday

ch = int(input('Enter number between 1-7'))

match ch:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Invalid choice')



