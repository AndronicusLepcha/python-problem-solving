#pallindrome check
s=input('Enter the string')
if s==s[::-1]:
    print('Pallindrome')
else:
    print('! pallindrome')