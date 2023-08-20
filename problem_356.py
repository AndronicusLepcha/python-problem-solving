class MyException(Exception):
    def __init__(self,msg):
        self.msg=msg
        
age=int(input('enter your age'))
if age>80:
    raise MyException('you are too old to apply')