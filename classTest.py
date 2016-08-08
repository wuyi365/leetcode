class A(object):
    def __init__(self, setv = 'set init class A'):
        self.setv = setv
        print(self.setv)
        print('calling class A init method')

    def testA(self, setv = ''):
        self.setv = setv
        print(self.setv)

class B(A):
    def __init__(self, setv = 'class b'):
    	A.__init__(self, setv)
        print 'calling class B init method'
   
    # def testA(self, setv = ''):
    #     self.b = set
    #     print(self.b)

b = B()
b.testA('bbb')
