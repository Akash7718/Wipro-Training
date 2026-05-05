from oops_concept.myexception import MyException


class AgeCalculation():
    def voting_age_check(self,age):
        if age < 18:
            raise MyException('Not Eligible to vote....')
        else:
            return True

    def pension_age_check(self,age):
        if age < 60:
            raise MyException('Not eligible for pension')


