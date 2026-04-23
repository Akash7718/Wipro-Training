Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
dict1={1:10,2:20:,3:30}
SyntaxError: invalid syntax
dict1={1:10,2:20,3:30}
>>> dict1
{1: 10, 2: 20, 3: 30}
>>> dict1[2]
20
>>> dict2={'a':10,'b':20,'c':30}
>>> dict2
{'a': 10, 'b': 20, 'c': 30}
>>> dict2['a']
10
>>> stud1={'name':'Akash','roll':24,'city':'kolkata'}
>>> stud1['name']
'Akash'
>>> stud1['name']='Baran'
>>> stud1
{'name': 'Baran', 'roll': 24, 'city': 'kolkata'}
>>> stud1['fname']='Akash'
>>> stud1
{'name': 'Baran', 'roll': 24, 'city': 'kolkata', 'fname': 'Akash'}
>>> stud1.keys()
dict_keys(['name', 'roll', 'city', 'fname'])
>>> stud1.values()
dict_values(['Baran', 24, 'kolkata', 'Akash'])
>>> dict1.pop['name']
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dict1.pop['name']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> dict1.pop('name')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict1.pop('name')
KeyError: 'name'
>>> stud1.pop('name')
'Baran'
>>> stud1
{'roll': 24, 'city': 'kolkata', 'fname': 'Akash'}
