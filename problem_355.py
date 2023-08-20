try:
    print(10/0)
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exception in try block")
finally:
    print("finallly block executed")