
from oops_concept.demoA import A
from oops_concept.demoB import B


class C(A, B):
    def __init__(self,n1,n2,msg):
        super().__init__(n1,n2)
        B.__init__(msg)
    