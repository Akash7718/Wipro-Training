import re

#begening and end matching of a string
'''atxt = input('Enter a text :')

bpat = input('Enter beginning pattern :')
epat = input('Enter ending pattern :')
bpat = '^'+ bpat
epat = epat+'$'
if re.search(pattern=bpat,string=txt):
    print('Beginning pattern available')
else:
    print('Beginning pattern not available')

if re.search(pattern=epat,string=txt):
    print('Ending pattern available')
else:
    print('Ending pattern not available')
'''

'''mbno = input('Enter a txt :')
pat = r"\d"

if re.fullmatch(pattern=pat,string=mbno):
    print('Only digits')
else:
    print('Other characters available')'''

#user name
'''un = input('Enter user name :')
pat = r"[a-z]{8}"  #exactly 8 characters

if re.match(pattern=pat,string=un):
    print('Valid')
else:
    print('Invalid')'''

#email

'''emailadd = input('Enter email')
pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"
if re.match(pattern=pat,string=emailadd):
    print('valid')
else:
    print('not valid')'''


#password

'''pwd= input('enter password :')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"
if re.match(pattern=pat,string=pwd):
    print('valid')
else:
    print('not valid')
'''
'''txt = input('Text')
pat =r"\s+"

#print(re.sub(pattern=pat,string=txt,repl='*'))
print(re.split(pattern=pat,string=txt))'''
