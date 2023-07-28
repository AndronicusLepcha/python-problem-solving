from random import *
alpha='abcdefghijklmnopqrstuvwxyz'
digits='123456789'
def fake_name():
    name=choice(alpha).upper()
    n=randint(2,9)
    for i in range(n):
        name=name+choice(alpha)
    return name

def fake_eid():
    eid='e-'
    for i in range(4):
        eid=eid+choice(digits)
    return eid
#print(fake_eid())

def fake_salary():
    esal=uniform(10000,100000)
    return esal
#print(fake_salary())
city=['Delhi','NAmchi','Mumbai']

def fake_city():
    ci=choice(city)
    return ci


print(fake_city())
