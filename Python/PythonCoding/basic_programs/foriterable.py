"""
23-04-2026
"""

#list

numbers = [11,22,94,75,43,29,75,15]

for num in numbers:
    print(num)

for num in numbers:
    print(num%10, end='\t')
print()  #for new line

#touple

numbers = (11,22,94,75,43,29,75,15)

for num in numbers:
    print(num)

for num in numbers:
    print(num%10, end='\t')
print()    #for new line

#set

numbers = {11,22,94,75,43,29,75,15}

for num in numbers:
    print(num)

for num in numbers:
    print(num%10, end='\t')
print()    #for new line

#dictionary

stud={'name':'Akash','roll':24,'city':'kolkata'}

for k,v in stud.items():
    print(k,'--',v)
