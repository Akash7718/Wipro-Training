from oops_concept.agecalculation import AgeCalculation
from oops_concept.myexception import MyException

age = int(input('Age : '))

aobj = AgeCalculation()

try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)
except MyException as ae:
    print(ae)

else:
    print('Eligible')