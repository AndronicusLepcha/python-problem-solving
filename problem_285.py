class Outer:
    def __init__(self):
        print('this is outer class')
    class Inner:
        def __init__(self):
            print('this is inner class')
        def m1(self):
            print('This is inner classs method')

o=Outer().Inner().m1()

