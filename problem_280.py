class Test:
    ''' Program to count the no of object created '''
    count =0

    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def getNoOfObject(cls):
        print("total no of object is {}".format(cls.count))

Test.getNoOfObject()
t1=Test()
t2=Test()
Test.getNoOfObject()